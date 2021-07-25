#!/usr/bin/env python3
"""
Calculates polynomial integral
"""


def poly_integral(poly, c=0):

    poly.insert(0, c)
    i = 0
    for n in poly:
        if i != 0:
            poly[i] = n/i
        i = i+1
    return poly
