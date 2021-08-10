#!/usr/bin/env python3
'''
Neuron Binary Classification Forward
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

    def forward_prop(self, X):
        '''
        Defines a single neuron performing binary classification
        '''
        tmp = Neuron.np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + Neuron.np.exp(-tmp))
        return self.__A

    def cost(self, Y, A):
        '''
        Defines a single neuron performing binary classification
        '''
        tmp = Y * Neuron.np.log(A) + (1 - Y) * Neuron.np.log(1.0000001 - A)
        tmp = Neuron.np.sum(tmp)
        return -tmp / A.shape[1]

    def evaluate(self, X, Y):
        '''
        Evaluates the neuron’s predictions
        '''
        self.forward_prop(X)
        pre = Neuron.np.where(self.__A >= 0.5, 1, 0)
        cost = self.cost(Y, self.__A)
        return pre, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        '''
        Calculates one pass of gradient descent on the neuron
        '''
        dz = A - Y
        dw = Neuron.np.matmul(X, dz.T) / A.shape[1]
        db = Neuron.np.sum(dz) / A.shape[1]
        self.__W = self.__W - alpha * dw.T
        self.__b = self.__b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        '''
        Trains the neuron
        '''
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        elif iterations < 0:
            raise ValueError("iterations must be a positive integer")
        elif not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        elif alpha < 0:
            raise ValueError("alpha must be positive")
        else:
            while iterations > 0:
                self.gradient_descent(X, Y, self.forward_prop(X), alpha)
                iterations -= 1
            return self.evaluate(X, Y)

