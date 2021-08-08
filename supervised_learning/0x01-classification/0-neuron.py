#!/usr/bin/env python3

class Neuron:
    '''
    Class Neuron
    '''
    import numpy as np

    def __init__(self, nx):
        '''
        Class Constructor
        '''

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        else:
            self.nx = nx
            self.W = Neuron.np.random.normal(size=(1, nx))
            self.b = 0
            self.A = 0