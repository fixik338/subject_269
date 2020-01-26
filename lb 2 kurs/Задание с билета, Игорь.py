import math as mt
import numpy as np

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


# def x(a, b, k):
#     z = 0
#     for i in range(a, k):
#         if(z <= b):
#             z += 0.1
#         else:
#             break
#     return z

k = 10
a = 0
b = np.pi/2
# x = [slice(a, b)]
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = np.arange(a, b, 0.1)
xp = np.array(x)
# print(x(a, b, k))
print('Иксы: ', f(x, k))
print('Ответ: ', L(f(x, k), k))
# print('Проверка: ', np.linalg.solve(mt.sin(x), x))
# print(x(a, b, k))