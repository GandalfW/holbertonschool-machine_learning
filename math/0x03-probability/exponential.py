#!/usr/bin/env python3
'''
Exponential Class
'''


class Exponential:
    '''
    Exponential Distribution
    '''
    def __init__(self, data=None, lambtha=1.):
        '''
        Constructor
        '''
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be positive value")
            else:
                self.lambtha = float(lambtha)
        elif not isinstance(data, list):
            raise TypeError("data must be a list")
        elif len(data) < 2:
            raise ValueError("data must contain multiple values")
        else:
            self.lambtha = 1 / (sum(data) / len(data))
