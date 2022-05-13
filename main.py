import numpy as np
from sympy import *
from sympy.plotting import plot
from sympy.abc import x
init_printing()

np.exp(1)

e = np.exp(1)
f = e**x
def maxminf(f):
    """ Calcula los máximos y mínimos de una función f(x) """
    df = diff(f, x) # 1era. derivada
    d2f = diff(f, x, 2) # 2da. derivada
    pcs = solve(Eq(df,0)) # puntos críticos
    for p in pcs:
        if d2f.subs(x,p)>0: 
            tipo="Min"
        elif d2f.subs(x,p)<0: 
            tipo="Max"
        else: 
            tipo="Indefinido"
        print("x = %f (%s)"%(p,tipo))
maxminf(e**x)

