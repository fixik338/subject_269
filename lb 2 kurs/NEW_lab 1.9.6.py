from numpy import *
n = 5
p = 1
r = 0.1
b = 0.01
A = zeros((n, n))
for i in range(1, n):
    A[i][i] = 6.5 * i ** (p / 3)
    for j in range(1, n):
        A[i][j] = b*exp(-r/((i + j)**r))
A = A[1:n, 1:n]
print(A)
