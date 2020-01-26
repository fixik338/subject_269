import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
n = 25
a = 1
b = 2
h = 1 / n


def f(x):
    return np.tan((np.pi * (x ** (1 / m))) / 4) ** k


def tf(x):
    return x**2


def P(xq, x, yR1, yR2):
    return y[j] + (xq[j] - x[j]) * yR1 + (xq[j] - x[j]) * (xq[j] - x[j + 1]) * yR2


j = np.arange(-25, n)
x = j * h
x7 = (j+(1/2))*h
# print(x)
r = tf(x)
l = np.ones(len(x))
for j in range(len(x)):
    for i in range(len(x)):
        if j != i:
            l[j] *= (x7[j]-x[i])/(x[j]-x[i])
l = l*r
print(l)
plt.plot(tf(x), x)
plt.plot(l, x7)
plt.show()