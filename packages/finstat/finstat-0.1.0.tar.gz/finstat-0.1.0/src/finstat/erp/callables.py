import string
import typing as typ
import numpy as np
import pandas as pd

from .erp import Schedule
from ..nodes.input import Input

def sales_invoice_generator(
    customer:str,
    sales_deposit_per:float, 
    sales_deposit_amount:float, 
    sales_deposit_date:pd.Period,
    sales_deposit_bank:bool,
    pmt_at_ship:float,
    sales_terms:str, 
    watts:float,
    rev_per_watt:float,
    n_orders:int,
    n_months:int,
    last_ship_date:str,
    ):
    watts_per_order = watts / n_orders
    invoice_amount = watts_per_order*rev_per_watt
 
    end = last_ship_date.to_timestamp()
    start =  end - pd.DateOffset(months=n_months)
    ndays = (end - start).days // n_orders
    ship_dates = pd.date_range(end=end, periods=n_orders, freq=f'{ndays}D')
    inv = pd.Series({
        'Customer': customer,
        'Terms': sales_terms,
    })
    invoices = pd.concat([inv.to_frame().T]*n_orders)

    sales_sched = Schedule(invoices, name='Sales Invoices', short_name='sales_invoices')
    
    sales_sched.insert(2, 'Invoice No', np.arange(sales_sched.shape[0]) + 1)

    sales_sched.loc[:, 'Deposit Date'] = sales_deposit_date
    sales_sched.loc[:, 'Ship Date'] = ship_dates.to_period('d')
    net_days = pd.to_timedelta(sales_sched.Terms.str.lstrip('net ').astype('int'), unit='D')
    sales_sched['Due Date'] = sales_sched['Ship Date'] + net_days
    sales_sched['Actual Date'] = sales_sched['Due Date']

    sales_sched.loc[:, 'Amount'] = invoice_amount
    if sales_deposit_bank:
        deposit_required = np.where(sales_sched.Amount.cumsum() <= sales_deposit_amount, 1, 0) # cumulative value of revenue
    else:
        deposit_required = sales_deposit_per
    
    sales_sched.loc[:, 'Deposit Per'] = deposit_required
    sales_sched.loc[:, 'Deposit Amount'] = sales_sched.Amount * sales_sched['Deposit Per']
    sales_sched.loc[:, 'At Shipment'] = np.where(deposit_required == 1, 0, pmt_at_ship)
    sales_sched.loc[:, 'Shipment Amount'] = sales_sched['At Shipment'] * sales_sched.Amount
    sales_sched.loc[:, 'Due Amount'] = sales_sched.Amount - sales_sched['Deposit Amount'] - sales_sched['Shipment Amount']

    sales_sched = sales_sched.reset_index(drop=True)
    
    return sales_sched

def purchase_invoice_generator(
    watts:float,
    rev_per_watt:float,
    n_orders:int,
    n_suppliers:int,
    supply_deposit_bank:bool,
    supply_deposit_per:float,
    supply_deposit_amount:float,
    supply_deposit_date:str,
    supply_terms:str,
    expected_margin:float,
    names:np.ndarray,
    cost:np.ndarray,
    leads:np.ndarray,
    sales_invoices:Schedule,
):  
    watts_per_order = watts / n_orders
    invoice_amount = watts_per_order*rev_per_watt

    purchases = pd.DataFrame([names, cost, leads], index=["Supplier", "Cost Portion", "Lead Time"]).T
    purchases = pd.concat([purchases]*n_orders)

    purchases = Schedule(purchases, name='Purchase Invoices', short_name='purchase_invoices')

    purchases.insert(1, 'Terms', supply_terms)
    purchases.insert(2, 'Invoice No', np.repeat(np.arange(n_orders), n_suppliers) + 1)
    purchases.insert(2, 'Order No', np.arange(n_orders*n_suppliers))

    purchases.loc[:, 'Deposit Date'] = supply_deposit_date
    purchases.loc[:, 'Ship Date'] = np.repeat(pd.PeriodIndex(sales_invoices['Ship Date']).to_timestamp(), n_suppliers).values - purchases['Lead Time'].apply(pd.Timedelta, unit='D').values
    purchases['Ship Date'] = pd.DatetimeIndex(purchases['Ship Date']).to_period('D')

    def find_ship_date(x):
        return sales_invoices['Ship Date'][sales_invoices['Invoice No'] == x].iloc[0]

    purchases.loc[:, 'Recognition Date'] = purchases['Invoice No'].apply(lambda x: find_ship_date(x))

    net_days = pd.to_timedelta(purchases.Terms.str.lstrip('net ').astype('int'), unit='D')
    purchases['Due Date'] = purchases['Ship Date'] + net_days
    purchases['Actual Date'] = purchases['Due Date']

    purchases['Amount'] = purchases['Cost Portion'] * invoice_amount * (1 - expected_margin)

    if supply_deposit_bank:
        deposit_required = np.where(purchases.Amount.cumsum() <= supply_deposit_amount, 1, 0) # cumulative value of revenue
    else:
        deposit_required = supply_deposit_per

    purchases.loc[:, 'Deposit Per'] = deposit_required
    purchases.loc[:, 'Deposit Amount'] = purchases.Amount * purchases['Deposit Per']
    purchases.loc[:, 'Due Amount'] = purchases.Amount - purchases['Deposit Amount']
    
    return purchases
