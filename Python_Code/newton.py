# import math
from rounding import rounding as rnd
Digits = 7


# custom printing function
def printing(n, x0, x1, RE):
    x0 = round(rnd(x0, 7)[-1], 10)
    x1 = round(rnd(x1, 7)[-1], 10)
    RE = rnd(RE, 9)[-1]        
    print(n, ":\t||\t" ,x0,"\t||\t", x1,"\t||\t", RE)

# defining the RE, Relative Error
def RE_(x1, x0):
    return abs((x1 - x0)/x1)

# the original function
def f(x):
    return x ** 3 - x ** 2 + 7*x - 6   # function whose root we're approximating
    
# the iteration function, g(x) = x - f(x) / f'(x)
def g(x):
    return x - ( f(x) / (3*x ** 2 - 2* x  + 7) )  # the iteration function, g(x) = x - f(x) / f'(x)


# main function
def fixed_point(p0, epsilon):
    RE = 1
    n = 1
    while RE >= epsilon:
        p = g(p0)
        RE = RE_(p, p0)
        printing(n, p0, p, RE)
        p0 = p
        n += 1

    print('Approximation of the fixed point is', rnd(p, 7)[-1])


fixed_point(1.632653, 1e-7)

