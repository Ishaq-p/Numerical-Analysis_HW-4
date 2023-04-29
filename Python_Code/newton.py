# import math
import numpy as np
from rounding import rounding as rnd
Digits = 7


# custom printing function
def printing(n, x0, x1, RE):
    x0 = round(rnd(x0, 7)[-1], 10)
    x1 = round(rnd(x1, 7)[-1], 10)
    # RE = rnd(RE, 9)[-1]        
    print(n, ":\t||\t" ,x0,"\t||\t", x1,"\t||\t", RE)

# defining the RE, Relative Error
def RE_(x1, x0):
    return abs((x1 - x0)/x1)

# the original function
def f(x):
    # return 10*x**3 - 2*x**2 + 3*x - 1   # function whose root we're approximating
    return x + np.e**(2.499*x)
    
# the iteration function, g(x) = x - f(x) / f'(x)
def g(x):
    # return x - ( f(x) / (30*x**2 - 4*x + 3) )  # the iteration function, g(x) = x - f(x) / f'(x)
    return x - ( f(x) / (1 + 2.499*np.e**(2.499*x)) )


# main function
def fixed_point(p0, epsilon):
    RE = 1
    n = 1
    while RE >= epsilon:
        p = g(p0)
        RE = RE_(round(rnd(p, 7)[-1], 10), round(rnd(p0, 7)[-1], 10))
        printing(n, p0, p, RE)
        p0 = p
        n += 1

    print('Approximation of the fixed point is', rnd(p, 7)[-1])


fixed_point(-1, 1e-6)

