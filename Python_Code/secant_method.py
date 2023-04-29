from rounding import rounding as rnd
import numpy as np

def f(x):
    return x*np.sin(0.86*x) - 0.43

def RE_(x1, x0):
    return abs((x1 - x0)/x1)

def printing(n, x0, x1, x2, RE):
    x0 = round(rnd(x0, 7)[-1], 10)
    x1 = round(rnd(x1, 7)[-1], 10)
    x2 = round(rnd(x2, 7)[-1], 10)
    # RE = rnd(RE, 9)[-1]        
    print(n, ":\t||\t" ,x0,"\t||\t", x1,"\t||\t", x2,"\t||\t", RE)


def secant(x0, x1, epsilon):
    RE = 1
    n = 1
    while RE >= epsilon:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        RE = RE_(round(rnd(x2, 7)[-1], 10), round(rnd(x1, 7)[-1], 10))
        printing(n, x0, x1, x2, RE)
        x0 = x1
        x1 = x2
        n += 1

    print('Approximation of the root is', round(rnd(x2, 7)[-1], 10))

secant( 1, 0.8, 1e-6)