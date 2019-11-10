from sympy import *


class A:
    def __init__(self, c):
        self.c = c

    def limit(self, a, x):
        Cs = self.c.series(x, 0, 5)
        Cd = diff(Cs, a)
        return Cs, Cd


a, x = symbols('a x')
C = exp(-a * x) * (1 + 2 * cos(a * x))
c1 = A(C)
print(c1.limit(a, x))
