import numpy as np

a = [[130, 4, 7, 9],
     [5, 190, 12, 8],
     [2, 3, 120, 7],
     [2, 7, 3, 110]]

b = [10, 11, 11, 10]

x = [10, 11, 11, 10]

c = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

d = [0, 0, 0, 0]
x1 = [11, 11, 15, 15]
'------------------------------'
for i in range(len(a)):
    for j in range(len(a)):
        d[i] = (b[i] / a[i][i])
        if j != i:
            c[i][j] = (-a[i][j] / a[i][i])
'-----e1--------'
e = 10 ** -8

cnrm = 0

for i in range(len(a)):
    for j in range(len(a)):
        cnrm += c[i][j] ** 2

cnrm = cnrm ** (1 / 2)

e1 = ((1 - cnrm) / cnrm) * e
'-----Нормирование--------'
def norma(a1, b2):
    n = 0
    for p in range(len(a)):
        n += (a1[p] - b2[p]) ** 2
    return n ** (1 / 2)


'-------------------------------'
k = 0
while norma(x, x1) > e:
    x = np.copy(x1)
    for i in range(len(a)):
        x1[i] = d[i]
        for j in range(len(a)):
            if j < i:
                x1[i] += c[i][j] * x1[j]
            else:
                x1[i] += c[i][j] * x[j]
    k += 1
r = np.linalg.solve(a, b)
print(r)
print(x1)
print(k)