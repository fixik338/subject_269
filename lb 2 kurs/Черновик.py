import numpy as np
p = 3
r = 1
t = 1
N = 5


def check(a, b):
    return np.linalg.solve(a, b)


def get_l(A):
    l = A.copy()
    for i in range(l.shape[0]):
        l[i, i] = 1
        l[i, i + 1:] = 0
    return l


def get_u(A):
    u = A.copy()
    for i in range(1, u.shape[0]):
        u[i, :i] = 0
    return u


def decomp(a, l, u):
    lu_matrix = np.zeros([a.shape[0], a.shape[1]])
    n = a.shape[0]
    for k in range(n):
        for j in range(k, n):
            lu_matrix[k, j] = a[k, j] - np.dot(l, u)
        for i in range(k + 1, n):
            lu_matrix[i, k] = (a[i, k] - np.dot(l, u)) / u
    return lu_matrix


def solve_lu(lu_matrix, b):
    y = np.zeros([lu_matrix.shape[0], 1])
    for i in range(y.shape[0]):
        y[i, 0] = b[i] - np.dot(lu_matrix[i, :i], y[:i])
    x = np.zeros([lu_matrix.shape[0]])
    for i in range(1, x.shape[0] + 1):
        x[-i] = (y[-i] - np.dot(lu_matrix[-i, -i:], x[-i:]))/lu_matrix[-i, -i]
    return x


A = np.zeros((N, N))
B = np.zeros(N)
for i in range(0, N):
    for j in range(0, N):
        A[i][j] = 10 ** -3 * np.exp(-r / (abs((i+1) + (j+1)) ** t))
        A[i][i] = 8.5 * (i+1) ** (p / 3)
    B[i] = (7.5 * i + 1) ** (t / 2)

if A.any() == np.dot(get_l(A), get_u(A)).any():
    print("YES, YES, YES")

print("Искомое:", check(A, B), '\nОтвет:', solve_lu(decomp(A,get_l(A), get_u(A)), B))
