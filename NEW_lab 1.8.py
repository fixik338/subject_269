import numpy as np
p = 3
r = 1
t = 1
N = 4

A = np.zeros((N, N))
B = np.zeros(N)
for i in range(N):
    for j in range(N):
        A[i][j] = 10 ** -3 * np.exp(-r / (abs((i+1) + (j+1)) ** t))
        A[i][i] = 8.5 * (i+1) ** (p / 3)
    B[i] = (7.5 * i+1) ** (t / 2)
print(B)
S = np.linalg.solve(A, B)
# for i in range(N):
# #     for j in range(i, N):
# #         xx = A[j][i]/A[i][i]
# #         A[j, :] -= A[i, :]*xx
# #         B[j] -= B[i]*xx

for i in range(N):
    for j in range(N):
        print('{0:.6f}'.format(A[i][j]), end=' ')
    print()

X = np.ones(N)
i = N - 1
while i > -1:
    if A[i][i] != 0:
        X[i] = (B[i] - np.dot(A[i][:i], X[:i])) / A[i][i]
    i += -1
print(A)
print(S)
print(X)
'''       /\
         /||\
        / || \
       /  ||  \
          || -  Это решение Системы Линейных Алгебраических Уравнени, методом Гаусса'''
