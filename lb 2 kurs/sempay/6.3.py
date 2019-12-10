from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')
x1 = np.arange(0, 50, 0.1)
f1 = (x ** 2) * cos(x) + 2 * x + 4
df1 = diff(x ** 2 * cos(x) + 2 * x + 4)
vf = [0]*500
vf1 = [0]*500
for i in range(len(x1)):
    vf[i] = f1.subs(x, x1[i])
    vf1[i] = df1.subs(x, x1[i])
plt.plot(vf, vf1)
plt.show()
