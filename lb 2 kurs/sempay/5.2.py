from sympy import *

class A:
    def __init__(self, a):
        self.a = a

    def first(self):
        return expand(self.a)

    def second(self):
        return factor(self.a)

    def third(self):
        return apart(self.a)

    def fourth(self):
        akr = cancel(self.a)
        return akr


x = Symbol('x')
a = ((x ** 2) + 2 * x + 1) / ((2 + x) * (3 + x))
a1 = A(a)
print("1-e: ", a1.first(), '\n2-e:', a1.second(), '\n3-e:', a1.third(), '\n4-e:', a1.fourth())