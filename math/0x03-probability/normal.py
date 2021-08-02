#!/usr/bin/env python3
'''
Normal Distribution
'''


class Normal:
    def __init__(self, data=None, mean=0., stddev=1.):
        '''
        Constructor
        '''
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        elif not isinstance(data, list):
            raise TypeError("data must be a list")
        elif len(data) < 2:
            raise ValueError("data must contain multiple values")
        else:
            self.mean = sum(data) / len(data)
            self.stddev = ((sum([(data[j] - self.mean) ** 2
                                 for j in range(len(data))])) /
                           len(data)) ** 0.5

    def z_score(self, x):
        '''
        Standard Score
        '''
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        '''
        X Score
        '''
        return z * self.stddev + self.mean

    def pdf(self, x):
        '''
        Probaility Density Function
        '''
        e = 2.7182818285
        pi = 3.1415926536
        a = 1 / (self.stddev * ((2 * pi) ** (1 / 2)))
        return a * (e ** (-(1 / 2) * ((x - self.mean) / self.stddev) ** 2))

    def cdf(self, x):
        '''
        Cumulative Distribution Function
        '''
        e = 2.7182818285
        pi = 3.1415926536
        tmp = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        tmp2 = 2 / (pi ** (1 / 2))
        a1 = (tmp ** 3) / 3
        a2 = (tmp ** 5) /10
        a3 = (tmp ** 7) / 42
        a4 = (tmp ** 9) / 216
        erf = tmp2 * (tmp - a1 + a2 - a3 + a4)
        return (1 / 2) * (1 + erf)
