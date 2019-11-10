from sympy import *


class A:
    def __init__(self, b):
        self.b = b

    def first(self):
        return simplify(self.b)

    def second(self):
        b1 = expand(self.b)
        return simplify(b1)

    def third(self):
        b1 = expand(self.b)/8
        b2 = 8*b1
        return b2

    def fourth(self, x):
        b1 = expand(self.b)
        return collect(b1, x)


x, y = symbols('x y')

u = (2 * x * y + 4 * (x ** 2) - 2 * x * y ** 2) ** 3
u1 = A(u)
print("1-e: ", u1.first(), '\n2-e:', u1.second(), '\n3-e:', u1.third(), '\n4-e:', u1.fourth(x))
