import numpy as np
import matplotlib.pyplot as plt
from math import *


def f(x):
    return x * np.cosh(x)


def df(x):
    return np.cosh(x) + x * np.sinh(x)


def ddf(x):
    return 2 * np.sinh(x) + x * np.cosh(x)


def f_test(x):
    return np.exp(x)


h = 0.2
x = np.arange(0, 1, h)
dy = (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)
ddy = (-f(x - 2 * h) + 16 * f(x - h) - 30 * f(x) + 16 * f(x + h) - f(x + 2 * h)) / (12 * h ** 2)
d1r = abs(df(x) - dy)
d2r = abs(ddf(x) - ddy)
d1rk = np.sqrt(1/(len(x)+1) * np.sum((df(x)-dy)**2))
d2rk = np.sqrt(1/(len(x)+1) * np.sum((ddf(x)-ddy)**2))
print('', 'Значение 1-ой производной функции в узлах =', df(x),
      '\n', 'Приближенное значение 1-ой производной функции в узлах =', dy,
      '\n', 'Значение 2-ой производной функции в узлах =', ddf(x),
      '\n', 'Приближенное значение 2-ой производной функции в узлах =', ddy,
      '\n', 'Погрешность 1-ой производной =', d1r,
      '\n', 'Погрешность 2-ой производной =', d2r,
      '\n', 'Максимальная погрешность 1-ой производной =', np.max(d1r),
      '\n', 'Максимальная погрешность 2-ой производной =', np.max(d2r),
      '\n', 'Среднеквадратичная погрешность 1-ой производной =', d1rk,
      '\n', 'Среднеквадратичная погрешность 2-ой производной =', d2rk)
