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
