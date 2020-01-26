import numpy as np
import matplotlib.pyplot as plt
from math import *
def fe(x):
    return -np.sin(x)*np.sin(x)
def f(x):
    return -sin(x)*sin(x)
def df(x):
    return -2*sin(x)*cos(x)
def ddf(x):
    return -2*cos(2*x)
e = 10 ** -6
k = 0
kmax = 20
x = pi/4
x1 = x - (f(x) / df(x))
while abs(df(x)) > e and k < kmax:
    x1 = x - (df(x) / ddf(x))
    x = x1
    k += 1
print(x)
xe = np.arange(0, 6, 0.1)
plt.plot(xe, fe(xe))
plt.show()
