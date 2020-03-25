import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
e = 10
n = 50
h = 1 / n


def f(x):
    return np.cos(x) ** 3


j = np.arange(1, n)
x = j * h
yj = f(x)
B = np.zeros(4)
A = np.zeros((4, 4))
for k in range(4):
    B[k] = np.sum(yj * x ** k)
    for j in range(4):
        A[k][j] = np.sum(x ** (k + j))
print(A, '\n', B)
c = np.linalg.solve(A, B)
EF = c[0] + c[1] * x + c[2] * x ** 2 + c[3] * x ** 3
e = yj - EF
print(np.sqrt(np.sum(e ** 2) / n))
print(max(e))
plt.plot(x, yj, '--')
plt.plot(x, EF, 'x')
plt.show()