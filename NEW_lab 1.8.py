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
i = np.arange(0, N + 1)
B = np.array((7.5 * i) ** (t / 2))
A = A[1:N+1, 1:N+1]
A2 = A[1:N+1, 1:N+1]
B = B[1:N+1]
B1 = B[1:N+1]
'''
for i in range(10):
    for j in range(10):
        print('{0:.6f}'.format(A[i][j]), end=' ')
    print()
'''
for i in range(N):
    for j in range(i+1, N):
        xx = A[j, i]/A[i, i]
        A[j, :] -= A[i, :]*xx
        B[j] -= B[i]*xx

X = np.zeros(N)
X[N - 1] = B[N - 1] / A[N - 1][N - 1]
i = N - 1
while i > 0:
    X[i] = (B[i] - np.dot(A[i][:i], X[:i])) / A[i][i]
    i += -1
print(X)
'''       /\
         /||\
        / || \
       /  ||  \
          || -  Это решение Системы Линейных Алгебраических Уравнени, методом Гаусса'''
