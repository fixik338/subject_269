import numpy as np

a = np.array([[2, 1, -1, 2],
             [2, 3, -3, 4],
             [8, 3, 2, 2],
             [8, 1, 1, 5]])
A = np.array([[2, 1, -1, 2],
              [2, 3, -3, 4],
              [8, 3, 2, 2],
              [8, np.NaN, 1, 5]])
print(a > 1)
