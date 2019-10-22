from sympy import *


x, y = symbols('x y')
b1 = (2 * x * y + 4 * (x ** 2) - 2 * x * y ** 2) ** 3

print()
def first(b1):
    return simplify(b1)


def second(b1):
    b1 = expand(b1)
    return simplify(b1)


def third(b1):
    b1 = expand(b1)
    b1 = simplify(b1)
    return


def fourth(b1):
    b1 = expand(b1)
    return collect(b1, x)


print(first(b1), '\n', second(b1), '\n', third(b1), '\n', fourth(b1))
