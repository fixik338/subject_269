from sympy import *

a, x = symbols('a x')
C = exp(-a * x) * (1 + 2 * cos(a * x))


def limit5(C):
    Cs = C.series(x, 0, 5)
    Cd = diff(Cs, a)
    return Cs, Cd


print(limit5(C))
