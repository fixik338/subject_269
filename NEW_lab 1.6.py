def add(x):
    f = x * (1 - x) - (1 / 8)
    return f


import numpy as np

k = int(input("Peremennaya k: "))
j = int(input("Peremennaya j: "))
m = int(input("Peremennaya m: "))
n = int(input("Razmernost': "))
f = np.zeros(n)
h = 1 / (n - 1)
x = np.arange(0, 1, h)
f = np.array(add(x))
pos = len(f[f > 0])
neg = len(f[f < 0])
print(f, '\n' "max =", max(f), 'imax = ', f.argmax(), '\n' 'min = ', min(f), 'imin = ', f.argmin())
srd = np.sum(f)
srdkv = np.sum(f ** 2)
srd = srd / n
srdO = np.sum((f - srd) ** 2)
print("Fsrd:= ", srd, '\n' "Fsrdkv:= ", srdkv / n, '\n' "Fm:= ", np.sqrt(srdkv), '\n' 'srdOTKL:= ', srdO / n,
      '\n' 'pos = ', pos / n, '\n' 'neg = ', neg / n)
