import numpy as np
from rounding import rounding as rnd        # rounding.py is in the same folder, its pupose is to round according to FPA


# defining the function
def func(x):
    return (x**7 - 42*x**5 + 840*x**3 - 5839*x + 2520)/(2*x**7 - 84*x**5 + 1680*x**3 + 9199)

# defining the RE, Relative Error
def RE_(x1, x0):
    
    return abs((x1 - x0)/x1)

# custom printing function
def printing(n, x0, x1, RE):
    x0 = round(rnd(x0, 7)[-1], 10)
    x1 = round(rnd(x1, 7)[-1], 10)
    # RE = rnd(RE, 7)[-1]        # since the RE gets so small that the round() takes more the starting zeros so we all we left with is some floats
    print(n, ":\t||\t" ,x0,"\t||\t", x1,"\t||\t", RE)



# main function
def fixed_point(x0, criterion):
    interations = 0
    # rnd1 = rnd.rounding()

    # first iteration
    # x1 = rnd(func(x0),7)[-1]
    x1 = func(x0)
    RE = rnd( RE_(x1,x0) ,7)[-1]
    printing(interations, x0, x1, RE)


    # the middle iterations
    # while abs(x1 - x0) > criterion:
    while RE > criterion:
        interations += 1
        x0 = x1
        # x1 = rnd(func(x0),7)[-1]
        x1 = func(x0)
        RE = rnd( RE_(x1,x0) ,7)[-1]

        printing(interations, x0, x1, RE)
        
    
    # the last iteration
    # x0 = x1
    # x1 = rnd(func(x0),7)[-1]
    # RE = rnd( RE_(x1,x0) ,7)[-1]
    # printing(round(x0,10), x1, RE)
    # interations += 1

    return rnd(x1,7)[-1], f"iterarions: {interations+1}"


print(fixed_point(0.5051, 1e-7))


