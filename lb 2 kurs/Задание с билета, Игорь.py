from math import *
import numpy as np
def L(Si, k):
    n = 0
    l0 = []
    l0.append(Si[0])
    while n < k:
        l0.append(Si[n+1] - Si[n])
        n += 1
    return l0




k = 10

a = 0
b = pi/2
x = []
Si = []
while a < b:
    x.append(a)
    a += 0.1
for i in range(len(x)):
    Si.append(sin(x[i]))
print(Si)
print(x)
print('Иксы: ', Si)
print('Ответ: ', L(Si, k))