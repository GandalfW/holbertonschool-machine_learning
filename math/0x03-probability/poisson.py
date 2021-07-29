#!/usr/bin/env python3
'''
Poisson Probability Distribution Class
'''


class Poisson:
    '''
    Poisson Distribution
    '''

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

    def pmf(self, k):
        '''
        Function PMF
        '''

        e = 2.7182818285
        if k > 0:
            if not isinstance(k, int):
                k = int(k)
        else:
            return 0
        tmp = range(0, k+1)
        f = 1
        for i in tmp:
            if i == 0:
                f = f * 1
            else:
                f = f * i
        r = (e**(-self.lambtha))*(self.lambtha**k)
        r = r/f
        return r
