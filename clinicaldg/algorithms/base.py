import abc
import numpy as np
import torch

from clinicaldg.lib.hparams_registry import HparamSpec, HparamMixin


class Algorithm(torch.nn.Module, HparamMixin):
    """
    A subclass of Algorithm implements a domain generalization algorithm.
    Subclasses should implement the following:
    - update()
    - predict()
    """
    HPARAM_SPEC = [
        HparamSpec('lr', 1e-3, lambda r: 10**r.uniform(-7.0, -1)),
        HparamSpec('weight_decay', 0., lambda r: r.choice([0.] + (10.**np.arange(-7, -0)).tolist()))
    ]
    
    def __init__(self, experiment, num_domains, hparams):
        super(Algorithm, self).__init__()
        self.hparams = hparams

    @abc.abstractmethod
    def update(self, minibatches, device):
        """
        Perform one update step, given a list of (x, y) tuples for all
        environments.
        """
        pass

    @abc.abstractmethod
    def predict(self, x):
        pass