import typing as typ
import pandas as pd

import networkx as nx
from finstat.erp.erp import ScheduleFunction

from finstat.nodes.accounts import Accounts, Account, MultiLevelAccount

class Grouper:
    def __init__(self, stat:'FinancialStatement'):
        self.nodes = stat.graph.nodes
        self.grouped = stat._constructor(
            name=stat.name, 
            short_name=stat.short_name,
            graph=stat.graph.copy()
        )

    @property
    def _orig_inputs(self):
        return list(dict(self.grouped.filter_nodes_by_attribute('nodetype', 'input', fullgraph=True, data='obj')).values())
        
    @property
    def _orig_schedules(self):
        return self.grouped.filter_nodes_by_attribute('nodetype', 'schedule', fullgraph=True, data='obj')
        
    @property
    def _orig_accounts(self):
        return Accounts(*dict(self.grouped.filter_nodes_by_attribute('nodetype', 'account', fullgraph=True, data='obj')).values())

    @property
    def _orig_metrics(self):
        return self.grouped.filter_nodes_by_attribute('nodetype', 'metric', fullgraph=True, data=True)
    
    @property
    def grouper_kwargs(self):
        return NotImplementedError

    def _add_schedules(self):
        for schedname, schedule in self._orig_schedules: # need to access schedules that might be in the parent Financial Statement
            arg = schedule if not hasattr(schedule.sched_maker, 'schedfunc') else schedule.sched_maker.schedfunc
            self.grouped.add_schedule(arg)

    def _add_accounts(self, accts):
        for acct in accts:
            acct.set_graph(self.grouped.graph)
            nx.set_node_attributes(self.grouped.graph, {acct.short_name: acct}, name='obj')
            
    def _add_metrics(self):
        """
        Metrics have to be rebuilt top-down, including inside the MetricGraph. Here, the
        actual MetricFunction is pushed down the nodes with parameters updated as necessary to reflect the new state of
        the graph (in the MetricGraph, the result of the MetricFunction calculation is push down the nodes).

        Each loop pertains to a metric node. The goal of each loop is to rebuild the node's MetricFunction, then add it to
        the statement object using the standard `add_metric` approach. Each node's MetricFunction has its own internal graph
        that must be rebuilt with parameters updated as required.
        """
        for nodename, node in self._orig_metrics:
            mg = node['mfunc'].calculate
            for gen in mg.gens[0]: # Rebuilding MetricGraph with terms from the new `grouped` object
                term = mg.graph.nodes[gen]['mfunc'] # first generation of graph is always a static term
                if term is not None:
                    try:
                        term = getattr(self.grouped, term.short_name) # check for updated terms in the grouped first
                    except AttributeError as e:
                        term = self.grouped.graph.nodes[term.short_name]['obj'] # then check for the term in original graph (for inputs and schedules)
                mg.graph.nodes[gen]['mfunc'] = term
 
            mg.cascade_node_funcs(mg.graph, calculate=False) # Removing calculate flag ensures that the MetricFunction object is cascaded and NOT the result
            mf = mg.terminal_func # the terminal_func of the MetricGraph is MetricFunction to be added to the `grouped` object

            self._update_mfunc_args(mf, node) # Some func_args may contain Account objects; these need to be updated to the Grouped version
            self._update_mfunc_kwargs(mf, node) # Some func_kwargs may contain Account objects; these need to be updated to the Grouped version

            params = node['obj']._metaparams.copy()
            params['graph'] = self.grouped.graph
            params['shared_levels'] = self.grouped.shared_levels
            
            metric = mf(**params)
            nx.set_node_attributes(self.grouped.graph, {node['obj'].short_name: mf}, name='mfunc')
            nx.set_node_attributes(self.grouped.graph, {node['obj'].short_name: metric}, name='obj')

    def _update_mfunc_args(self, mf, node):
        new_args = []
        for arg in node['mfunc'].func_args:
            if isinstance(arg, (Account, MultiLevelAccount)):
                if arg.short_name in self.grouped.graph.nodes:
                    new_args.append(self.grouped.graph.nodes[arg.short_name]['obj'])
                else:
                    new_args.append(arg)
            else:
                new_args.append(arg)
        
        mf.set_func_args(*new_args)

    def _update_mfunc_kwargs(self, mf, node):
        new_kwargs = {}
        for k, v in node['mfunc'].func_kwargs.items():
            if isinstance(v, (Account, MultiLevelAccount)):
                if v.short_name in self.grouped.graph.nodes:
                    new_kwargs[k] = self.grouped.graph.nodes[v.short_name]['obj']
                else:
                    new_kwargs[k] = v
            else:
                new_kwargs[k] = v
        
        mf.set_func_kwargs(**new_kwargs)

    def _assign_obj_attrs(self):
        """
        Make attribute call available, same with original object
        """
        for name, obj in self.grouped.graph.nodes(data='obj'):
            setattr(self.grouped, name, obj)

    def _call(self):
        self.grouped.add_inputs(self._orig_inputs)
        self._add_schedules()
        self._add_accounts()
        self._add_metrics()
        self._assign_obj_attrs()

        return self.grouped

    def _assign_func(self, funcstr):
        self.funcstr = funcstr
        if 'groupby' in self.grouped.graph.graph:
            self.grouped.graph.graph['groupby']['func'] = self.funcstr # assign the appropriate funcstr to the graph, these params are availbe to any custom MetricFunction that might access it.

    def sum(self):
        self._assign_func('sum')
        return self._call()

    def last(self):
        self._assign_func('last')
        return self._call()

class FinStatGroupBy(Grouper):
    def __init__(self, stat:'FinancialStatement', by:str):
        self.by = by
        super().__init__(stat)
        self.grouped.update_shared_levels(self._update_shared_levels())
        self.grouped.graph.graph['groupby'] = {}
        self.grouped.graph.graph['groupby']['by'] = by

    def _update_shared_levels(self):
        if self.by == 'Account':
            sl = None
        elif len(self.by) == 1:
            sl = [self.by]
        else:
            sl = self.by

        return sl

    def _add_accounts(self):
        accts = self._orig_accounts.groupby(self.by, self.funcstr, to_account=True)
        return super()._add_accounts(accts)

    def _update_shared_level_attrs(self):
        """
        Make attribute call available, same with original object
        """
        sl = self._update_shared_levels()
        nx.set_node_attributes(self.grouped.graph, sl, name='shared_levels')

    def _call(self):
        self.grouped = super()._call()
        self._update_shared_level_attrs()
        return self.grouped

class FinStatResampler(Grouper):
    def __init__(self, stat:'FinancialStatement', freq:str='A-DEC'):
        self.freqstr = freq
        super().__init__(stat)
        self.grouped.update_periods(stat.periods.asfreq(freq).unique())
        self.grouped.update_shared_levels(stat.shared_levels)

        if 'groupby' in stat.graph.graph:
            self.grouped.graph.graph['groupby'] = stat.graph.graph['groupby'] # period resample retains groupby keywords
    
    @property
    def resampled(self):
        return self.grouped

    @property
    def grouper_kwargs(self):
        return {}

    def _add_accounts(self):
        accts = self._orig_accounts.resample(self.freqstr, self.funcstr)
        return super()._add_accounts(accts)
