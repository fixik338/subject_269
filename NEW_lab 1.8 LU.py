import numpy as np
p = 3
r = 1
t = 1
N = 10

A = np.zeros((N, N))
B = np.zeros(N)
for i in range(0, N):
    for j in range(0, N):
        A[i][j] = 10 ** -3 * np.exp(-r / (abs((i+1) + (j+1)) ** t))
        A[i][i] = 8.5 * i ** (p / 3)
    B[i] = (7.5 * i + 1) ** (t / 2)
print(np.linalg.solve(A, B))
U = A
L = np.tril(A)
for i in range(10):
    for j in range(10):
        print('{0:.6f}'.format(L[i][j]), end=' ')
    print()
