#!/usr/bin/env python3
'''
Poisson Probability Distribution Class
'''


class Poisson:
    '''
    Poisson Distribution
    '''
    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        '''
        Constructor
        '''
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif (len(data) < 2):
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)
