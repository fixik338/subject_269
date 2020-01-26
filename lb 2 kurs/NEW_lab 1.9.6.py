import numpy as np
n = 6
p = 1
r = 0.1
b = 0.01
kmax = 3
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
m = []
Y = []
n = n - 1
print("Проверка: ", np.linalg.eig(A))
for t in range(n):
    x0 = np.random.sample(n-t)
    k = 0
    Y0 = 0.1
    Y1 = 0.01
    while np.linalg.norm(Y1 - Y0) > eps and k < kmax:
        x0norm = np.dot(x0, x0) ** (1 / 2)
        e1 = x0 / x0norm
        x0 = np.dot(A, e1)
        Y1 = np.dot(x0, e1)
        eps = 10 ** -3
        k += 1
    Y.append(Y1)
    H = np.eye(n - t)
    for i in range(n - t):
        H[i][0] = -x0[i] / x0[0]
    H[0][0] /= x0[0]
    Hminus1 = np.linalg.inv(H)
    A = np.dot(np.dot(H, A), Hminus1)
    A = A[1:n, 1:n]
print(" Вектор х: ", x0, "\nCобст. числа: ", Y, "\nКол-во итераций: ", k)
