import numpy as np


class F:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def kramer(self):
        x = []
        R = np.copy(self.A)
        for i in range(len(self.A)):
            R[:, i] = self.B
            x.append(round(np.linalg.det(R)/np.linalg.det(self.A)))
            R[:, i] = A[:, i]
        return x

    def gauss(self):
        X = np.linalg.solve(self.A, self.B)
        return X

    def check(self):
        return len(np.linalg.solve(self.A, self.B)) ==  np.linalg.matrix_rank(self.A)


A = np.array([[2, 1, -1, 2],
              [2, 3, -3, 4],
              [8, 3, 2, 2],
              [8, 5, 1, 5]])
B = np.array([-4, -14, -1, -7])
M = F(A, B)
print(M.gauss())
print("Корень по Крамеру: ", M.kramer())
print(M.check())