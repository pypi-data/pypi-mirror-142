import torch
import torch.nn as nn
from pydoc import locate
from phobos.config import get_map, save_map

model_map = get_map('model')

def save_model_map(dest):
    """Saves model map in location ``dest`` as a json file

    This file can later be used to lookup phobos supported models

    Parameters
    ----------
    dest : `str <https://docs.python.org/3/library/stdtypes.html#str>`_ 
        destination path

    Examples
    --------
    Save model map in location ``/tmp``

    >>> save_model_map('/tmp')
    
    """
    save_map(map=model_map, name='model', dest=dest)

class ModelWrapper(nn.Module):
    """Wrapper class for phobos supported models

    Parameters
    ----------
    model : `torch.nn.module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_
        model to train or validate.
    iheads : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        list of input head keys
    oheads : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        list of output head keys
    
    Attributes
    ----------
    model : `torch.nn.module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_
        model to train or validate.
    iheads : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        list of input head keys
    oheads : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        list of output head keys
    """
    def __init__(self, model, iheads, oheads):
        super(ModelWrapper, self).__init__()

        self.model = model
        self.iheads = iheads
        self.oheads = oheads

    def forward(self, imap):
        itensors = [imap[head] for head in self.iheads]

        otensors = self.model(*itensors)

        if isinstance(otensors, torch.Tensor):
            omap = { self.oheads[0]: otensors }
        else:
            omap = { self.oheads[idx]: otensors[idx] for idx in range(len(self.oheads)) }

        return omap

def get_model(key, args, iheads, oheads):
    """Creates and returns an ModelWrapper instance created based on model config

    This method is consumed in the model creation pipeline in Grain

    Parameters
    ----------
    key : `str <https://docs.python.org/3/library/stdtypes.html#str>`_ / `torch.optim <https://pytorch.org/docs/stable/optim.html>`_
        type of model instance
    args : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
        dictionary of model parameters.
    iheads : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        list of input head keys
    oheads : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        list of output head keys

    Returns
    -------
    `torch.nn.module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_
        ModelWrapper instance

    Raises
    ------
    Exception
        custom exception generated if either of the following conditions are satisfied
        
        * ``key`` is not supported by ``phobos``
        * ``path`` is not provided as argument for custom model

    Examples
    --------
    Create a phobos supported model instance  

    >>> key = 'resnet18'
    >>> args = { 'pretrained': True }
    >>> iheads, oheads = ['in'],['out']
    >>> 
    >>> model = get_model(key=key, 
    ...                   args=args, 
    ...                   iheads=iheads,
    ...                   oheads=oheads)
    
    for custom models, pass ``path`` to model class as an argument. e.g

    >>> key = 'dummy'
    >>> args = { 
    ...         'nchannels': 4,
    ...         'nclasses': 10,
    ...         'path': 'model.dummy.Dummy'
    ... }
    ...
    >>> iheads, oheads = ['inp1'],['out1']
    >>>
    >>> model = get_model(key=key, 
    ...                   args=args, 
    ...                   iheads=iheads,
    ...                   oheads=oheads)

    this model instance is later consumed by runner for training
    """
    mclass = None

    if 'path' in args:
        mclass = locate(args['path'])
        del args['path']
    elif key in model_map:
        mclass = model_map[key]
    else:
        raise Exception('for phobos supported model, please provide correct key \
                         and for custom model, please provide path as argument') 
    
    minst = mclass(**args)

    return ModelWrapper(minst, iheads, oheads)