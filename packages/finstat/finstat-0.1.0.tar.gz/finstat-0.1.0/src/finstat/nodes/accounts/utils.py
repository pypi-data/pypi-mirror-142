import typing as typ
import functools as ft
import pandas as pd
from pandas.core.groupby import DataFrameGroupBy

def _constructor_wrapper(func, self):
    """
    Takes output from a DataFrameGroupBy method, then 
    reinstantiates the object and passing additional data specific to a
    finstat object 
    """
    @ft.wraps(func)
    def wrapper(*args, to_account:bool=False, **kwargs):
        ret = func(self, *args, **kwargs)
        
        result = self.obj._constructor(ret.values, index=ret.index, columns=ret.columns, **ret._metaparams, **kwargs)
        
        if to_account and result.has_single_row:
            result = result.to_account()

        return result
    
    return wrapper

class AccountGroupBy(DataFrameGroupBy):
    """
    Customized groupby class to control type of the output frame
    """
    def __getattribute__(self, name):
        WRAPPED_FUNCS = ['sum', 'last']
        if name in WRAPPED_FUNCS:
            func = super().__getattribute__(name)
            return _constructor_wrapper(func, self)
        else:
            return super().__getattribute__(name)
