import typing as typ
import pandas as pd

from .fincalcs import discount_factors

class Valuation:
    def __init__(self, cash_flows:typ.Iterable, discount:float, fwd_multiple:float, t=1):
        self.cash_flows = cash_flows
        self.discount = discount
        self.fwd_multiple = fwd_multiple
        self.t = t
        
        idx = self.cash_flows.index
        self.tvidx = pd.period_range(start=idx[0], periods=idx.size + 1, freq=idx.freqstr)
    
    @property
    def discount_factors(self):
        return discount_factors(self.cash_flows_with_tv(), self.discount, self.t)
    
    @property
    def terminal_value(self):
        return self.cash_flows.iloc[-1] * self.fwd_multiple        

    @property
    
    def tv(self):
        return self.terminal_value
    
    @property
    def discounted_tv(self):
        return self.discounted_cash_flows().iloc[-1]

    def cash_flows_with_tv(self):
        ser = pd.concat((self.cash_flows, pd.Series([self.terminal_value])))
        ser.index = self.tvidx
        return ser
    
    def discounted_cash_flows(self):
        return self.cash_flows_with_tv() / self.discount_factors

    def fair_value(self):
        return self.discounted_cash_flows().sum()
    
    def tv_per_fv(self):
        return self.discounted_tv / self.fair_value()
    
    def __call__(self):
        return self.fair_value()
