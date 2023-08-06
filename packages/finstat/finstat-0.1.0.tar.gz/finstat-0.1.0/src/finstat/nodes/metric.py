import inspect
import functools as ft
import typing as typ
import numpy as np

import networkx as nx

def mathwrap(func):
    @ft.wraps(func)
    def wrapper(self, item, **kwargs):
        if self.AS_METRICFUNC:
            return MetricFunction(self, func.__name__, item)
        else:
            return func(self, item, **kwargs)
            
    return wrapper
   
def multimathwrap(func):
    @ft.wraps(func)
    def wrapper(self, item=None, shared_levels:typ.Iterable=None, **kwargs):
        if self.AS_METRICFUNC:
            return MetricFunction(self, func.__name__, item)
        else:
            return func(self, item, shared_levels=shared_levels, **kwargs)

    return wrapper

def metricize(func):
    @ft.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.AS_METRICFUNC:
            kwargs.pop('shared_levels', None)
            return CustomMetricFunction(self, func.__name__, *args, **kwargs)
        else:
            result = func(self, *args, **kwargs)
            return result

    return wrapper

def register_metric_method(func):
    """
    Registers a custom method to the class of the `left` positioned argument. 
    The `func` is wrapped in `metricize` which allows it to work as a CustomMetricFunction.
    """
    left_arg = inspect.getfullargspec(func).args[0]
    if left_arg in inspect.getfullargspec(func).annotations:
        _class = inspect.getfullargspec(func).annotations[left_arg]
    else:
        raise ValueError('The first argument in `func` must have a type annotation')
    
    setattr(_class, func.__name__, metricize(func))
    print (f'Method {func.__name__} registered to {_class}')

class MetricGraph:
    def __init__(self, mfunc):
        self.mfunc = mfunc
        self.graph = nx.DiGraph()
        self.build_graph(self.mfunc, self.graph)
        self.assign_graph_attributes()

    @property
    def gens(self):
        return self.graph.graph['gens']

    @property
    def first_gen_names(self):
        """Returns `short_name` attribute of each node in the first generation of the graph"""
        return np.array([node.short_name for id_, node in nx.get_node_attributes(self.graph, 'mfunc').items() if id_ in self.gens[0] and hasattr(node, 'short_name')])

    @property
    def terminal_func(self):
        """Returns the MetricFunction of the last generation node"""
        return self.graph.nodes[self.graph.graph['terminal_node']]['mfunc']

    @property
    def mfunc_nodes(self):
        return np.array([isinstance(mfunc, MetricFunction) for mfunc in nx.get_node_attributes(self.graph, 'mfunc').values()])

    @property
    def multi_nodes(self):
        from .accounts import MultiLevelAccount
        return np.array([isinstance(mfunc, MultiLevelAccount) for mfunc in nx.get_node_attributes(self.graph, 'mfunc').values()])

    def build_graph(self, mfunc, graph):
        """
        Recursive method that builds a directed graph of relationships of the nested terms in a
        MetricFunction object. 
        
        The graph is built backwards from the terminal node, which is the MetricFunction passed at __init__.
        Each `left` and `right` term of the MetricFucntion is examined. 
        
        If the term is NOT a MetricFunction, the term is added as a node and an edge is added from the term to
        the original `mfunc`.

        If the term is itself a MetricFunction, it passed to its own `build_graph` call and the process is repeated.

        This builds a directed graph with specific generational characteristics. For a graph with "n" generations:
            + 1st generation: each nodes in this generation are NOT MetricFunction objects
            + 2nd generation: each node in this generation is a MetricFunction, but its terms (`left` and `right`) are not
            + 3rd to n - 1 generations: each node is a MetricFunction and its terms are also MetricFunction objects
            + nth generation: should have only one node, which is the terminal node for the calculation

        This can be seen by calling `nx.topological_generations(graph)`.

        The id of each `mfunc` object is used as the node key, as this is a reliable and unique reference to the original function.

        Parameters
        -----------
        mfunc: MetricFunction
        graph: networkx.DiGraph
        """
        graph.add_node(id(mfunc), mfunc=mfunc, left=mfunc.left, right=mfunc.right)
        
        if mfunc.left_is_func:
            self.build_graph(mfunc.left, graph)
        else:
            graph.add_node(id(mfunc.left), mfunc=mfunc.left, left=None, right=None)

        if mfunc.right_is_func:
            self.build_graph(mfunc.right, graph)
        else:
            graph.add_node(id(mfunc.right), mfunc=mfunc.right, left=None, right=None)
            
        graph.add_edge(id(mfunc.left), id(mfunc))
        graph.add_edge(id(mfunc.right), id(mfunc))

    def assign_graph_attributes(self):
        """
        The MetricGraph is structured with non-MetricFunction objects in the first generation of
        the graph. Calculations are cascaded from the first generation down through the penultimate
        generation. 
        
        Generations are found using `topological_generations` and assigned as a graph attribute.

        The last generation should contian only one node, referred to as the "terminal_node". 
        """
        gens = list(nx.topological_generations(self.graph))
        self.graph.graph['gens'] = gens
        self.graph.graph['terminal_node'] = gens[-1][0]
        assert len(gens[-1]) == 1, gens[-1]

    def cascade_node_funcs(self, graph, calculate:bool=True, **shared):
        """
        Looping algorithmn that cascades calculation of the nested MetricFunction objects in the graph. Each node in the
        graph is assigned "mfunc", "left", and "right" keys. 
        
        If both "left" and "right" are NOT MetricFunction objects, the `calc_func` method can be called on the "mfunc" object. 
        If any of "left" and "right" are MetricFunction objects, then calc_func cannot be called. Therefore, we must find the
        generation of nodes for which all "left" and "right" keys are NOT MetricFunction objects.

        This is the 2nd generation. 
        
        Process
        --------
        + Starting with the 2nd generation, at each node, find the immediate successor nodes using `out_edges`.
        + Check which term the predecessor node is assigned to in the successor node. 
        + Re-assign that term by calling `calc_func` on the predecessor node. The term MetricFunction object has now been 
        replaced with a calcuable type.
        + After the term has been reassigned, check if both terms of the successor node are now calcuable types. If they are, 
        we reassign the "mfunc" key with a new MetricFunction using the calcuable types.
        + now each node in the successor generation has calcuable terms.
        + Repeat the above process for each generation up to the second last generation

        + The last generation should contain only the terminal node. Upon completion, the terminal node should have
        calcuable terms.

        + The terminal node is assigned as an attribute of the graph

        Parameters
        -----------
        graph: networkx.DiGraph

        """
        for gen in self.gens:
            for node in gen:
                node_func = graph.nodes[node]['mfunc']
                for edge in graph.out_edges(node):
                    out_node = edge[1]
                    out_dict = graph.nodes[out_node]
                    if id(out_dict['left']) == node:
                        graph.nodes[out_node]['left'] = node_func.calc_func(**shared) if isinstance(node_func, MetricFunction) and calculate else node_func # For first gen nodes, "mfunc" is not a MetricFunction so just needs to be passed up
                    if id(out_dict['right']) == node:
                        graph.nodes[out_node]['right'] = node_func.calc_func(**shared) if isinstance(node_func, MetricFunction) and calculate else node_func

                    if not calculate or (not isinstance(graph.nodes[out_node]['left'], MetricFunction) and not isinstance(graph.nodes[out_node]['right'], MetricFunction)):
                        graph.nodes[out_node]['mfunc'] = out_dict['mfunc']._constructor(graph.nodes[out_node]['left'], out_dict['mfunc'].funcstr, *out_dict['mfunc'].func_args, right=graph.nodes[out_node]['right'], **out_dict['mfunc'].func_kwargs)
                        
    def __call__(self, **kwargs):
        shared = {k: v for k,v in kwargs.items() if k == 'shared_levels'}
        self.cascade_node_funcs(self.graph, **shared)
        return self.terminal_func.calc_func(**kwargs)

class MetricFunction:
    """
    Handler class to implement metric calculations.

    When called, it simply implements the `func` passed at instantiation with keywords passed to the result.

    Parameters:
        left: Account or MetricFunction
            the left term in standard python arithmetic
        right: Account or MetricFunction
            the right term in standard python arithmetic
        funcname: str
            any of the standard python operations that have been overriden in MathMixin. The value must be
            from the `__name__` attribute of the method.
    """
    @property
    def _constructor(self):
        return MetricFunction

    def __init__(self, left, funcstr:str, right, **func_kwargs):
        self.left = left
        self.funcstr = funcstr
        self.right = right
        self._func_args = []  # standard math functions do not get arguments, but custom functions may
        self._func_kwargs = func_kwargs

    def __repr__(self):
        return f'MetricFunction: {self.funcstr}'

    def __add__(self, item):
        return MetricFunction(self, '__add__', item)

    def __radd__(self, item):
        return MetricFunction(self, '__radd__', item)

    def __sub__(self, item):
        return MetricFunction(self, '__sub__', item)

    def __rsub__(self, item):
        return MetricFunction(self, '__rsub__', item)

    def __mul__(self, item):
        return MetricFunction(self, '__mul__', item)

    def __rmul__(self, item):
        return MetricFunction(self, '__rmul__', item)

    def __truediv__(self, item):
        return MetricFunction(self, '__truediv__', item)

    def __rtruediv__(self, item):
        return MetricFunction(self, '__rtruediv__', item)

    @property
    def func_args(self):
        return self._func_args

    @property
    def func_kwargs(self):
        return self._func_kwargs

    def set_func_kwargs(self, **kwargs):
        self._func_kwargs = kwargs

    def set_func_args(self, *args):
        self._func_args = args

    @property
    def left_is_func(self) -> bool:
        return isinstance(self.left, MetricFunction)

    @property
    def right_is_func(self) -> bool:
        return isinstance(self.right, MetricFunction)

    @property
    def lfunc(self):
        """
        The mathematical operation is always called on the `left` object
        """
        return getattr(self.left, self.funcstr)

    @property
    def rfunc(self):
        """
        The mathematical operation is always called on the `left` object
        """
        funcname = '__' + self.funcstr.lstrip('__r') if '__r' in self.funcstr else '__r' + self.funcstr.lstrip('__')
        return getattr(self.right, funcname)

    @property
    def left_not_implemented(self):
        return isinstance(self.left, (str, int, float))

    def calc_func(self, **kwargs):
        if not self.left_not_implemented:
            value = self.lfunc(item=self.right, **self.func_kwargs, **kwargs)
        if self.left_not_implemented or value is NotImplemented:
            value = self.rfunc(item=self.left, **self.func_kwargs, **kwargs)
        return value

    @property
    def calculate(self):
        self.mgraph = MetricGraph(self)
        return self.mgraph

    def find_predecessors(self, graph):
        return np.intersect1d(np.array(graph.nodes), self.mgraph.first_gen_names)

    def __call__(self, **kwargs):
        """
        Simply implements the `func` method passed and is equivalent to: left.__add__(item, return_func=False)

        Passing `return_func=False` ensures the function is completed normally, thus returning another Account object.
        The Account object is instantiated with whatever attributes are indicated in `kwargs`. This would typically include
        `_short_name`, `_graph`, etc.
        """
        return self.calculate(**kwargs)

class CustomMetricFunction(MetricFunction):
    @property
    def _constructor(self):
        return CustomMetricFunction
    
    def __init__(self, left, funcstr:str, *func_args, right=None, **func_kwargs):
        self.left = left
        self.right = right
        self.funcstr = funcstr
        self._func_args = func_args
        self._func_kwargs = func_kwargs

    def __repr__(self):
        return f'CustomMetricFunction: {self.funcstr}'

    def calc_func(self, **kwargs):
        return self.lfunc(*self._func_args, **self._func_kwargs, **kwargs)
