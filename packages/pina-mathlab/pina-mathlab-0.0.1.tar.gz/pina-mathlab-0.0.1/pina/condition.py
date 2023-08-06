""" """
import torch

from .location import Location

class Condition:
    def __init__(self, *args, **kwargs):

        if len(args) == 2 and not kwargs:

            if (isinstance(args[0], torch.Tensor) and
                    isinstance(args[1], torch.Tensor)):
                self.input_points = args[0]
                self.output_points = args[1]
            elif isinstance(args[0], Location) and callable(args[1]):
                self.location = args[0]
                self.function = args[1]
            else:
                raise ValueError

        elif not args and len(kwargs) == 2:

            if 'input_points' in kwargs and 'output_points' in kwargs:
                self.input_points = kwargs['input_points']
                self.output_points = kwargs['output_points']
            elif 'location' in kwargs and 'function' in kwargs:
                self.location = kwargs['location']
                self.function = kwargs['function']
            else:
                raise ValueError
        else:
            raise ValueError
