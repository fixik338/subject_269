import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
n = 2
a = 1
b = 2
h = 1 / n


def f(x):
    return np.tan((np.pi * (x ** (1 / m))) / 4) ** k


def tf(x):
    return x ** 2


j = np.arange(-100, 100, n)
x = j * h
x7 = (j + (1 / 2)) * h
print(x, '\n', x7)
r = f(x)
l = np.ones(len(x))
for j in range(len(x)):
    for i in range(len(x)):
        if j != i:
            l[j] *= (x7[j] - x7[i]) / (x[j] - x[i])
l = l * r
# plt.plot(x, f(x))
# plt.plot(x7, l, "-")
# plt.grid(True)
# plt.show()
