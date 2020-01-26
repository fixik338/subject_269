from math import *

def f(x, k):
    interval = []
    x1 = []
    for i in x:
        x1[i] = np.sin(x)
        interval.append(x1[i])
    return interval


def L(f, k):
    n = 0
    l0 = f[0]
    while n < k:
        l0 += f[n+1] - f[n]
        n += 1
        return l0




k = 10
a = 0
b = pi/2
x = []
while a < b:
    x.append(a)
    a+=0.1
print(x)
# print(x(a, b, k))
# print('Иксы: ', f(x, k))
# print('Ответ: ', L(f(x, k), k))
# print('Проверка: ', np.linalg.solve(mt.sin(x), x))
# print(x(a, b, k))