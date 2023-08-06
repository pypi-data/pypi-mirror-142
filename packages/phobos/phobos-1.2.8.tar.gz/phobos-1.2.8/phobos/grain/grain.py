from inspect import getmodule

from phobos import __version__ as version
from phobos.io import InputCollection, OutputCollection
from phobos.model import get_model
from phobos.runner import Runner

from pydoc import locate

from yacs.config import CfgNode as CN
from yacs import config
from polyaxon.tracking import Run

import logging
import os, re
import collections
import yaml
import copy
import torch
import torch.nn as nn

config._VALID_TYPES = config._VALID_TYPES.union({Run, torch.device})

_VALID_TYPES = config._VALID_TYPES

class Grain(CN):
    """A class derived from class CfgNode from yacs to be used for:

    - validating config yaml properties
    
    - creating a python yacs object from yaml config file

    - loading arguments for models and logging model inputs
    
    - creating input and output collections based on:
        
        - yaml properties 
    
        - combine map (optional)

    The object formed thus is a nested YACS object wherein YAML keys are converted to multilevel keys/attributes.

    Parameters
    ----------
    polyaxon_exp : `polyaxon.tracking.Run <https://polyaxon.com/docs/experimentation/tracking/client/>`_
        polyaxon experiment
    *args : `list <https://docs.python.org/3/tutorial/introduction.html#lists>`_
        a non keyworded arguments' list.
    **kwargs : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
        a keyworded arguments' list.
    
    Attributes
    ----------
    polyaxon_exp : `polyaxon.tracking.Run <https://polyaxon.com/docs/experimentation/tracking/client/>`_
        polyaxon experiment
    
    Examples
    --------
    1. Parsing dummy metadata YAML through a Grain instance
    
    >>> args = Grain(yaml='/tmp/metadata.yaml')
    >>> args.sensor
    'sentinel2'

    2. Create input and output collection instances, and loaded model based on YAML properties

    >>> grain_exp = Grain()
    >>> args = grain_exp.parse_args_from_yaml('examples/training/mnist_single_mode_multi_head/metadata.yaml')
    >>> 
    >>> inputs, outputs, model = grain_exp.get_inputs_outputs_model()
    >>> len(outputs.heads)
    2
    >>> type(model)
    <class 'phobos.model.model.ModelWrapper'>
    >>> type(model.model)
    <class models.model.Dummy>

    3. Create a map of loss combination methods

    >>> finloss = lambda map: map['1']
    >>> getloss = lambda map: sum(map.values())/len(map)
    >>> 
    >>> combine = {
    ...     'all': finloss,
    ...     'heads': {
    ...         '1': getloss,
    ...         '2': getloss
    ...     }
    ... }

    use combine map and YAML properties for creation of collection instances

    >>> grain_exp = Grain()
    >>> args = grain_exp.parse_args_from_yaml('examples/training/mnist_single_multihead/metadata_sat4.yaml')
    >>> 
    >>> inputs, outputs = grain_exp.get_inputs_outputs(combine) 

    These collection instances and model are consumed later by dataloader and runner

    """

    def __init__(self, yaml, polyaxon_exp = None, *args, **kwargs):
        super(Grain, self).__init__(*args, **kwargs)
        self.version = version
        self.polyaxon_exp = polyaxon_exp

        self.parse_args_from_yaml(yaml)
    
    def parse_args_from_yaml(self, yaml_file):
        """Populates and returns a grain instance using arguments from YAML config file

        Parameters
        ----------
        yaml_file : `str <https://docs.python.org/3/library/stdtypes.html#str>`_ 
            path to YAML config file

        Returns
        -------
        `phobos.grain.Grain <https://github.com/granularai/phobos/blob/develop/phobos/grain/grain.py>`_
            grain instance

        """
        with open(yaml_file, 'r') as fp:
            meta = dict(yaml.safe_load(fp.read()))
            meta = expand(meta, meta)['project']
            meta = Grain._create_config_tree_from_dict(meta, key_list=[])
            super(Grain, self).__init__(init_dict = meta)
            if self.polyaxon_exp:
                map = flatten(self, sep='-')
                self.polyaxon_exp.log_inputs(**map)
        
        self.device = torch.device("cpu", 0)
        if torch.cuda.is_available() and self.run.num_gpus > 0:
            self.device = torch.device("cuda", 0)

        if Runner.local_testing():
            self.run.distributed = False
        elif self.run.distributed:
            Runner.distributed()
    
    def get_inputs_outputs_model(self, combine_meta=None, load=None):
        """Performs the following:
        
        * Generates and returns input and output collection objects, as well as model instance
        * Generates and loads a wrapper instance containing model 

        based on YAML properties, a custom pretrained weight loader and a map of loss combination methods

        Parameters
        ----------
        combine_meta : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_, optional
            map of loss combination methods, by default None
        load: `func <https://docs.python.org/3/tutorial/classes.html#method-objects>`_        
            custom method to load pretrained layers in model, by default None

        Returns
        -------
        inputs : `phobos.io.InputCollection <https://github.com/granularai/phobos/blob/develop/phobos/io/input.py>`_
            instance containing collection of input objects
        outputs : `phobos.io.OutputCollection <https://github.com/granularai/phobos/blob/develop/phobos/io/output.py>`_
            instance containing collection of output objects
        model : `torch.nn.module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_
            wrapper instance containing model loaded based on YAML configs 
        """
        inputs = InputCollection(ymeta=self.input)
        outputs = OutputCollection(
                                ymeta=self.output,
                                cmeta=combine_meta, 
                                device=self.device,
                                )
        
        model = self.create_and_load_model(load)

        return inputs, outputs, model

    def create_and_load_model(self, load=None):
        """Log and instantiate a model with keyword arguments

        Parameters
        ----------
        model_cls : `torch.nn.module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_
            A pytorch model class to instantiate.
        **kwargs : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
            all model positional arguments

        Returns
        -------
        `object <https://docs.python.org/3/reference/datamodel.html#objects-values-and-types>`_
            pytorch model object created from keyword arguments.

        """
        logging.debug("Enter create_and_load_model routine")
        
        meta = self.model 

        iheads = list(self.input.heads.keys())
        oheads = list(self.output.heads.keys())

        model = get_model(
                    key=meta['name'], 
                    args=meta['args'], 
                    iheads=iheads, 
                    oheads=oheads
                    )

        if self.polyaxon_exp:
            self._log_model(model, args=meta['args'])
                
        model = model.to(self.device)
        if meta.distributed:
            model = nn.parallel.DistributedDataParallel(model, find_unused_parameters=False)
        elif meta.num_gpus > 1:
            model = nn.DataParallel(model, device_ids=list(range(meta.num_gpus)))

        weights = None
        if meta.pretrained_checkpoint:
            weights = torch.load(meta.pretrained_checkpoint)
        elif meta.resume_checkpoint:
            weights = torch.load(meta.resume_checkpoint)

        if weights:
            if load:
                load(model, weights)
            else:
                model.load_state_dict(weights)
             
        logging.debug("Exit create_and_load_model routine")
        
        return model

    def _log_model(self, model, args):
        """Log model inputs

        Parameters
        ----------
        model_cls : `torch.nn.module <https://pytorch.org/docs/stable/generated/torch.nn.Module.html>`_
            A pytorch model class.
        **kwargs : `dict <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
            all model positional arguments

        """
        logging.debug("Enter _log_model routine")
        model_cls = model.__class__
        model_module = getmodule(model_cls).__name__
        model_path = os.path.relpath(getmodule(model_cls).__file__)
        model_name = model_cls.__name__

        self.polyaxon_exp.log_inputs(model_path=model_path,
                                     model_name=model_name,
                                     model_module=model_module,
                                     model_args=args)
        logging.debug("Exit _log_model routine")   

    @classmethod
    def _create_config_tree_from_dict(cls, dic, key_list):
        """
        Create a configuration tree using the given dict.
        Any dict-like objects inside dict will be treated as a new CfgNode.
        Args:
            dic (dict):
            key_list (list[str]): a list of names which index this CfgNode from the root.
                Currently only used for logging purposes.
        """
        dic = copy.deepcopy(dic)
        for k, v in dic.items():
            if isinstance(v, dict):
                # Convert dict to CfgNode
                dic[k] = CN(v, key_list=key_list + [k])
            else:
                # Check for valid leaf type or nested CfgNode
                _assert_with_logging(
                    _valid_type(v, allow_cfg_node=False),
                    "Key {} with value {} is not a valid type; valid types: {}".format(
                        ".".join(key_list + [str(k)]), type(v), _VALID_TYPES
                    ),
                )
        return dic

def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, str(v)))
    return dict(items)

def _assert_with_logging(cond, msg):
    if not cond:
        logging.debug(msg)
    assert cond, msg

def _valid_type(value, allow_cfg_node=False):
    return (type(value) in _VALID_TYPES) or (
        allow_cfg_node and isinstance(value, CN)
    )

def replace(map, rkey):
    ref = map

    keys = rkey.split('.')
    for key in keys:
        if type(ref) == dict:
            ref = ref[key]
        elif type(ref) == list:
            ref = ref[int(key)]
        
    return ref

def expand(block, meta):
    if isinstance(block, dict):
        for key in block:
            block[key] = expand(block[key], meta)
    elif isinstance(block, list):
        for idx in range(len(block)):
            block[idx] = expand(block[idx], meta)
    else:
        if type(block) == str:
            mlist = re.findall(r'\$\{.*?\}', block)
            mkeys = [m[2:-1] for m in mlist]
            for i in range(len(mkeys)):
                if not block.replace(mlist[i], ''):
                    block = replace(meta, mkeys[i])
                else:
                    kref = replace(meta, mkeys[i])
                    block = block.replace(mlist[i], str(kref))
        
    return block
