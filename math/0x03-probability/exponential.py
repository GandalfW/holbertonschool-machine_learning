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

    def pdf(self, x):
        '''
        Probability density function
        '''
        e = 2.7182818285
        if x < 0:
            return 0
        else:
            return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        '''
        Cumulative Distribution Function
        '''
        e = 2.7182818285
        if x < 0:
            return 0
        else:
            return 1-(e ** -self.lambtha * x)
