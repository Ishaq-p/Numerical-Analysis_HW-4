from rounding import rounding as rnd
# import numpy as np


def f(x):
    return 2*x**3 - 9*x**2 + 2*x + 10

def RE_(x1, x0):
    return abs((x1 - x0)/x1)

def printing(n, a_n, b_n, p_n, y_a, y_p, RE):
    a_n = round(rnd(a_n, 7)[-1], 10)
    b_n = round(rnd(b_n, 7)[-1], 10)
    p_n = round(rnd(p_n, 7)[-1], 10)
    y_a = rnd(y_a, 7)[-1]
    y_p = rnd(y_p, 7)[-1]
    # RE = rnd(RE, 9)[-1]        
    print(n, ":\t||\t" ,a_n,"\t||\t", b_n,"\t||\t", p_n,"\t||\t", y_a, "\t||\t", y_p, "\t||\t", RE)

def xINT(a, b):
    return a - (f(a) * (a - b) / (f(a) - f(b)))


def regular_falsi(a, b, epsilon):
    RE = 1
    n = 1
    while RE >= epsilon:
        p = xINT(a, b)
        RE = RE_(p, a)
        printing(n, a, b, p, f(a), f(p), RE)
        Hot_Cold = f(a) * f(p)
        if Hot_Cold < 0:
            b = p
        else:
            a = p
        n += 1

    print('Approximation of the root is', round(rnd(p, 7)[-1], 10))

regular_falsi( 1, 2, 1e-7)