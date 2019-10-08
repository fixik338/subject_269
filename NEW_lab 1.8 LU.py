import numpy as np
p = 3
r = 1
t = 1
N = 10

A = np.zeros((N+1, N+1))
for i in range(1, N+1):
    for j in range(1, N+1):
        A[i][j] = 10 ** -3 * np.exp(-r / (abs(i + j) ** t))
        A[i][i] = 8.5 * i ** (p / 3)
U = A
L = np.tril(A)
for i in range(10):
    for j in range(10):
        print('{0:.6f}'.format(L[i][j]), end=' ')
    print()
