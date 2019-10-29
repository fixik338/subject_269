from sympy import *

# x = Symbol('x')
# a = ((x ** 2) + 2 * x + 1) / ((2 + x) * (3 + x))


def first2(a):
    return expand(a)


def second2(a):
    return factor(a)


def third2(a):
    return apart(a)


def fourth2(a):
    akr = cancel(a)
    return


# print(first2(a), '\n', second2(a), '\n', third2(a), '\n', fourth2(a))
