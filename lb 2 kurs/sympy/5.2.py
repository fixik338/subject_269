from sympy import *

x = Symbol('x')
a = ((x ** 2) + 2 * x + 1) / ((2 + x) * (3 + x))


def first(a):
    return expand(a)


def second(a):
    return factor(a)


def third(a):
    return apart(a)


def fourth(a):
    akr = cancel(a)
    return


print(first(a), '\n', second(a), '\n', third(a), '\n', fourth(a))
