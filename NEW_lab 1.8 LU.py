import numpy as np
p = 3
r = 1
t = 1
N = 5

A = np.zeros((N, N))
B = np.zeros(N)
for i in range(0, N):
    for j in range(0, N):
        A[i][j] = 10 ** -3 * np.exp(-r / (abs((i+1) + (j+1)) ** t))
        A[i][i] = 8.5 * (i+1) ** (p / 3)
    B[i] = (7.5 * i) ** (t / 2)
print(np.linalg.det(A))
U = np.zeros((N, N))
L = np.zeros((N, N))
k = np.arange(N)
for i in range(N):
    for j in range(N):
        if i < 2:
            U[0][j] = A[0][j]
            L[j][0] = A[j][0]/U[0][0]
        else:
            U[i][j] = A[i][j] - np.dot(L[i][k], U[k][j])
            L[j][i] = np.dot((1/U[i][i]), (A[j][i] - np.dot(L[j][k], U[k][i])))
for i in range(N):
    for j in range(N):
        print('{0:.6f}'.format(L[i][j]), end=' ')
    print()
for i in range(N):
    for j in range(N):
        print('{0:.6f}'.format(U[i][j]), end=' ')
    print()
