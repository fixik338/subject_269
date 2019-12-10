import matplotlib.pyplot as plt
import numpy as np
import pylab
import sympy as sp
"==== №1 ===="
x = np.arange(0.1, 5, 0.1)
f1 = x ** (1 / 2)
f2 = 2 * np.log(x)
plt.subplot(331)
plt.plot(x, f1, "red", x, f2, "blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphic 1")
plt.fill_between(x, f1, f2, where=(f1 > f2), color="green")
plt.fill_between(x, f1, f2, where=(f1 < f2), color="orange")
plt.grid(True)
"==== №2 ===="
x1 = np.arange(0, 10, 0.1)
x2 = np.arange(2, 6)
x3 = np.arange(-10, 50)


def f3(x):
    return x ** 2 * np.cos(x) + 2 * x + 4


def df3(f, x):
    return np.diff(f, x.all())


plt.subplot(332)
plt.plot(x1, f3(x1), "-.", df3(f3(x1), x1), "--")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphic 2.1")
plt.grid(True)
plt.subplot(333)
plt.plot(x2, f3(x2), "-.", df3(f3(x2), x2), "--")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphic 2.2")
plt.grid(True)
plt.subplot(334)
plt.plot(x3, f3(x3), "-.", df3(f3(x3), x3), "--")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphic 2.3")
plt.grid(True)
"==== №3 ===="
plt.subplot(338)
x = sp.symbols('x')
x1 = np.arange(0, 50, 0.1)
f1 = (x ** 2) * sp.cos(x) + 2 * x + 4
df1 = sp.diff(x ** 2 * sp.cos(x) + 2 * x + 4)
vf = [0]*500
vf1 = [0]*500
for i in range(len(x1)):
    vf[i] = f1.subs(x, x1[i])
    vf1[i] = df1.subs(x, x1[i])
plt.plot(vf, vf1, '->')
plt.title("Graphic 3")
pylab.xlim(-2500, 2500)
pylab.ylim(2500, -2500)
plt.tick_params(labelbottom=False, labelleft=False)
"==== №4 ===="
plt.subplot(336)
x = np.arange(0, 10, 0.2)
f5 = np.sin(2 * x)
plt.plot(x, f5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphic 4")
plt.grid(True)
plt.show()