import numpy as np
from random import *

n = 4
p = 1
r = 0.1
b = 0.01
eps = 10 ** -3
Y0 = 0.1
Y1 = 0.01
x0 = np.zeros(n)
A = np.zeros((n, n))
Q = np.zeros((n, n))
for i in range(0, n):
    A[i][i] = 6.5 * (i+1) ** (p / 3)
    for j in range(0, n):
        A[i][j] = b * np.exp(-r / (((i+1) + (j+1)) ** r))
print(A, '\n')
q = 1-(2/(n*(n-1)))
k = 0
imax = 0
jmax = 0
L = np.copy(A)
sig = np.sum(A**2) - np.sum(np.diag(A)**2)
sig1 = 1
while sig1 >= q*sig:
    amax = np.max(A - np.diag(A) * np.eye(n))
    for i in range(n):
        for j in range(n):
            if amax == A[i][j]:
                jmax = i
                imax = j
    P = (2*amax)/(A[jmax][jmax] - A[imax][imax])
    fi = np.arctan(P)/2
    Q[0][0] = 1
    Q[-1][-1] = 1
    Q[imax][imax] = np.cos(fi)
    Q[jmax][jmax] = np.cos(fi)
    Q[imax][jmax] = np.sin(fi)
    Q[jmax][imax] = -np.sin(fi)
    # Q[jmax+1][jmax+1] = 1
    Q[imax-1][imax-1] = 1
    sig = np.sum(A ** 2) - np.sum(np.diag(A) ** 2)
    B = np.dot(A, Q)
    A = np.dot(Q.T, B)
    sig1 = np.sum(A ** 2) - np.sum(np.diag(A) ** 2)
    k += 1
print(imax, jmax)
print(Q, '\n', "Проверка: ", np.linalg.eig(A))
print("L: ", A, "\n", 'пися', "\n", "пися2: ", k)