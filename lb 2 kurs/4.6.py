import numpy as np


class A:

    def __init__(self, x1, x2, x3, x4):
        self.a1 = x1
        self.a2 = x2
        self.a3 = x3
        self.a4 = x4

    def solve(self):
        S = np.array((self.a1, self.a2, self.a3, self.a4)).transpose()
        b = np.linalg.matrix_rank(S)
        print('Ранг линейной оболочки: ', np.linalg.matrix_rank(S))
        R = S[:, 0:b]
        return R


a1 = [1, 2, 3, -1, 2]
a2 = [2, 3, 5, 1, 1]
a3 = [5, 8, 13, 1, 4]
a4 = [3, 4, 7, 3, 0]
V = A(a1, a2, a3, a4)
print(V.solve())
