import numpy as np
from random import *
import time

s = 1000
A = np.zeros((s, s))
b = np.zeros(s)
x2 = np.zeros(s)
x1 = np.zeros(s)
T1 = time.time()
for i in range(len(A)):
    for j in range(len(A)):
        A[i][j] = randint(1, 2)
    A[i][i] *= 1000
    b[i] = randint(1, 15)
    x1[i] = randint(1, 5)
print(A, b)
e = 10 ** -8
r = np.zeros(len(A))
t = 0
k = 0
while np.linalg.norm(x1-x2) > e:
    x1 = np.copy(x2)
    r = np.dot(A, x1) - b
    t = r * r / (r * np.dot(A, r))
    x2 = x1 - t*r
    k += 1
T2 = time.time()
v = np.linalg.solve(A, b)
T3 = time.time()
print("Исходная норма: ", np.linalg.norm(v - x2))
print('Наше решение: = ', T2 - T1, 'cек.', '\nВремя Solve: = ', T3 - T2, 'cек.')
print(k)
