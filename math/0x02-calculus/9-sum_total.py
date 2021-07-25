#!/usr/bin/env python3

def summation_i_squared(n):
    if(not isinstance(n,int)):
        result=None
    elif n==1:
        result=1
    else:
        result=(pow(n,2)+summation_i_squared(n-1))
    return result
