from sympy import *

class A:
    def __init__(self, c):
        self.c = c

    def preob(self, x, y):
        C0 = self.c.subs(y, 3*x-2*b)
        C = C0.subs(x, b + 2)
        return C

b, x, y = symbols('b x y')
C = (x+1+x*y)**2
c1 = A(C)
print("Ответ: ", c1.preob(x, y))