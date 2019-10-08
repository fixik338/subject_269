import numpy as np
N = int(input("Кол-во строк :"))
M = int(input("Кол-во столбцов :"))
L = int(input("Ввести строку :"))
K = int(input("Ввести столбец :"))
d = np.ones((N, M))
for i in range(N):
    for j in range(M):
