import numpy as np
N = int(input("Кол-во строк :"))
M = int(input("Кол-во столбцов :"))
L = int(input("Ввести строку для удаления :"))
d = np.ones((N, M))
c = [i for i in range(N) if i != L-1]
d = d[c, :]
print(d)