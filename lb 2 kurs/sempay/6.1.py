import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 5, 0.1)
f1 = x**(1/2)
f2 = 2 * np.log(x)
q1 = plt.plot(f1, x, color="red")
q2 = plt.plot(f2, x, color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphic_1")
plt.fill_between(x, f1, f2, color="green")
plt.fill_between(x, f1, f2, color="orange")
plt.show()

# f3 = x**2*np.cos(x) + 2*x + 4
# df3 = np.diff(f3, x)
# q2 = plt.plot(f3, df3, x, title='Graphic_2', xlabel='x', ylabel='y', show=False)
# q2.show()