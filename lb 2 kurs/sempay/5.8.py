from sympy import *

class A:
    def __init__(self, L):
        self.L = L

    def lim(self, a, b):
        return limit(self.L, a, b)

x, y = symbols('x y')
L1 = ((x**2) - 4)/(x - 2)
L2 = 1/(x - 5) - 10/((x**2) - 25)
L3 = sin(x)/x
L4 = ((x + 2*y)/x)**x
L5 = (1 + 1/x)**(2*x + 1)
L6 = tan(x)/x

l1 = A(L1)
l2 = A(L2)
l3 = A(L3)
l4 = A(L4)
l5 = A(L5)
l6 = A(L6)
print("1-й предел: ",  l1.lim(x, 2),
      '\n2-й предел:', l2.lim(x, 5),
      '\n3-й предел:', l3.lim(x, 0),
      '\n4-й предел:', l4.lim(x, oo),
      '\n5-й предел:', l5.lim(x, oo),
      '\n6-й предел:', l6.lim(x, 0))
