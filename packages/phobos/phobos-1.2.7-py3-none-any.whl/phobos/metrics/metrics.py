import numpy as np
import torch, inspect, logging

import torch.nn as nn
import torch.distributed as dist
from torch.distributed import ReduceOp

from pydoc import locate
from phobos.config import get_map, save_map

from copy import deepcopy

metrics_map = get_map('metric')

def save_metrics_map(dest):
    """Saves metrics map in location ``dest`` as a json file

    This file can later be used to lookup phobos supported metrics  

    Parameters
    ----------
    dest : `str <https://docs.python.org/3/library/stdtypes.html#str>`_ 
        destination path

    Examples
    --------
    Save metrics map in location ``/tmp``

    >>> save_metrics_map('/tmp')
    
    """
    save_map(map=metrics_map, name='metric', dest=dest)

class MetricCollection(nn.ModuleDict):
    """Class representing a collection of metrics

    Parameters
    ----------
    metlist : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        list of metrics in collection
    logits : `boolean <https://docs.python.org/3/library/functions.html#bool>`_, optional
        flag representing type of input expected by MetricCollection instance, by default ``False``
        
        * ``True``  : logits based inputs
        * ``False`` : non logits based inputs

    Attributes
    ----------
    logits : `boolean <https://docs.python.org/3/library/functions.html#bool>`_, optional
        flag representing type of input expected by MetricCollection instance, by default ``False``
    
        * ``True``  : logits based inputs
        * ``False`` : non logits based inputs

    Examples
    --------
    Given a map of metric configs

    >>> mconfig = {
    ...     'accuracy': None,
    ...     'precision': {
    ...         'num_classes': 3,
    ...         'average': 'macro'
    ...     },
    ...     'recall': {
    ...         'num_classes': 3,
    ...         'average': 'macro'
    ...     }
    ... }

    Create a list of metrics objects

    >>> metlist = []
    >>> for key in mconfig:
    ...     minst = None
    ...     margs = mconfig[key]
    ... 
    ...     if key in metrics_map:
    ...         mclass = metrics_map[key]
    ...         if margs is None:
    ...             minst = mclass()
    ...         else:
    ...             minst = mclass(**margs)
    ... 
    ...     print(minst.num_classes,minst.average)
    ...     metlist.append(minst)

    Use this list to create a MetricCollection instance

    i. expecting non logits based inputs:

    >>> metrics = MetricCollection(metlist)
    >>> metrics
    MetricCollection(
    (accuracy): Accuracy()
    (precision): Precision()
    (recall): Recall()
    )
    >>> metrics.logits
    False

    ii. expecting logits based inputs:

    >>> metrics = MetricCollection(metlist,logits=True)
    >>> metrics
    MetricCollection(
    (accuracy): Accuracy()
    (precision): Precision()
    (recall): Recall()
    )
    >>> metrics.logits
    True

    Compute metrics for

    i. non logit based inputs

    >>> pred = torch.randint(0,3,size=(4,32,32))
    >>> targ = torch.randint(0,3,size=(4,32,32))
    >>> 
    >>> mmap = metrics(pred, targ)
    >>> mmap
    {'accuracy': tensor(0.3420), 'precision': tensor(0.3424), 'recall': tensor(0.3422)}   

    ii. logits based inputs

    >>> metrics = get_metric(mconfig, cconfig,logits=True)
    >>> pred = torch.rand(size=(4,3,32,32))
    >>> targ = torch.randint(0,3,size=(4,32,32))
    >>> 
    >>> mmap = metrics(pred, targ)
    >>> mmap
    {'accuracy': tensor(0.3337), 'precision': tensor(0.3340), 'recall': tensor(0.3338)}
    >>> 

    Combine metrics computations after a cycle

    >>> means = metrics.compute()

    Log compute results and reset metrics states after cycle completion

    >>> metrics.reset()

    """
    def __init__(self, metlist, device, logits=False, multilabel=False):
        super().__init__()
        self.logits = logits
        self.device = device
        self.multilabel = multilabel

        self.add_metrics(metlist)

    def add_metrics(self, metlist):
        """Add metrics instances in metrics list to MetricCollection

        Parameters
        ----------
        metlist : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
            metrics list

        Raises
        ------
        ValueError
            MetricCollection should not have redundant entries
        """
        for metric in metlist:
            mkey = metric.__class__.__name__
            if mkey in self:
                raise ValueError(f'Metric config has two metrics both named {mkey}')
            self[mkey.lower()] = metric 
        
    def forward(self, predicted, target):
        """Performs metrics computation for predicted and ground truth tensors

        Parameters
        ----------
        predicted : `torch.Tensor <https://pytorch.org/docs/stable/tensors.html#torch.Tensor>`_
            predicted tensor
        target : `torch.Tensor <https://pytorch.org/docs/stable/tensors.html#torch.Tensor>`_
            ground truth tensor

        Returns
        -------
        `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
            map containing metric computation results
        """
        fmap = {}

        pr = predicted.detach().squeeze().to(self.device)
        tg = target.detach().squeeze().to(self.device)

        if self.multilabel:
            assert pr.shape == tg.shape
            n = pr.shape[1]
            p = pr.transpose(0, 1).reshape(n, -1).transpose(0, 1).type(torch.float)
            t = tg.transpose(0, 1).reshape(n, -1).transpose(0, 1).type(torch.int)            
        elif not self.logits:
            assert pr.shape == tg.shape
            p = pr.reshape(-1)
            if 'float' in str(p.dtype):
                p = p.round().type(torch.int)
            t = tg.reshape(-1).type(torch.int)
        else:
            assert len(pr.shape) == len(tg.shape)+1
            n = pr.shape[1]
            p = pr.transpose(0, 1).reshape(n, -1).transpose(0, 1).type(torch.float)
            t = tg.reshape(-1).type(torch.int)

        for mkey, metric in self.items():
            if 'classification' in str(metric.__class__):
                fmap[mkey] = metric(p, t)
            else:
                fmap[mkey] = metric(pr, tg)

        return fmap

    def compute(self):
        """Combines metric computation results after a train/val cycle

        Returns
        -------
        `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
            map summarising overall metrics after the cycle
        """
        return {k: m.compute() for k, m in self.items()}

    def reset(self):
        """Resets metric states. 
        
        """
        for _, m in self.items():
            m.reset()

def get_metric(mconfig, cconfig, device, logits=False, multilabel=False):
    """Creates and returns a MetricCollection instance based on metric config and common config maps. 

    This method is consumed in the OutputCollection creation pipeline.

    Parameters
    ----------
    mconfig : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
        moss config map
    cconfig : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
        common config map
    logits : `boolean <https://docs.python.org/3/library/functions.html#bool>`_, optional
        flag representing type of input expected by MetricCollection instance, by default ``False``
        
        * ``True``  : logits based inputs
        
        * ``False`` : non logits based inputs

    multilabel : `boolean <https://docs.python.org/3/library/functions.html#bool>`_, optional
        flag representing whether multilabel input is expected by MetricCollection instance, by default ``False``

    Returns
    -------
    `phobos.metrics.MetricCollection <https://github.com/granularai/phobos/blob/develop/phobos/metrics/metrics.py>`_
        MetricCollection instance

    Examples
    --------
    Create a MetricCollection object from metric and common config maps

    >>> mconfig = {
    ...     'accuracy': None,
    ...     'precision': {
    ...         'num_classes': 3,
    ...         'average': 'macro'
    ...     },
    ...     'recall': {
    ...         'num_classes': 3,
    ...         'average': 'macro'
    ...     }
    ... }
    >>>
    >>> cconfig = {
    ...     'num_classes': 3
    ... }
    >>>
    >>> metrics = get_metric(mconfig, cconfig)
    >>> metrics
    MetricCollection(
    (accuracy): Accuracy()
    (precision): Precision()
    (recall): Recall()
    )
    
    """
    metlist = []
    for mkey in mconfig:
        minst = None

        margs = {} if mconfig[mkey] is None else mconfig[mkey]

        if 'path' in margs:
            mclass = locate(margs['path'])
            del margs['path']
        elif mkey in metrics_map:
            mclass = metrics_map[mkey]
        else:
            raise Exception('for phobos supported metric, please provide correct key \
                             and for custom metric, please provide path as argument')

        argslist = inspect.getfullargspec(mclass.__init__).args
        for ckey in cconfig:
            if ckey in argslist:
                margs[ckey] = cconfig[ckey]

        if not margs:
            minst = mclass()
        else:
            minst = mclass(**margs)
        
        minst.to(device)
        metlist.append(minst)

    return MetricCollection(metlist, device, logits, multilabel)