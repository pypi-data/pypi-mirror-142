import warnings
import typing as typ
import numpy as np
import pandas as pd

import networkx as nx

from ..node import NodeMixin
from ..input import Input
from .utils import AccountGroupBy
from .accounts import index_values, Accounts
from ..metric import mathwrap, multimathwrap, metricize

class Account(NodeMixin, pd.Series):
    """
    Root class for constructing FinancialStatement objects. Extends pandas Series object.
    """
    _metadata = ['_short_name', '_periods', '_graph', '_hide']

    @property
    def _constructor(self):
        return Account
    
    @property
    def _constructor_expanddim(self):
        warnings.warn('Account methods that call `_constructor_expanddim` return a standard DataFrame (e.g. pd.concat)')
        return super()._constructor_expanddim

    def __init__(self, values, 
        name:str=None, 
        short_name:str=None, 
        graph:nx.DiGraph=None, 
        hide:bool=False,
        ffill:typ.Union[int, float]=None,
        **kwargs
    ): 
        values = self._clean_values(values, ffill, **kwargs)
        super().__init__(values, name=name, **kwargs)

        self._short_name = None
        if short_name:
            self._short_name = short_name
        elif name is not None:
            if not isinstance(name, (pd.Period, tuple)): # when pd.Period or tuple is passed, this is result of _constructor_sliced call from MultiLevelAccount
                self._short_name = self._shorten(name)

        self._graph = graph
        self._hide = hide
        self._periods = self.index

    def __hash__(self):
        return hash(self._name)

    @mathwrap
    def __add__(self, item, **kwargs):
        return self.singlemath(item, '__add__', **kwargs)

    @mathwrap        
    def __radd__(self, item, **kwargs):
        item = item.value if isinstance(item, Input) else item
        return self.singlemath(item, '__radd__', **kwargs)

    @mathwrap
    def __sub__(self, item, **kwargs):
        return self.singlemath(item, '__sub__', **kwargs)

    @mathwrap
    def __rsub__(self, item, **kwargs):
        item = item.value if isinstance(item, Input) else item
        return self.singlemath(item, '__rsub__', **kwargs)

    @mathwrap
    def __mul__(self, item, **kwargs):
        return self.singlemath(item, '__mul__', **kwargs)

    @mathwrap
    def __rmul__(self, item, **kwargs):
        item = item.value if isinstance(item, Input) else item
        return self.singlemath(item, '__rmul__', **kwargs)

    @mathwrap
    def __truediv__(self, item, **kwargs):
        return self.singlemath(item, '__truediv__', **kwargs)

    @mathwrap
    def __rtruediv__(self, item, **kwargs):
        item = item.value if isinstance(item, Input) else item
        return self.singlemath(item, '__rtruediv__', **kwargs)

    def singlemath(self, item, funcname:str, **kwargs):
        shared_levels = kwargs.pop('shared_levels', []) # Shared levels not required for Account objects

        value = item.value if isinstance(item, Input) else item
        result = getattr(super(), funcname)(value)

        if result is NotImplemented:
            return result
        else:
            return result._constructor(result.values, index=result.index, **kwargs)

    @property
    def _metaparams(self):
        """
        Used to pass metadata as kwargs on _constructor calls.

        Used in _constructor_wrapper
        """
        metaparams = super()._metaparams
        metaparams.pop('periods')
        metaparams['name'] = self.name
        return metaparams
    
    @property
    def has_single_row(self):
        return True

    @property
    def is_multi(self):
        return False

    def _clean_values(self, values, ffill:typ.Any, index:typ.Iterable=None, **kwargs):
        """
        If a scalar is provided and the index length is > 1, this automatically fills
        out the rest of the series with the value indicate by `ffill`
        """
        has_index = index is not None and len(index) > 1
        scalar = isinstance(values, (int, float, Input, str, np.number))
        
        if not scalar:
            scalar = values.size == 1 if hasattr(values, 'size') else len(values) == 1
            
        if has_index and scalar:
            values = values*np.concatenate((np.ones(1), np.ones(len(index)-1)*ffill))
            
        return values

    def update(self, data:typ.Union[dict, list]):
        """
        Assigns new values to object and cascades updates
        to any successor nodes.

        Data to update successors is calculated using the Metric keywords stored
        in each successor node.
        """
        if isinstance(data, dict):
            self.loc[list(data.keys())] = list(data.values())
        else:
            self.iloc[:len(data)] = data

        self._push_updates()

    def to_series(self):
        return pd.Series(self.values, index=self.index, name=self.name)

    def to_multi(self, index:pd.MultiIndex=None):
        return MultiLevelAccount(
            self.values.reshape(1,-1), 
            index=index, 
            columns=self.index,
            **self._metaparams
        )

    def resample(self, freq:str='A-DEC', func:str='sum', **kwargs):
        resampler = super().resample(freq, **kwargs)
        result = getattr(resampler, func)()
        return result._constructor(result.values, index=result.index, **self.set_constructor_kwargs(kwargs))

    @metricize
    def cumsum(self, **kwargs):
        result = super().cumsum()
        return result._constructor(result.values, index=result.index, **self.set_constructor_kwargs(kwargs))

    @metricize
    def cum_growth(self, **kwargs):
        result = (1 + self).cumprod()
        return result._constructor(result.values, index=result.index, **self.set_constructor_kwargs(kwargs))

    @metricize
    def where(self, func, comp, if_true=None, if_false=None, if_true_neg:bool=False, if_false_neg:bool=False, **kwargs):
        if_true = self if if_true is None else if_true
        if_false = comp if if_false is None else if_false

        if isinstance(if_true, MultiLevelAccount):
            if_true = if_true.sum()

        if isinstance(comp, MultiLevelAccount):
            comp = comp.sum()

        if if_true_neg:
            if_true = -if_true
        if if_false_neg:
            if_false = -if_false
    
        result = np.where(func(self, comp), if_true, if_false)
        return self._constructor(result, index=self.index, **self.set_constructor_kwargs(kwargs))

class MultiLevelAccount(NodeMixin, pd.DataFrame):
    _metadata = Account._metadata + ['_name']

    @property
    def _constructor(self):
        return MultiLevelAccount
    
    @property
    def _constructor_sliced(self):
        return Account
    
    def __init__(self, 
        values,
        name:str=None, 
        short_name:str=None, 
        graph:nx.DiGraph=None, 
        index:pd.Index=None, 
        hide:bool=False,
        **kwargs
    ):
        index = self._clean_index(index, name)
        super().__init__(values, index=index, **kwargs)
        
        self._name = name
        self._short_name = short_name if short_name else (self._shorten(name) if name else None)
        self._graph = graph
        self._hide = hide
        self._periods = self.columns

    def _clean_index(self, index:pd.Index, name:str):
        """
        Attaches 'Account' level to index if it does not already exist

        Account is only attached if 'Account' is not already in the index and
        the object has not been instantiaed through a call to _constructor
        
        The other approach is to override the various methods with _constructor calls to pass a
        flag that prevents the `_reindex` call.
        """
        if index is not None and name is not None:
            if isinstance(index, pd.Index) and index.name == 'Account':
                index = pd.Index([name], name='Account')
            elif 'Account' in index.names:
                index = index.droplevel('Account')

            if not 'Account' in index.names:
                index = self.insert_account_level_in_index(index, name)

        return index

    def multimath(self, item, funcname, **kwargs):
        shared_levels = kwargs.pop('shared_levels', [])
        if isinstance(item, Input):
            item = item.value
        elif isinstance(item, MultiLevelAccount): # if both terms are MultiLevelAccount, must insure the indices are aligned
            accounts = Accounts(self, item)
            if not accounts.are_aligned:
                left, right = accounts.align_indexes(shared_levels)
                return getattr(left, funcname)(right, **kwargs) # passes right back to `multimath` which will now find accounts.are_aligned == True
        
        result = getattr(super(), funcname)(item)

        return self._constructor(result.values, index=result.index, columns=result.columns, **kwargs)

    @multimathwrap
    def __add__(self, item, **kwargs):
        return self.multimath(item, '__add__', **kwargs)

    @multimathwrap
    def __radd__(self, item, **kwargs):
        return self.multimath(item, '__radd__', **kwargs)

    @multimathwrap
    def __sub__(self, item, **kwargs):
        return self.multimath(item, '__sub__', **kwargs)

    @multimathwrap
    def __rsub__(self, item, **kwargs):
        return self.multimath(item, '__rsub__', **kwargs)

    @multimathwrap
    def __mul__(self, item, **kwargs):
        return self.multimath(item, '__mul__', **kwargs)

    @multimathwrap
    def __rmul__(self, item, **kwargs):
        return self.multimath(item, '__rmul__', **kwargs)

    @multimathwrap
    def __truediv__(self, item, **kwargs):
        return self.multimath(item, '__truediv__', **kwargs)

    @multimathwrap
    def __rtruediv__(self, item, **kwargs):
        return self.multimath(item, '__rtruediv__', **kwargs)

    @property
    def _metaparams(self):
        """
        Used to pass metadata as kwargs on _constructor calls.

        Used in _constructor_wrapper
        """
        metaparams = super()._metaparams
        metaparams['name'] = self.name
        metaparams.pop('periods')
        return metaparams

    @property
    def name(self):
        return self._name

    @property
    def is_multi(self):
        return True

    @property
    def has_single_row(self):
        return self.shape[0] == 1

    def insert_account_level_in_index(self, index, name:str=None):
        name = self.name if name is None else name
        frame = index.to_frame().reset_index(drop=True)
        frame.insert(0, 'Account', name)

        return pd.MultiIndex.from_frame(frame)

    def insert_account_level(self, name:str=None):
        """
        Inserts an 'Account' level into the index of the Account object passed.

        Parameters:
            account: Account
        """
        acct = self.copy()
        idx = self.insert_account_level_in_index(acct.index, name)
        acct.index = idx

        return acct

    def categorize_level(self, name, categories):
        idx_frame = self.index_as_frame
        cats = pd.Categorical(idx_frame[name], categories=categories, ordered=True)
        idx_frame.loc[:, name] = cats
        self.index = pd.MultiIndex.from_frame(idx_frame)

    def groupby(
        self,
        by=None,
        axis=0,
        level:None=None,
        *args, **kwargs
        ):
        """Ripped from pandas groupby"""

        if level is None and by is None:
            raise TypeError("You have to supply one of 'by' and 'level'")

        return AccountGroupBy(
            obj=self,
            keys=by,
            axis=self._get_axis_number(axis),
            level=level,
            *args, **kwargs
        )

    @metricize
    def sum(self, *args, **kwargs):
        result = super().sum()
        kwargs = result.set_constructor_kwargs(kwargs)
        for k, v in kwargs.items(): # `sum` will not pass any _metaparams, so `set_constructor_kwargs` will be full on None that should be replaced
            if v is None:
                kwargs[k] = self._metaparams[k]

        return result._constructor(result.values, index=result.index, **kwargs)

    @metricize
    def total(self, item=None, **kwargs):
        if 'name' not in kwargs or kwargs['name'] is None:
            kwargs['name'] = 'Total ' + self.name
            kwargs['short_name'] = 'tot_' + self.short_name
        
        index_name =  index_values(self.index, kwargs['name'])
        index = pd.MultiIndex.from_tuples([index_name], names=self.index.names)
        
        total = self.sum().to_multi(index)

        return self._constructor(total.values, index=total.index, columns=total.columns, **self.set_constructor_kwargs(kwargs))

    @metricize
    def cumsum(self, **kwargs):
        cumsum = super().cumsum(axis=1)
        return self._constructor(cumsum.values, index=cumsum.index, columns=cumsum.columns, **self.set_constructor_kwargs(kwargs))

    @metricize
    def where(self, func, comp, if_true=None, if_false=None, if_true_neg:bool=False, if_false_neg:bool=False, **kwargs):
        if_true = self if if_true is None else if_true
        if_false = comp if if_false is None else if_false

        if if_true_neg:
            if_true = -if_true
        if if_false_neg:
            if_false = -if_false

        result = np.where(func(self, comp), if_true, if_false)

        return self._constructor(result, index=self.index, columns=self.columns, **self.set_constructor_kwargs(kwargs))

    def resample(self, freq='A-DEC', func:str='sum', **kwargs):
        """
        Resample data structure along the columns / periods axis.

        Unlike Account objects, MultiLevelAccount objects must be rotated via `T` then resampled, then rotated back. This is not
        currently supported by MultiLevelAccount, so the pd.DataFrame is used and the MultiLevelAccount reconsituted via
        `_constructor`.
        """
        resampler = self.to_frame().T.resample(freq, **kwargs)
        resampled = getattr(resampler, func)().T

        return self._constructor(resampled, **self._metaparams)

    def update(self, data:typ.Union[dict, list]):
        """
        Assigns new values to object and cascades updates
        to any successor nodes.

        Data to update successors is calculated using the Metric keywords stored
        in each successor node.
        """
        if isinstance(data, dict):
            for k, v in data.items():
                self.loc[k] = v
        elif isinstance(data, MultiLevelAccount):
            for k, v in data.__dict__.items(): # assumes that `data` should fully replace the entire object; this is true if `update` is called in `_push_updates`
                if k not in self._metaattrs:
                    setattr(self, k, v)
        else:
            self.iloc[:len(data)] = data

        self._push_updates()

    def to_frame(self, columns_as_periods:bool=True, strftime:str='%b-%Y'):
        frame = super().to_frame()
        if not columns_as_periods and isinstance(frame.columns, pd.PeriodIndex):
            frame.columns = frame.columns.strftime(strftime)
        return frame

    def to_account(self):
        if self.shape[0] > 1:
            raise ValueError('Only MultiLevelAccount objects with a single row can be converted to Account objects.')
        
        return Account(
            self.values[0],  
            index=self.columns,
            **self._metaparams
        )
