from sympy import *


x, y = symbols('x y')
b1 = (2 * x * y + 4 * (x ** 2) - 2 * x * y ** 2) ** 3

print()
def first1(b1):
    return simplify(b1)


def second1(b1):
    b1 = expand(b1)
    return simplify(b1)


def third1(b1):
    b1 = expand(b1)
    b1 = simplify(b1)
    return


def fourth1(b1):
    b1 = expand(b1)
    return collect(b1, x)


# print(first1(b1), '\n', second1(b1), '\n', third1(b1), '\n', fourth1(b1))
