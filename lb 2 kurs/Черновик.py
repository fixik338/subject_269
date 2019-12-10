import numpy as np
import sympy as sp
import matplotlib.pyplot as plt



a = -1
b = 1
m = 1
n = 2
e = 10 ** -3
k = 0
kmax = 50
x0 = sp.symbols('x')
df = sp.diff(0.5*(x0 + 1)**(-0.5) - sp.pi*sp.cos(sp.pi*x0/4)/4)
print (df)