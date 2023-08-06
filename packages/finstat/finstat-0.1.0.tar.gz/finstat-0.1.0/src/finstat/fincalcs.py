import numpy as np
import pandas as pd
from typing import Iterable

def cagr(fv, pv, t):
    """
    Computes compound annual growth rate implied by two values over a time, t

    Params
    -------
    fv:     float, future value
    pv:     float, present value
    t:      time between values in years
    """
    return (fv / pv)**(1/t) - 1

def discount_factors(cf, discount, t):
    return (1 + discount)**np.arange(t, cf.shape[0] + t)

def wacc_calc(cost_debt, cost_equity, debt_to_cap):
    return (cost_debt*debt_to_cap) + (cost_equity*(1-debt_to_cap))

def npv(cf, disc=.08):
    """
    Net Present Value calculation for a stream of cash flows
    
    Params
    -------
    cf:    nxm array of cash flow streams
            > n = # of years
            > m = # of different cash flow streams
    disc:  float representing annual discount rate
            > default value per Duff&Phelps recommendation here:
                https://www.duffandphelps.com/-/media/assets/pdfs/publications/articles/dp-erp-rf-table-2020.pd
    
    Returns
    --------
        nxm array representing of each cash inflow discounted to the current day
    """
    return cf.values.reshape(-1,cf.ndim) / (1+disc)**np.arange(0, cf.shape[0]).reshape(-1,1)

def logparams(x1, y1, x2, y2):
    """
    Returns parameters for line of form 
    
    y = a*ln(b*x)
    
    https://math.stackexchange.com/questions/716152/graphing-given-two-points-on-a-graph-find-the-loglarithmic-function-that-passes
    """
    a = (y1 - y2) / np.log(x1 / x2)
    b = np.exp((y2*np.log(x1) - y1*np.log(x2)) / (y1 - y2))
    
    return a, b

def logline(x, a, b):
    xdim = b.shape[0]
    x = x.repeat(xdim).reshape(-1,xdim)
    a = a.reshape(-1,1)
    b = b.reshape(-1,1)

    return a*np.log(b*x.T)

def log_returns(ser):
    if not isinstance(ser, pd.Series):
        ser = pd.Series(ser)
    return np.log(ser / ser.shift(1)).iloc[1:]

