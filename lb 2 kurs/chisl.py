import numpy as np

a = [[130, 4, 7, 9],
     [5, 190, 12, 8],
     [2, 3, 120, 7],
     [2, 7, 3, 110]]

b = [10, 15, 11, 10]

B = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

x1 = [10, 15, 11, 10]

x2 = [0, 0, 0, 0]

for i in range(4):
    for j in range(4):
        if i != j:
            B[i][j] = (- a[i][j] / a[i][i])

r = np.linalg.solve(a, b)

for i in range(4):
    for j in range(4):
        print('{0:.6f}'.format(B[i][j]), end=' ')
    print()

e = 10**-8
Bnrm = 0
for i in range(4):
    for j in range(4):
        Bnrm += B[i][j] ** 2
Bnrm = Bnrm**(1/2)
print(Bnrm)
e1 = ((1 - Bnrm) / Bnrm) * e
d = []
for i in range(4):
    d.append(b[i] / a[i][i])


def norma(a1, b2):
    n = 0
    for p in range(4):
        n += (a1[p] - b2[p]) ** 2
    return n ** (1 / 2)

for i in range(4):
    for j in range(4):
        x2[i] += B[i][j] * x1[i]

for i in range(4):
    x2[i] += d[i]

print(e1)
k = 0
while norma(x1, x2) > e1:
    for i in range(4):
        x1[i] = x2[i]
    x2 = np.dot(B, x1)+d
    k += 1
print(r)
print(x2)
print(k)

