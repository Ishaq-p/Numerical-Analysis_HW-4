from sympy import *
import mpmath as mp
# import numpy as np

# Define the function
x = symbols('x')
f = x*sin(0.63*x) - 0.32

# Define the function to find the x-intercept of the line
def XINT(u, v):
    return float(u - (f.subs(x, u) * (u - v) / (f.subs(x, u) - f.subs(x, v))))

# Set the precision
mp.dps = 7

# Set the initial values
p0 = 1
p1 = 0.8
epsilon = 1e-6
RE = 1

# Iterate to find the root
n = 2
while RE >= epsilon:
    p = XINT(p0, p1)
    RE = abs((p - p1) / p)
    print(n, round(p0,7), round(p1,7), round(p,7), RE)
    p0 = p1
    p1 = p
    n += 1

# Print the final result
print('Approximation of the root is', p)