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
    return x**2
j = np.arange(-250, 250, n)
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
plt.plot(tf(x), x)
plt.plot(l, x7)
plt.show()