import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
n = 10000
h = 1 / n


def f(x):
    return np.cos((np.pi * (x ** (1 / m))) / 4) ** k


def tf(x):
    return x ** 2


def P(xq):
    return y[j] + (xq[j] - x[j]) * yR1 + (xq[j] - x[j]) * (xq[j] - x[j + 1]) * yR2


def eliki():
    j = np.arange(-n, n)
    x = j * h
    y = f(x)
    plt.plot(x, f(x))
    plt.show()


eliki()
# e = abs(f(xq) - P(xq))
# e_Max = np.max(e)
# e_Sr_Kv = 1 / (n - 1) * np.sum(e ** 2)
# e_Sr_Kv_Pog = np.sqrt(e_Sr_Kv)
# print("e_Max:", e_Max, '\ne_Sr_Kv:', e_Sr_Kv, '\ne_Sr_Kv_Pog:', e_Sr_Kv_Pog)
