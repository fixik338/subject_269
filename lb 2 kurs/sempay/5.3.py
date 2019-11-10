from sympy import *

class A:
    def __init__(self, c):
        self.c = c

    def preob(self, a, b, x, y):
        C0 = self.c.subs(a, x)
        C = C0.subs(b, x + y ** 2)
        return C

a, b, x, y = symbols('a b x y')
C = (a**b)-(a**2)+2*a*(b**2)-3*a*b+1
C1 = A(C)
print("Ответ: ", C1.preob(a, b, x, y))