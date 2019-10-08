import numpy as np
import numpy.random as rand


class A:

    def __init__(self, D):
        self.matrix = D

    def chg(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j] = int(input())

    def show(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print('{0:.1f}'.format(self.matrix[i][j]), end=' ')
            print()

    def rand(self):
        self.matrix = rand.sample((len(self.matrix), len(self.matrix)))

    def det(self):
        l = np.shape(self.matrix)
        if l[0] == l[1]:
            a = np.linalg.det(self.matrix)
            return a
        else:
            return 'Не имеет определителя'


D = [[3, -2, 1], [-2, 1, 3], [2, 0, -2]]
D2 = [[30, -10, -10], [-2, 9, -2], [-13, 3, 5]]

C = A(D)
C2 = A(D2)
print(C.det(), C2.det())
C.chg()