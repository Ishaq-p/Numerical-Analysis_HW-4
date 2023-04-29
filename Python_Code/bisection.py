import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA


# defining the function
def f_(x):
    # return (3.64 * x * (1 - x**2 + x)*np.log(x)) - x**2 +1
    return 9*x**3 - 14*x**2 - 12*x + 7

# defining the p_(a,b) , the midpoint of a and b
def p_(a,b):
    return (a+b)/2

# defining the sign of f(a)*f(p), in order to specify whihc side to give the p
def sign_(a,p):
    if f_(a)*f_(p) > 0:
        return True,'+'
    elif f_(a)*f_(p)<0:
        return False, '-'

# defining the RE, Relative Error
def RE_(p1, p0):
    return abs((p1 - p0)/p1)

# custom printing function
def printing(a, p, b, sign, RE):
    a = rnd(round(a, 10), 7)[-1]
    b = rnd(round(b, 10), 7)[-1]
    p = rnd(round(p, 10), 7)[-1]
    # RE = round(RE, 10)        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(a,"\t||\t", p,"\t||\t", b,"\t||\t",sign,"\t||\t", RE)



# main function
def bisect(f, a, b, p0, tol=1e-3):
    """Find root of f(x) = 0 on interval [a,b] to within tolerance tol."""
    if f(a)*f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    while RE_(b, a) > tol:
        p1 = p_(a,b)
        sign = sign_(a,p1)
        RE = RE_(p1,p0)

        printing(a, p1, b, sign[1], RE)

        if sign[0]:
            a = p1
        else:
            b = p1
        p0 = p1

    # p1 = rnd(p_(a,b), fpa)[-1]
    # sign = sign_(a,p1)
    # RE = rnd(RE_(p1,p0), fpa)[-1]
    # printing(a, p1, b, sign[1], RE)



print(bisect(f_, a=0, b=1, p0=0))


