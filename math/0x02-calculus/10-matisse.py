
#!/usr/bin/env python3
"""
Juego de polinomios con numpy
"""
import numpy as np

def poly_derivate(poly):
    poly.reverse()
    p=np.poly1d(poly)
    return(np.polyder(p).c)
