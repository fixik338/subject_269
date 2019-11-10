import numpy as np
import matplotlib.pyplot as plt

eps = 10 ** -6
m = 1
k = 1
j = 1
a = 0
b = 1
x0 = 0.2


def dih(eps, m, k, j, a, b, x0):
    n = 0
    fa = (1 - a) ** (1 / j) - np.tan((np.pi * a ** m) / 4) ** k
    while np.fabs(a - b) > eps:
        c = (a + b) / 2
        fc = (1 - c) ** (1 / j) - np.tan((np.pi * c ** m) / 4) ** k
        n += 1
        if fa * fc > 0:
            a = c
            fa = fc
        else:
            b = c
    x = (a + b) / 2
    fx = (1 - x) ** (1 / j) - np.tan((np.pi * x ** m) / 4) ** k
    print("Знач. функции: ", fx, "\nОТВЕТ:", x, "\nИтераций:", n)


def sek(eps, m, k, j, x0):
    i = 0
    imax = 10
    x1 = x0 - 90*eps
    fx0 = (1 - x0) ** (1 / j) - np.tan((np.pi * x0 ** m) / 4) ** k
    while i < imax:
        fx1 = (1 - x1) ** (1 / j) - np.tan((np.pi * x1 ** m) / 4) ** k
        x = x1 - ((x1 - x0)/(fx1 - fx0))*fx1
        eps1 = np.fabs(x - x1)
        if eps1 > eps:
            x0 = x1
            fx0 = fx1
            x1 = x
        i += 1
    fx = (1 - x) ** (1 / j) - np.tan((np.pi * x ** m) / 4) ** k
    # plt.show()
    print("Знач. функции: ", fx, "\nОТВЕТ:", x, "\nИтераций:", i)


dih(eps, m, k, j, a, b, x0)
sek(eps, m, k, j, x0)