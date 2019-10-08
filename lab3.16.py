import numpy as np
N = int(input('Кол-во строк :'))
x = np.zeros(N)
for i in range(N):
    x[i] = input('Введите элемент : ')
print(x)
b = x[x < 0]
c = x[x >= 0]
z = abs(sum(b)) - sum(c)
x = np.append(x, [z])
print(x)
