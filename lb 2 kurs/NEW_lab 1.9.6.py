import numpy as np
from random import *

n = 6
p = 1
r = 0.1
b = 0.01
eps = 10 ** -3
Y0 = 0.1
Y1 = 0.01
x0 = np.zeros(n)
A = np.zeros((n, n))
for i in range(1, n):
    x0[i] = np.random.uniform(0, 1)
    A[i][i] = 6.5 * i ** (p / 3)
    for j in range(1, n):
        A[i][j] = b * np.exp(-r / ((i + j) ** r))
A = A[1:n, 1:n]
x0 = x0[1:n]
k = 0
while np.linalg.norm(Y1 - Y0) > eps and k < 10:
    x0norm = np.dot(x0, x0) ** (1 / 2)
    e1 = x0 / x0norm
    x0 = np.dot(A, e1)
    Y1 = np.dot(x0, e1)
    k += 1
print(np.linalg.eig(A))
print(Y1, k)
