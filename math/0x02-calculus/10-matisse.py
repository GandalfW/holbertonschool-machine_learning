#!/usr/bin/env python3
"""
 Deriva de polinomios
"""


def poly_derivative(poly):
    i = 0
    for n in poly:
        poly[i] = i * n
        i = 1 + i
    poly.pop(0)
    return poly
