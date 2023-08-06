from pydoc import locate
from phobos.config import get_map, save_map

import logging

optimizer_map = get_map('optimizer')

def save_optimizer_map(dest):
    """Saves optimizer map in location ``dest`` as a json file

    This file can later be used to lookup phobos supported optimizers  

    Parameters
    ----------
    dest : `str <https://docs.python.org/3/library/stdtypes.html#str>`_ 
        destination path

    Examples
    --------
    Save optimizer map in location ``/tmp``

    >>> save_optimizer_map('/tmp')
    
    """
    save_map(map=optimizer_map, name='optimizer', dest=dest)

def get_optimizer(key, args, model):
    """Creates and returns a optimizer based on optimizer type and arguments. 

    Parameters
    ----------
    key : `str <https://docs.python.org/3/library/stdtypes.html#str>`_
        type of optimizer instance
    args : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
        dictionary of optimizer parameters.
    model : `torch.nn.module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_
        model to train or validate.

    Returns
    -------
    `torch.optim <https://pytorch.org/docs/stable/optim.html>`_
        optimizer instance.

    Examples
    --------
    Create an optimizer instance using a dummy model and SGD parameters

    >>> class Dummy(nn.Module):
    ...     def __init__(self, n_channels, n_classes):
    ...         super(Dummy, self).__init__()
    ...         self.linear = nn.Linear(n_channels, n_classes)
    ...
    ...     def forward(self, x):
    ...         x = self.linear(x).permute(0, 3, 1, 2)
    ...         return x
    >>> model = Dummy(1, 1)
    >>> optim_key = 'sgd'
    >>> optim_args = {'lr': 0.1}
    >>> optimizer = get_optimizer(key=optim_key, args=optim_args, model=model)
    >>> optimizer
    SGD (
    Parameter Group 0
        dampening: 0
        lr: 0.1
        momentum: 0
        nesterov: False
        weight_decay: 0
    )

    This optimizer instance can be passed to runner for training.

    Click `here <phobos.runner.optimizers.map.html>`_ to view details of optimizers supported by phobos currently. 
    """
    logging.debug("Enter get_optimizer routine")
    
    if 'path' in args:
        optimizer = locate(args['path'])
        del args['path']
    elif key in optimizer_map:
        optimizer = optimizer_map[key]
    else:
        raise Exception('for phobos supported optimizer, please provide correct key \
                         and for custom optimizer, please provide path as argument')
    
    args['params'] = model.parameters()
    
    logging.debug("Exit get_optimizer routine")

    return optimizer(**args)
