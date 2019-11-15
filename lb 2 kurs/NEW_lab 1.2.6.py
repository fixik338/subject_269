import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

eps = 10 ** -6
m = 1
k = 1
j = 1
a = 0
b = 1


def dih(eps, m, k, j, a, b):
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
    return fx, x, n


def sek(eps, m, k, j):
    S = []
    i = 0
    imax = 10
    x0 = 0.2
    x1 = x0 - 90 * eps
    fx0 = (1 - x0) ** (1 / j) - np.tan((np.pi * x0 ** m) / 4) ** k
    while i < imax:
        fx1 = (1 - x1) ** (1 / j) - np.tan((np.pi * x1 ** m) / 4) ** k
        x = x1 - ((x1 - x0) / (fx1 - fx0)) * fx1
        S.append(x)
        eps1 = np.fabs(x - x1)
        if eps1 > eps:
            x0 = x1
            fx0 = fx1
            x1 = x
        i += 1
    fx = (1 - x1) ** (1 / j) - np.tan((np.pi * x1 ** m) / 4) ** k
    plt.show()
    return fx, x1, i


def kas(eps, m, k, j):
    i = 0
    imax = 10
    x0 = 0.2
    fx0 = (1 - x0) ** (1 / j) - np.tan((np.pi * x0 ** m) / 4) ** k
    dfx0 = -np.pi * (np.tan(np.pi * x0 / 4) ** 2 + 1) / 4 - 1

    def f(x0):
        f = (1 - x0) ** (1 / j) - np.tan((np.pi * x0 ** m) / 4) ** k
        return f

    def df(x0):
        df = -np.pi * (np.tan(np.pi * x0 / 4) ** 2 + 1) / 4 - 1
        return df

    x1 = x0 - (f(x0) / df(x0))
    while np.fabs(x1 - x0) > eps or i < imax:
        x1 = x0 - (f(x0) / df(x0))
        x0 = x1
        i += 1
    fx = (1 - x1) ** (1 / j) - np.tan((np.pi * x1 ** m) / 4) ** k
    return fx, x1, i


print("Дихотомия:", dih(eps, m, k, j, a, b), "\nМетод секущих:", sek(eps, m, k, j), "\nМетод касательных:",
      kas(eps, m, k, j))
