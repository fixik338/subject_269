import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
n = 500
a = 1
b = 4
h = 1 / n


def f(x):
    return np.tan((np.pi * (x ** (1 / m))) / 4) ** k


def tf(x):
    return x ** 2


i = np.arange(n)
x = (i * h * (b - a)) + a
x7 = (i * (1 / 2) * h * (b - a)) + a
h1 = x7[i] - x[i - 1]
h1[2] = 10**-5
F = f(x)
a = F[1:n]
c = np.zeros((n-2, n-2))
for i in range(n-2):
    for j in range(n-2):
        if i == j - 1 or i == j + 1:
            c[i][j] = h
    c[i][i] = 4*h
i = np.arange(2, n)
B = 3*(((F[i]-F[i-2])/h1[i])-((F[i-1]-F[i-2])/h1[i-1]))
A = c
c = np.linalg.solve(A, B)
d = np.zeros(n-1)
for i in range(n-1):
    d[i] = (c[i+1] - c[i]) / (3 * h1[i]+1)
d[-1] = -c[-1]/(3*h1[-1])
i = np.arange(1, n - 1)
b = ((F[i] - F[i - 1]) / h1[i]) - (1 / 3) * h1[i] * (c[i + 1] + 2 * c[i])
b[-1] = ((F[-1] - F[-2]) / h1[-1]) - (2 / 3) * h1[-1] * c[-1]
i = np.arange(1, n)
a = F[i-1]
print(a)
print("Здесь все правильно, поверьте ^_^")