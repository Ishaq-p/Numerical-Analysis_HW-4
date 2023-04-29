def f(x):
    return 2*x**3 - 9*x**2 + 2*x + 10

def XINT(u, v):
    return u - f(u) * (u - v) / (f(u) - f(v))

Digits = 7
a = 1.0
b = 2.0
p = a
epsilon = 10**(-4)

n = 1
while abs(f(p)) >= epsilon:
    p = XINT(a, b)
    print(n,"\t||\t", round(a,7),"\t||\t", round(b,7),"\t||\t", round(p,7),"\t||\t", f(a), f(p), f(a) * f(p))
    HotCold = f(a) * f(p)
    if HotCold < 0:
        b = p
    else:
        a = p
    n += 1

print('Approximation of the root is', p)