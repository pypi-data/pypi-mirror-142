import functools as ft
import warnings
import typing as typ
import numpy as np
import pandas as pd

import networkx as nx

from .nodes.node import NodeMixin
from .nodes.accounts import Account, MultiLevelAccount, Accounts
from .nodes.metric import MetricFunction
from .nodes.input import Input
from .groupers import FinStatResampler, FinStatGroupBy
from .erp.erp import ScheduleMaker, ScheduleType
from .valuation import Valuation

FinancialStatementType = typ.TypeVar('FinancialStatementType', bound='FinancialStatement')

class AddMetric:
    """
    A context manager that allows metrics to be added to a FinancialStatement object using 
    standard python notation.

    Example
    --------
    with istat.add_metric as add_metric:
        add_metric(istat.input1 + istat.input2, name='Input 3', short_name='input3')

    The context manager sets the flag `ADDING_METRIC=True` in the FinancialStatement graph. Each Node object checks this
    flag before executing the magic method (`__add__` in this example). Instead of returning the appropriate Node object,
    the method retuns a MetricFunction, which is executed inside the `add_metric` call. 

    This process allows the resulting value to be added as a Node to the graph with metadata attached and edges back to the
    component terms.

    Parameters
    -----------
    finstat: FinancialStatement
        FinancialStatement object on which with AddMetric object is called via `add_metric` method
    """
    def __init__(self, finstat:FinancialStatementType):
        self._finstat = finstat

    def __enter__(self):
        """
        As we enter the context, we set the ADDING_METRIC flag on the graph. The instantiated object
        is passed, so it can be called directly.
        """
        self._finstat.open_metric_context()
        return self

    def __call__(self, 
        metricfunc:MetricFunction,
        name:str=None,
        short_name:str=None, 
        insert_after:str=None,
        **kwargs
        ) -> None:
        """
        When AddMetric is called directly, the args and kwargs are simply assigned to object. The metric is
        then added to the FinancialStatement via `_assign_metric` so that it can be add to the graph.

        Parameters
        -----------
        metricfunc: MetricFunction
            Can be passed as any combination of Node objects using standard pythom mathematical notation.
        name: str
            Name of the node
        short_name: str
            Default None. If not provided, assigned automatically.
        insert_after: str
            Name of existing Node object. Used to organize order of nodes in the FinancialStatement. If provided, the new node
            will be insert after the name of the node provided. If not, the new node is inserted in the last position. Default None.
        """
        self.metricfunc = metricfunc
        self.name = name
        self.insert_after = insert_after

        if short_name is None and name is not None:
            short_name = self._finstat._shorten(name)

        self.short_name = short_name

        self._finstat.close_metric_context() # Flag must be closed for calculation
        metric = self.metricfunc(
            name=self.name, 
            short_name=self.short_name, 
            graph=self._finstat.graph, 
            shared_levels=self._finstat.shared_levels,
            **kwargs
        )

        self._assign_metric(metric, self.metricfunc, self.insert_after, self._finstat.shared_levels)

        self._finstat.open_metric_context() # Open flag again; ALLOWS AddMetric to be called again for another Node

    def _assign_metric(self, metric:Account, metricfunc:MetricFunction, insert_after:str=None, shared_levels:typ.Iterable=[]) -> None:
        """
        Helper method to add metric Node objects to the statement.

        Process
        --------
        1. the metric is assigned to an attribute based on its short name. 
        2. the metric is assigned to a node 
        """
        setattr(self._finstat, metric.short_name, metric)
        
        if isinstance(metric, Input):
            nodetype = 'input'
        else:
            nodetype = 'metric'
        
        self._finstat.add_node(
            metric.short_name,
            obj=metric,
            name=metric.short_name,
            statement=self._finstat.short_name,
            mfunc=metricfunc,
            nodetype=nodetype,
            position=self._finstat.find_node_position(insert_after),
            insert_after=insert_after,
            shared_levels=shared_levels
        )
        self._finstat.graph.add_edges_from([(parent, metric.short_name) for parent in metricfunc.find_predecessors(self._finstat.graph)])
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        The `ADDING_METRIC` flag is closed for the last time.
        """
        self._finstat.close_metric_context()

@staticmethod
def reset(func):
    """
    Resets the `__statement__` attribute after the function call so that calls made directly
    on the FinancialStatement object act normally
    """
    @ft.wraps(func)
    def wrap(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.__statement__ = ''
        return result
    
    return wrap

class FinancialStatement(NodeMixin):
    """
    Main class
    
    Consists of DataFrame front-end, matrix backend?,
    and graph structure to map front-end on to backend,
    graph structure used to facilitate observer pattern
    and automatic updates

    Financial statement as a directed graph
    Each Account / Metric / Ratio is a node
    Account objects never have predecessors
    Metric objects must have predecssors

    Each account is assigned to a 
            self.graph.add_node(account.short_name, obj=account)

    Parameters:
        periods: pd.PeriodIndex
            time-series applied to all the constituent accounts
    """
    _metadata = ['_name', '_short_name', '_graph', '_viewstr', '_shared_levels']
    NODE_TYPES = np.array(['schedule', 'input', 'section', 'account', 'metric'])
    EXCLUDED_NODES = NODE_TYPES[:2]
    ACCOUNT_NODES = NODE_TYPES[2:]
    _ipython_canary_method_should_not_exist_ = None # Need for ipython support of __getattribute__ customization

    def __init__(self, 
        periods:pd.PeriodIndex=None, 
        name:str=None,
        short_name:str=None,
        shared_levels:typ.Iterable[str]=[],
        view:str='visible',
        graph:nx.DiGraph=None,
        ):
        self._graph = nx.DiGraph(OPEN_METRIC_CONTEXT=False, periods=periods, statements={}) if graph is None else graph
        self._name = name
        self._shared_levels = shared_levels
        self._viewstr = view
        self._short_name = self._shorten(name) if short_name is None else short_name

        self.__statements__ = []

    @property
    def _constructor(self):
        return FinancialStatement

    def __getattribute__(self, name:str) -> typ.Any:
        """
        """
        try:
            return object.__getattribute__(self, name)
        except AttributeError as e:
            statements = object.__getattribute__(self, '__statements__')
            if statements:
                for statement in statements:
                    substat = object.__getattribute__(self, statement)
                    try:
                        return object.__getattribute__(substat, name)
                    except AttributeError:
                        pass
            raise e

    @property
    def statements(self):
        return self.graph.graph['statements']

    def add_statement(self, name, short_name:str=None, **kwargs):
        """
        Adds statement meta to the FinancialStatement
        1. Add statement meta to graph
        2. Add statement `short_name` to `__statements__` (need for lookup in `__getattribute__`)
        3. Assign `short_name` as attribute that simply returns the statement object
        """
        self.graph.graph['statements'][short_name] = {'name': name, 'short_name': short_name}
        if short_name not in self.__statements__:
            self.__statements__.append(short_name)

        for kw in ['periods', 'shared_levels']:
            if kw not in kwargs:
                kwargs[kw] = getattr(self, kw)

        stat = FinancialStatement(name=name, short_name=short_name, graph=self.graph, **kwargs)
        setattr(self, short_name, stat)

    #### Visuals ####
    def _repr_html_(self):
        if not self.__statements__:
            return self._frame._repr_html_()
        else:
            pd.DataFrame()
            statstrs = ""
            for i, name in enumerate(self.__statements__):
                statstrs += f"""
                    <tr style="text-align: left;">
                     <td>{i + 1}. {self.statements[name]['short_name']} - {self.statements[name]['name']}
                    </tr>
                """
            if len(self.__statements__) == 0:
                statstrs = '<tr><td>None added</td></tr>'

            return f"""<div>\n
                <table border="1" class="dataframe">\n  
                 <thead>\n    
                  <tr style="text-align: left;">\n      
                    <th>Statements</th>\n    
                   </tr>\n
                 </thead>\n  
                 <tbody>\n
                 {statstrs}
                 </tbody>\n
                </table>\n
               </div>
            """

    @property
    def _frame(self):
        self.__frame__ = self.to_frame()
        return self.__frame__

    def to_frame(self, with_periods:bool=True, strftime:str='%b-%Y', *args, **kwargs) -> pd.DataFrame:
        if 'shared_levels' not in kwargs and self.shared_levels:
            kwargs['shared_levels'] = self.shared_levels

        if self.empty:
            frame = pd.DataFrame([], columns=[f'Empty {self.name}'])
        elif self.view.size == 0:
            frame = pd.DataFrame([], columns=[f'Empty {self.name} View'])
        else:
            frame = self.view.concat(*args, **kwargs)

        if not with_periods and isinstance(frame.columns, pd.PeriodIndex):
            frame.columns = frame.columns.strftime(strftime)

        return frame

    @property
    def view(self):
        """
        Attribute manages the contents of `to_frame` output
        """
        if self._viewstr == 'visible':
            return self.accounts.visible.by_position()
        elif self._viewstr == 'hidden':
            pass
        elif self._viewstr == 'all':
            return self.accounts.by_position()
        else:
            raise ValueError("`style` must be one of 'visible', 'hidden', 'all'")

    def set_view(self, view:str):
        self._viewstr = view

    @property
    def name(self):
        return self._name

    @property
    def _periods(self):
        return self.graph.graph['periods']

    @property
    def periods(self):
        return self._periods

    def update_periods(self, periods:pd.PeriodIndex):
        self.graph.graph['periods'] = periods 

    @property
    def empty(self):
        return not self.accounts.size

    @property
    def shared_levels(self):
        return self._shared_levels

    def update_shared_levels(self, shared_levels:typ.Iterable[str]):
        self._shared_levels = shared_levels

    def open_metric_context(self):
        self.graph.graph['OPEN_METRIC_CONTEXT'] = True

    def close_metric_context(self):
        self.graph.graph['OPEN_METRIC_CONTEXT'] = False

    #### Node Management ####
    @property
    def next_node_position(self):
        if self.node_positions.size == 0:
            return 0
        else:
            return self.node_positions.max() + 1

    @property
    def node_positions(self):
        return np.array(list(nx.get_node_attributes(self.graph, 'position').values()))

    def get_node_position(self, name):
        """
        Returns order attribute of node
        """
        return self.graph.nodes[name]['position']

    def update_node_positions(self, insert_pos:int):
        old_order = self.node_positions
        new_order = np.where(old_order >= insert_pos, old_order + 1, old_order)
        for name, position in zip(list(self.graph.nodes), new_order):
            self.graph.nodes[name]['position'] = position

    def find_node_position(self, insert_after:typ.Union[str, None]):
        if insert_after is None:
            order = self.next_node_position
        else:
            order = self.get_node_position(insert_after) + 1
            self.update_node_positions(order)

        return order

    def add_node(self, node:str, **kwargs):
        """
        Centralizes `add_node` to ensure each node receives the same attributes.
        """
        REQUIRED_ATTRS = ['obj', 'statement', 'mfunc', 'nodetype', 'name', 'position', 'insert_after']
        not_provided = [attr for attr in REQUIRED_ATTRS if attr not in kwargs]
        assert not not_provided, f'`add_node` has missing parameters: {", ".join(not_provided)}'
        self.graph.add_node(node, **kwargs)

    @staticmethod
    def subgraph(graph, attr, value):
        # returns a subgraph containing only the nodes with attribute value specified
        def f(n):
            if hasattr(value, '__len__') and not isinstance(value, str):
                return graph.nodes(data=attr)[n] in value
            else:
                return graph.nodes(data=attr)[n] == value
        return nx.subgraph_view(graph, filter_node=f)

    @property
    def statgraph(self):
        """Returns node specific to the current statement"""
        return self.subgraph(self.graph, 'statement', self.short_name)

    def filter_nodes_by_attribute(self, attr, value, fullgraph:bool=False, **kwargs):
        graph = self.graph if fullgraph else (self.statgraph if not self.__statements__ else self.graph)
        return self.subgraph(graph, attr, value).nodes(**kwargs)

    #### Main Node 
    @property
    def inputs(self):
        inputs = self.filter_nodes_by_attribute('nodetype', 'input', data='obj')
        return pd.Series(dict(inputs), name='Inputs', dtype=object)

    @property
    def schedules(self):
        schedules = dict(self.filter_nodes_by_attribute('nodetype', 'schedule', data='obj')).values()
        return Accounts(*schedules)

    @property
    def accounts(self) -> Accounts:
        """
        Returns all Account objects that are nodes on the FinancialStatement graph. This includes accounts nested
        in the subgraphs of sections.
        """
        accounts = dict(self.filter_nodes_by_attribute('nodetype', self.ACCOUNT_NODES, data='obj')).values()
        return Accounts(*accounts)
        
    def add_input(self, name:typ.Union[str, Input], value:typ.Union[np.number, int, float]=None, insert_after:str=None):
        input = name if isinstance(name, Input) else Input(value=value, name=name, graph=self.graph)

        setattr(self, input.name, input)
        self.add_node(
            input.name,
            obj=input,
            name=input.name,
            statement=self.short_name,
            nodetype='input',
            mfunc=None,
            position=self.find_node_position(insert_after),
            insert_after=insert_after,
        )

    def add_inputs(self, inputs:typ.Iterable):
        if isinstance(inputs, dict):
            for k,v in inputs.items():
                self.add_input(k, v)
        else:
            for input in inputs:
                if isinstance(input, Input):
                    self.add_input(input)
                else:
                    self.add_input(**input)

    def add_schedule(self, schedule:typ.Union[ScheduleType, typ.Callable], insert_after:str=None):
        if callable(schedule):
            schedule = ScheduleMaker(schedule, self).make()
            mfunc = schedule._sched_maker.make
        else:
            mfunc = None

        schedule.set_graph(self.graph)

        setattr(self, schedule.short_name, schedule)
        self.add_node(
            schedule.short_name, 
            obj=schedule,
            name=schedule.short_name, 
            statement=self.short_name,
            nodetype='schedule', 
            mfunc=mfunc,
            position=self.find_node_position(insert_after),
            insert_after=insert_after,
            shared_levels=[],
        )
        self.graph.add_edges_from([(parent, schedule.short_name) for parent in schedule.find_predecessors()])

    def add_account(
        self, 
        data:typ.Iterable,
        name:str='',
        short_name:str='',
        periods:pd.PeriodIndex=None,
        index:typ.Iterable=None,
        insert_after:str=None,
        **kwargs
        ) -> None:
        """
        An account is a pandas object with no predecessors. When an account is added,
        1. it is added as an attribute according to its `short_name`
        2. the Graph is passed into the Account
        3. the Account is added as a node in the graph

        Parameters:
            data: any python iterables
            name: str
            short_name: str
                used to assign attribute name to the FinancialStatement
            periods: pd.PeriodIndex
                can be passed directly to override class-level attribute
        """
        if isinstance(data, (Account, MultiLevelAccount)):
            account = data
            account._graph = self.graph
        else:
            if isinstance(data, pd.Series):
                if not name:
                    name = data.name
                data, index = data.values, data.index

            if not name:
                raise ValueError('You must provide `name` attribute if `data` is not type pd.Series')

            data = np.array(data) # To check dimensionality
            periods = periods if periods is not None else self.periods
            if data.ndim == 2:
                account = MultiLevelAccount(
                    data, 
                    index=index,
                    columns=periods,
                    name=name, 
                    short_name=short_name, 
                    graph=self.graph,
                    **kwargs
                )
            else:
                account = Account(
                    data, 
                    index=periods, 
                    name=name, 
                    short_name=short_name, 
                    graph=self.graph,
                    **kwargs
                )

        setattr(self, account.short_name, account)
        self.add_node(
            account.short_name, 
            obj=account, 
            name=account.short_name,
            mfunc=None,
            statement=self.short_name,
            nodetype='account', 
            position=self.find_node_position(insert_after),
            insert_after=insert_after,
        )
       
    def add_accounts(self, data:typ.Iterable) -> None:
        """
        Add multiple accounts with one call.

        If data is a pd.DataFrame, can iterate over the pd.Series rows. Otherwise iterate over the collections.
        """
        if isinstance(data, pd.DataFrame):
            for i, row in data.iterrows():
                self.add_account(data=row)
        else:
            for account in data:
                if isinstance(account, (Account, MultiLevelAccount)):
                    self.add_account(account)                
                else:
                    self.add_account(**account)

    @property
    def add_metric(self):
        return AddMetric(self)

    ##### Implementations of common pandas methods #####
    @property
    def iloc(self):
        return self._frame.iloc

    @property
    def loc(self):
        return self._frame.loc

    @property
    def index(self):
        return self._frame.index

    @property
    def shape(self):
        return self._frame.shape

    def resample(self, *args, **kwargs):
        return FinStatResampler(self, *args, **kwargs)

    def groupby(self, *args, **kwargs):
        return FinStatGroupBy(self, *args, **kwargs)

    def reorder_levels(self, *args, **kwargs):
        warnings.warn('`reorder_levels` currently returns a `MultiLevelAccount` object, NOT a FinancialStatement')
        return self._frame.reorder_levels(*args, **kwargs).sort_index()

    def droplevel(self, *args, **kwargs):
        warnings.warn('`accounts_only` currently returns a `MultiLevelAccount` object, NOT a FinancialStatement')
        return self._frame.droplevel(*args, **kwargs)

    def to_csv(self, *args, **kwargs):
        self._frame.to_csv(*args, **kwargs)

    def valuation(self, *args, **kwargs):
        return Valuation(*args, **kwargs)
