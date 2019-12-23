import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
n = 50
a = 1
b = 2
h = 1 / n


def f(x):
    return np.tan((np.pi * (x ** (1 / m))) / 4) ** k


def tf(x):
    return x ** 2


def P(x):
    return y[j] + (x - x[j]) * yR1 + (x - x[j]) * (x - x[j + 1]) * yR2


j = np.arange(0, n + 1)
x = j * h
y = np.zeros(n + 1)
y[j] = tf(x)
j = np.arange(0, n)
yR1 = (y[j + 1] - y[j]) / h
j = np.arange(0, n - 1)
yR2 = (y[j + 2] - 2 * y[j + 1] + y[j]) / (2 * h ** 2)
yR1 = yR1[:n - 1]
y = y[:n - 1]
xq = (j + 1 / 2) * h
px = P(xq)
print(px)
e = np.linalg.norm(f(xq) - px)
e_Max = np.max(e)
e_Sr_Kv = 1 / (n - 1) * np.sum(e ** 2)
e_Sr_Kv_Pog = np.sqrt(e_Sr_Kv)
print("e_Max:", e_Max, '\ne_Sr_Kv:', e_Sr_Kv, '\ne_Sr_Kv_Pog:', e_Sr_Kv_Pog)

# plt.plot(f(x), x)
# plt.show()
