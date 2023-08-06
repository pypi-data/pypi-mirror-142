import typing as typ
import numpy as np
import pandas as pd

import networkx as nx

from .node import NodeMixin
from .metric import mathwrap

InputType = typ.TypeVar('InputType', bound='Input')

class Input(NodeMixin):
    """
    Root class for constructing FinancialStatement objects. Extends pandas Series object.
    """
    @property
    def _constructor(self):
        return Input

    def __init__(self, 
        value:typ.Union[int, float], 
        name:str=None, 
        short_name:str=None, 
        graph:nx.DiGraph=None,
        **kwargs):
        
        self._value = value
        self._name = name
        if short_name is None and name and len(name.split()) == 1:
            self._short_name = name
        else:
            self._short_name = short_name if short_name else (self._shorten(name) if name else None)
        self._graph = graph

    def __repr__(self):
        return f'Input: {self._value.__repr__()}'

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, item):
        if isinstance(item, Input):
            result = self._value == item._value
        else:
            result = self._value == item
        
        return result

    @mathwrap
    def __add__(self, item, **kwargs):
        result = self._value + item._value if isinstance(item, Input) else self._value + item
        return self.singlemath(result, **kwargs)

    @mathwrap
    def __radd__(self, *args, **kwargs):
        return self.__add__(*args, **kwargs)
        
    @mathwrap
    def __sub__(self, item, **kwargs):
        result = self._value - item._value if isinstance(item, Input) else self._value - item
        return self.singlemath(result, **kwargs)

    @mathwrap
    def __rsub__(self, item, **kwargs):
        result = item._value - self._value if isinstance(item, Input) else item - self._value
        return self.singlemath(result, **kwargs)

    @mathwrap
    def __mul__(self, item, **kwargs):
        result = self._value * item._value if isinstance(item, Input) else self._value * item
        return self.singlemath(result, **kwargs)

    @mathwrap
    def __rmul__(self, *args, **kwargs):
        return self.__mul__(*args, **kwargs)

    @mathwrap
    def __truediv__(self, item, **kwargs):
        result = self._value / item._value if isinstance(item, Input) else self._value / item
        return self.singlemath(result, **kwargs)

    @mathwrap
    def __rtruediv__(self, item, **kwargs):
        result = item._value / self._value if isinstance(item, Input) else item / self._value
        return self.singlemath(result, **kwargs)

    def singlemath(self, result, **kwargs):
        from .accounts.account import Account, MultiLevelAccount
        kwargs.pop('shared_levels', []) # Shared levels not required for Account objects

        if result is NotImplemented:
            return result
        elif isinstance(result, (Account, MultiLevelAccount)):
            return result._constructor(result.values, index=result.index, **kwargs)
        else:
            return self._constructor(result, **kwargs)

    @property
    def values(self):
        """
        Property maintains consistency with Account objects, where `values` attribute returns an np.ndarray
        """
        return self._value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def update(self, value):
        """
        Assigns new values to object and cascades updates
        to any successor nodes.

        Data to update successors is calculated using the Metric keywords stored
        in each successor node.
        """
        self._value = value._value if isinstance(value, Input) else value
        self._push_updates()
