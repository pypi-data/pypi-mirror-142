import typing as typ
import inspect
import numpy as np
import pandas as pd

import networkx as nx

from ..nodes.node import NodeMixin
from ..nodes.input import Input
from ..nodes.accounts import MultiLevelAccount
from ..nodes.metric import MetricFunction

ScheduleType = typ.TypeVar('ScheduleType', bound='Schedule')

# Helpers map list of value and date items to a schedule containing
# all dates in a given set of periods
def _create_arr(values:np.ndarray, periods:pd.PeriodIndex) ->  np.ndarray:
    """
    Creates m x n array, where m is df.shape[0], or the number of values to be mapped, and n is len(periods), or the number of dates
    available on which values can be mapped. Each row in the array contains only one value in the index == 0 location of that row.
    
    Parameters:
        values: pandas Series or numpy n x 1 ndarray
        periods: pandas PeriodIndex
            
    Return:
        arr: (m x n) numpy ndarray
            m == len(values), or the number of items to be mapped and n == len(periods), or the number of periods considered.
            arr contains one value per row, all in the index 0 location of that row.
    """
    arr = np.zeros((len(values), periods.size))
    arr[:, 0] = values
    
    return arr

def relocate(arr:np.ndarray, locs:np.ndarray, direction:str='forward') -> np.ndarray:
    """
    Intermediate helper that shifts each index 0 location value in `arr` to the location found in `locs`.
    
    Numba could be used to improve speed for large `arr`.
    
    `ogrid` is used to produce arrays of row and column indices. The locations are then subtracted from the
    column indices. `arr` is then resorted with update column indices. This results in the values at index 0 
    moving to the index location specified in `locs`. 

    Parameters:
        values: pandas Series or numpy n x 1 ndarray
        periods: pandas PeriodIndex
            
    Return:
        arr: (m x n) numpy ndarray
            m == len(values), or the number of items to be mapped and n == len(periods), or the number of periods considered.
            arr contains one value per row, each value positioned in the index location specified by `locs`.

    """
    rows, column_indices = np.ogrid[:arr.shape[0], :arr.shape[1]]
    if direction == 'forward':
        column_indices = column_indices - locs[:, np.newaxis]
    elif direction == 'backward':
         column_indices = column_indices + locs[:, np.newaxis]
    return arr[rows, column_indices]

def map_to_periods(values:np.ndarray, dates:np.ndarray, periods:pd.PeriodIndex) -> np.ndarray:
    """
    Process:
        1. Create m x n array for each m item in df to be mapped and n periods on which the values are to be mapped
        2. 
    
    Parameters:
        values: n x 1 np.ndarray
        dates: n x 1 np.ndarray of datetime-like objects
        periods: pandas PeriodIndex

    Return:
        arr: (m x n) numpy ndarray
            m == len(values), or the number of items to be mapped and n == len(periods), or the number of periods considered.
            arr contains one value per row, each value positioned in the index location specified by `locs`.
    """
    arr = _create_arr(values, periods)
    locs = periods.searchsorted(dates)
    arr = relocate(arr, locs)
    
    return arr

class ScheduleMaker:
    def __init__(self, schedfunc:typ.Callable, finstat:'FinancialStatement'=None, **kwargs):
        self.EXPECTED_INPUTS = inspect.getfullargspec(schedfunc).annotations
        self.schedfunc = schedfunc
        self.inputs = {}
        self.finstat = finstat
        if finstat is not None:
            for input in self.EXPECTED_INPUTS:
                self.inputs[input] = getattr(finstat, input)
        else:
            for k, v in kwargs.items():
                if k in self.EXPECTED_INPUTS:
                    self.inputs[k] = Input(name=k, value=v) if self.EXPECTED_INPUTS[k] is not Schedule and not isinstance(v, Input) else v # when another schedule is passed don't make it an input

    @property
    def raw_inputs(self):
        return {k: v.value if isinstance(v, Input) else v for k, v in self.inputs.items()}

    def make(self, *args, **kwargs):
        sched = self.schedfunc(**self.raw_inputs)
        sched.add_inputs(self.inputs)
        sched.set_maker(self)
        if self.finstat is not None:
            sched.set_graph(self.finstat.graph)

        return sched

class ScheduleFunction(MetricFunction):
    def __init__(self, left:ScheduleType, func='map_schedule', right=None, **func_kwargs):
        """
        ScheduleFunction accepts kwargs to mirror behavior of MetricFunction.
        It is passed right, funcname, and func_kwargs keywords in MetricGraph, which are ignored.
        """
        self.left = left
        self.right = None
        self.funcstr = func
        self._func_args = {}
        self._func_kwargs = func_kwargs

    @property
    def _constructor(self):
        return ScheduleFunction

    def __repr__(self):
        return f'ScheduleFunction: {self.funcstr}'

    def find_predecessors(self, graph):
        return np.array([self.left.short_name])

    def calc_func(self, **kwargs):
        return self.left.map_schedule(**kwargs, **self.func_kwargs)
    
class Schedule(pd.DataFrame, NodeMixin):
    """
    Container and handler class for a list of invoice or purchase orders.
    """
    _metadata = ['_name', '_short_name', '_graph', '_hide', '_inputs', '_sched_maker']

    def __init__(self, 
        *args, 
        name:str=None, 
        short_name:str=None, 
        graph:nx.DiGraph=None, 
        hide:bool=True,
        sched_maker:typ.Callable=None,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._graph = graph
        self._name = name
        self._short_name = short_name if short_name else (self._shorten(name) if name else None)
        self._hide = hide
        self._sched_maker = sched_maker

        self._inputs = pd.Series([], dtype=object)

    @property
    def _constructor(self):
        return Schedule

    @property
    def name(self):
        return self._name

    @property
    def sched_maker(self):
        return self._sched_maker

    @property
    def inputs(self):
        return self._inputs

    def find_predecessors(self):
        return self.inputs.index.values

    def set_maker(self, maker):
        self._sched_maker = maker

    def set_graph(self, graph):
        self._graph = graph
        for k, v in self.inputs.iteritems():
            self.inputs[k].set_graph(graph)

    def add_input(self, name:str, value:typ.Union[Input, ScheduleType]):
        self._inputs.loc[name] = value

    def add_inputs(self, inputs:dict):
        for k, v in inputs.items():
            self.add_input(k, v)

    def update_input(self, name:str, value:typ.Union[int, float]):
        self.inputs.loc[name].update(value)
        self.update()

    def update_inputs(self, inputs:dict):
        for name, value in inputs.iteritems():
            self.inputs.loc[name].update(value)

        self.update()

    def update(self, updated:ScheduleType):
        for k, v in updated.__dict__.items():
            setattr(self, k, v)

        self._push_updates()

    def map_schedule(self,
        value_column:str=None,
        date_column:str=None, 
        periods:pd.PeriodIndex=None,
        **kwargs
        ):
        if self.AS_METRICFUNC:
            return ScheduleFunction(self, value_column=value_column, date_column=date_column, periods=periods)
        else:
            obj = map_to_periods(self[value_column].values, self[date_column].values, periods)

            kwargs.pop('shared_levels', None)
            obj = MultiLevelAccount(
                obj,
                columns=periods,
                index=pd.MultiIndex.from_frame(self),
                **kwargs
            )
            if obj.has_graph:
                if 'groupby' in obj.graph.graph: # group if graph has groupby kwargs
                    by_kws = obj.graph.graph['groupby']
                    obj = getattr(obj.groupby(by_kws['by']), by_kws['func'])(to_account=True)

                if self.compare_freq(self.graph.graph['periods'].freqstr, periods.freqstr): # resample Schedule if the periods in the graph are larger than the periods provded at instantiation
                    obj = obj.resample(self.graph.graph['periods'].freqstr, 'sum') # these Schedules should only be used in Income Statement items

            return obj
