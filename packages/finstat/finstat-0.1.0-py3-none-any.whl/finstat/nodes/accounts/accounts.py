from multiprocessing.sharedctypes import Value
import typing as typ
import numpy as np
import pandas as pd

AccountsType = typ.TypeVar('AccountsType', bound='Accounts')

def index_fillers(common_idx):
    fillers = []
    for i, col in common_idx.to_frame().iteritems():
        if pd.api.types.is_period_dtype(col):
            fillers.append(pd.Period('1900-1-1', freq='d'))
        elif pd.api.types.is_numeric_dtype(col):
            fillers.append(0)
        else:
            fillers.append('---')
    return fillers

def index_values(common_idx, holder='Other'):
    """
    Creates index values for 'Other' row created for MultiLevelAccount objects that are created via
    a MetricFunction or concating a set of Account objects.

    Index value is '---' or np.nan depending on dtype of the index value.

    Parameters
    -----------
    common_idx: pd.Index
        Index resulting from call to `common_level_values` method of Accounts object
    """
    fillers = index_fillers(common_idx)
    row = tuple([holder] + fillers[1:]) if len(fillers) > 1 else holder

    return row

class concat:
    """
    Object-based concat method for Accounts object. Handles different instances and
    combinations of Account objects and MultiLevelAccount objects.
    """
    def __init__(self, accounts:AccountsType):
        self.accounts = accounts
    
    def _account_only_concat(self):
        concatted = pd.concat(self.accounts, axis=1).T
        concatted.index.name = 'Account'
        concatted.index = pd.CategoricalIndex(
            concatted.index, 
            categories=self.accounts.names, 
            ordered=True, 
            name='Account'
        )
        return concatted

    def _multi_level_concat(self, shared_levels:typ.Iterable=None, other=True):
        accounts = self.accounts.to_multi()
        grouped = accounts.align_indexes(shared_levels)
        grouped = grouped.insert_account_level()
        
        concatted = pd.concat(grouped)
        concatted.categorize_level('Account', self.accounts.names)
        return concatted
    
    def __call__(self, *args, **kwargs):
        if self.accounts.is_multi.any() and not self.accounts.have_single_row.all():
            concatted = self._multi_level_concat(*args, **kwargs)
        else:
            concatted = self._account_only_concat()

        return concatted

class Accounts(np.ndarray):
    """
    Container for Account objects. Standard numpy methods and attributes are available.

    Includes several helper methods for manipulating sets of Account objects used in 
    MetricFunction and FinancialStatment.

    Issues arise from assigning Account objects directly to `obj`, so the str representation is instead.
    The underlying items manipulated are still the Account objects, given changes to __getitem__

    Parameters:
        accounts: iterable of Account objects
    """

    def __new__(cls, *accounts):
        obj = np.asarray([a.name for a in accounts], dtype='object').view(cls)
        obj._accounts = [a for a in accounts]
        return obj
    
    def __init__(self, *accounts):
        self.concat = concat(self)

    def __array_finalize__(self, obj):
        if obj is None: return
        
    def __repr__(self):
        joined = ', '.join([s.name for s in self._accounts])
        return f'Accounts([{joined}])'

    def __getitem__(self, item):
        """
        Overriden to allow access to underlying Account objects, instead of the str representation
        """
        if isinstance(item, slice):
            return Accounts(*self._accounts[item])
        if isinstance(item, tuple):
            item = slice(*item)
        return self._accounts[item]

    def __add__(self, accounts):
        return Accounts(*[acct for acct in self._accounts] + [acct for acct in accounts])

    @property
    def _index_names(self):
        return [np.array(acct.index.names) for acct in self._accounts]

    @property
    def names(self):
        return np.array([acct.name for acct in self._accounts])

    @property
    def short_names(self):
        return np.array([acct.short_name for acct in self._accounts])

    @property
    def hides(self):
        return np.array([acct.hide for acct in self._accounts])

    @property
    def visible(self):
        return Accounts(*[acct for acct in self._accounts if not acct.hide])

    @property
    def is_multi(self):
        return np.array([acct.is_multi for acct in self._accounts])

    @property
    def are_aligned(self):
        return all([self._accounts[0].index.equals(acct.index) for acct in self._accounts[1:]])

    @property
    def have_single_row(self):
        return np.array([acct.has_single_row for acct in self._accounts])

    def groupby(self, by, funcstr, to_account:bool=False):
        return Accounts(*[getattr(acct.groupby(by), funcstr)(to_account=to_account) for acct in self._accounts])

    def resample(self, freqstr, funcstr, **kwargs):
        return Accounts(*[acct.resample(freqstr, funcstr, **kwargs) for acct in self._accounts])

    @property
    def commonize(self):
        """
        Filters out Account objects that should not be aggregated on common index values. This includes
        Account objects with `_multi_index` attribute, which indicates they are an aggregate account from
        a `total()` call.
        """
        return Accounts(*[acct for acct in self._accounts])

    def idx_frames(self):
        return [acct.index.to_frame().reset_index(drop=True).apply(lambda col: col.astype(object)) for acct in self._accounts]

    def shared_levels(self):
        """
        Finds the intersection of level names among all Account objects
        """
        unq, counts = np.unique(np.concatenate(self._index_names), return_counts=True)
        shared = unq[counts == self.size]
        return [acct for acct in self._index_names[0] if acct in shared]

    def common_level_values(self):
        """
        Finds the common level values among the indexes of each of the Account objects in
        the Accounts container. These values are used from concat and MetricFunction

        Parameters:
            as_index: bool
                if True, returns a MultiIndex. If False, returns DataFrame. Default True.
        """
        accts_to_commonize = self.commonize
        first, rest = accts_to_commonize.idx_frames()[0], accts_to_commonize.idx_frames()[1:]
        if rest:
            for nxt in rest:
                merged = pd.merge(first, nxt, how='outer', indicator=True)
                first = merged[merged._merge == 'both'].drop(columns='_merge')
            merged = merged.where(merged._merge == 'both').dropna().drop(columns='_merge')
        else:
            merged = first
        merged = pd.MultiIndex.from_frame(merged)   
        if merged.nlevels == 1:
            merged = merged.get_level_values(0)

        return merged

    def align_indexes(self, shared_levels:typ.Iterable=[]):
        shared_levels = shared_levels if shared_levels else self.shared_levels()
        grouped = self.group_on_shared(shared_levels).drop_account_level()
        common_idx = grouped.common_level_values()
        terms = []
        for acct in grouped:
            uncommon = acct.loc[acct.index.difference(common_idx)]
            if not uncommon.empty:
                other_row = uncommon.sum().rename(index_values(common_idx))
                acct = acct.loc[common_idx].append(other_row.to_series())
            terms.append(acct)

        return Accounts(*terms)

    def group_on_shared(self, shared_levels):
        return Accounts(*[acct.groupby(shared_levels).sum() for acct in self._accounts])

    def to_multi(self):
        return Accounts(*[acct.to_multi() if not is_multi else acct for is_multi, acct in zip(self.is_multi, self._accounts)])

    def to_accounts(self):
        return Accounts(*[acct.to_account() if single else acct for single, acct in zip(self.have_single_row, self._accounts)])

    def drop_account_level(self):
        return Accounts(*[acct.droplevel('Account') if 'Account' in acct.index.names else acct for acct in self._accounts])

    def insert_account_level(self):    
        return Accounts(*[acct.insert_account_level() for acct in self._accounts])
    
    def by_position(self):
       return Accounts(*sorted(self._accounts, key=lambda n: n.graph.nodes[n.short_name]['position']))
