import numpy as np
from .chebyshev import chebyshev_roots
import torch

from .location import Location
from .label_tensor import LabelTensor


class Span(Location):
    def __init__(self, span_dict):

        self.fixed_ = {}
        self.range_ = {}

        for k, v in span_dict.items():
            if isinstance(v, (int, float)):
                self.fixed_[k] = v
            elif isinstance(v, (list, tuple)) and len(v) == 2:
                self.range_[k] = v
            else:
                raise TypeError

    def sample(self, n, mode='random'):

        bounds = np.array(list(self.range_.values()))
        if mode == 'random':
            pts = np.random.uniform(size=(n, bounds.shape[0]))
        elif mode == 'chebyshev':
            pts = np.array([
                chebyshev_roots(n) * .5 + .5
                for _ in range(bounds.shape[0])])
            grids = np.meshgrid(*pts)
            pts = np.hstack([grid.reshape(-1, 1) for grid in grids])
        elif mode == 'grid':
            pts = np.array([
                np.linspace(0, 1, n)
                for _ in range(bounds.shape[0])])
            grids = np.meshgrid(*pts)
            pts = np.hstack([grid.reshape(-1, 1) for grid in grids])
        elif mode == 'lh' or mode == 'latin':
            from scipy.stats import qmc
            sampler = qmc.LatinHypercube(d=bounds.shape[0])
            pts = sampler.random(n)

        # Scale pts
        pts *= bounds[:, 1] - bounds[:, 0]
        pts += bounds[:, 0]
        pts = torch.from_numpy(pts)
        pts_range_ = LabelTensor(pts, list(self.range_.keys()))

        fixed = torch.Tensor(list(self.fixed_.values()))
        pts_fixed_ = torch.ones(pts_range_.tensor.shape[0], len(self.fixed_)) * fixed
        pts_fixed_ = LabelTensor(pts_fixed_, list(self.fixed_.keys()))

        if self.fixed_:
            return LabelTensor.hstack([pts_range_, pts_fixed_])
        else:
            return pts_range_

    def meshgrid(self, n):
        pts = np.array([
            np.linspace(0, 1, n)
            for _ in range(self.bound.shape[0])])

        pts *= self.bound[:, 1] - self.bound[:, 0]
        pts += self.bound[:, 0]

        return np.meshgrid(*pts)
