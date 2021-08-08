#!/usr/bin/env python3
'''
Neuron Binary Classification
'''


class Neuron:
    '''
    Neuron Class
    '''

    import numpy as np

    def __init__(self, nx):
        '''
        Init of the class
        '''
        if not isinstance(nx, int):
            raise TypeError("nx must be a integer")
        elif nx < 1:
            raise ValueError("nx must be positive")
        else:
            self.nx = nx
            self.__W = Neuron.np.random.normal(size=(1, nx))
            self.__b = 0
            self.__A = 0

    @property
    def W(self):
        '''
        Getter function for W
        '''
        return self.__W

    @property
    def A(self):
        '''
        Getter function for A
        '''
        return self.__A

    @property
    def b(self):
        '''
        Getter function for b
        '''
        return self.__b
