#!/usr/bin/env python3
import numpy as np

def summation_i_squared(n):
    if(not isinstance(n,int)):
        return None
    else:
        x=range(1,(n+1))
        x=np.power(x,2)
        return sum(x)

n=5
print(summation_i_squared(n))
