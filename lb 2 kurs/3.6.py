import numpy as np
import numpy.random as rand


class A:
    def __init__(self, F):
        self.A = F
        self.det = np.linalg.det(F)
        self.inv = np.linalg.inv(F)

    def chg(self):
        for i in range(len(self.A)):
            for j in range(len(self.A)):
                self.A[i][j] = int(input())

    def check(self, T):
        Ts = T / self.det
        return 'True' if Ts.all() == self.inv.all() else 'False'

    def rand(self):
        self.A = rand.sample((len(self.A), len(self.A)))

    def show(self):
        for i in range(len(self.A)):
            for j in range(len(self.A)):
                print('{0:.1f}'.format(self.A[i][j]), end=' ')
            print()


S = [[3, -2], [-2, 1]]
T = np.array([[S[1][1], -S[0][1]], [-S[1][0], S[0][0]]])
B = A(S)
print(B.check(T))
