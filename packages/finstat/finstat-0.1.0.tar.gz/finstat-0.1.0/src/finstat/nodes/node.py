import numpy as np
import pandas as pd

MATH_METHODS = ['__add__', '__sub__', '__mul__', '__truediv__', '__radd__', '__rsub__', '__rmul__', '__rtruediv__']
PANDAS_FREQ_OFFSET = [
    'D', 'B', 'C', 'W', 'SM', 'SMS', 'M', 'BM' , 'CBM', 'MS', 'BMS', 'CBMS', 'Q', 'BQ',
    'QS', 'BQS', 'A', 'Y', 'BA', 'BY', 'AS', 'YS', 'BAS', 'BYS'
]
FREQ_MAP = {freqstr: v for freqstr, v in zip(PANDAS_FREQ_OFFSET, np.arange(len(PANDAS_FREQ_OFFSET)))}

class NodeMixin:
    @property
    def _metaparams(self):
        """
        Used to pass metadata as kwargs on _constructor calls.

        Used in _constructor_wrapper
        """
        return {meta.lstrip('_'): getattr(self, meta) for meta in self._metadata}

    @property
    def _metaattrs(self):
        """
        Used to pass metadata as kwargs to `_update_meta` calls
        """
        return {meta: getattr(self, meta) for meta in self._metadata}

    def _update_meta(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self._metadata:
                raise ValueError(f'{k} is not in `_metadata`')
            setattr(self, k, v)

    def set_constructor_kwargs(self, kwargs):
        kwargs.pop('shared_levels', None)
        for k, v in self._metaparams.items():
            if k not in kwargs:
                kwargs[k] = v

        return kwargs

    @property
    def AS_METRICFUNC(self):
        return self.graph is not None and self.graph.graph['OPEN_METRIC_CONTEXT']

    @property
    def short_name(self):
        return self._short_name

    @property
    def graph(self):
        return self._graph

    def set_graph(self, graph):
        self._graph = graph

    @property
    def has_graph(self):
        return self.graph is not None

    @property
    def periods(self):
        return self._periods

    @property
    def hide(self):
        return self._hide

    def set_hide(self, hide:bool):
        self._hide = hide

    @property
    def successors(self):
        if self.graph:
            return list(self.graph.successors(self.short_name))
        else:
            raise ValueError('Account is not connected to a graph')

    @property
    def multi_index(self):
        return self._multi_index

    @property
    def is_multi(self):
        NotImplementedError

    @property
    def is_total(self):
        return hasattr(self, '_is_total') and self._is_total

    @property
    def index_as_frame(self):
        return self.index.to_frame().reset_index(drop=True)

    def compare_freq(self, freq_a:str, freq_b:str):
        freq_a = freq_a.split('-')[0]
        freq_a = ''.join([i for i in freq_a if not i.isdigit()])
        freq_b = freq_b.split('-')[0]
        freq_b = ''.join([i for i in freq_b if not i.isdigit()])
        return FREQ_MAP[freq_a] > FREQ_MAP[freq_b]

    def _shorten(self, name) -> str:
        """"
        Logic for creating shorthand name for an Account object
        
        Examples:
            'Revenue' -> 'revenue'
            'Cost of Goods Sold' -> 'cogs'
            'Amortization' -> 'amort'

        Parameters:
            name: str
        """ 
        if name == '' or name is None:
            return ''
        elif len(name.split(' ')) > 1:
            return ''.join(s[0].lower() for s in name.split(' '))
        elif len(name) > 10:
            return name[:5].lower()
        else:       
            return name.lower()

    def _push_updates(self, **kwargs):
        """
        If the object is a node in a graph, loop through each successor node and
        execute the MetricFunction in the successor node. Successors have a 'function' key by defintion.
        """
        if self.graph:
            for successor in self.successors:
                node_data = self.graph.nodes[successor]
                obj, mfunc, shared_levels = node_data['obj'], node_data['mfunc'], node_data['shared_levels']
                obj.update(mfunc(shared_levels=shared_levels, **obj._metaparams))

    def to_frame(self):
        return pd.DataFrame(self.values, index=self.index, columns=self.columns)
