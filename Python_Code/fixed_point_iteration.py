import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA
from sig_digits import sig_digits as sd      # sig_digits.py is in the same folder, its pupose is to find the number of significant digits


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# defining the function
def func(x):
    return (x**3)/fact(3) - (x**5)/fact(5) + (x**7)/fact(7) + 1/2

# defining the RE, Relative Error
def RE_(x1, x0):
    return abs(abs(x1 - x0)/x1)

# custom printing function
def printing(n, x0, x1, RE):
    x0 = round(rnd(x0, 9)[-1], 12)
    x1 = round(rnd(x1, 9)[-1], 12)
    # RE = rnd(RE, 7)[-1]        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(n, ":\t||\t" ,x0,"\t||\t", x1,"\t||\t", RE)



# main function
def fixed_point(x0, criterion):
    interations = 0
    # rnd1 = rnd.rounding()

    # first iteration
    # x1 = rnd(func(x0),7)[-1]
    x1 = func(x0)
    RE = RE_(round(rnd(x1, 9)[-1], 12),round(rnd(x0, 9)[-1], 12))
    printing(interations, x0, x1, RE)


    # the middle iterations
    # while abs(x1 - x0) > criterion:
    while RE > criterion:
        interations += 1
        x0 = x1
        # x1 = rnd(func(x0),7)[-1]
        x1 = func(x0)
        RE = RE_(round(rnd(x1, 9)[-1], 12), round(rnd(x0, 9)[-1], 12))

        printing(interations, x0, x1, RE)
        
    
    # the last iteration
    # x0 = x1
    # x1 = rnd(func(x0),7)[-1]
    # RE = rnd( RE_(x1,x0) ,7)[-1]
    # printing(round(x0,10), x1, RE)
    # interations += 1
    y_ = 6*x1
    pi = np.pi
    RE1 = RE_(pi, y_)

    return rnd(x1,9)[-1], f"steps={interations+1}, y*={rnd(y_, 9)[-1]}, RE={RE1}, SD={sd(RE1)[2]}"


print(fixed_point(0.5226, 1e-7))


