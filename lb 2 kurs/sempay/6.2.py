from sympy import *
from sympy.abc import *
from sympy.plotting import *

F1 = lambda x: (x**2)*cos(x)+(2*x)+4
F2 = lambda x: diff(F1(x), x)
a, b = 0, 10
q = plot_parametric((F1(x), (x, a, b)), (F2(x), (x, a, b)), show=False)
q.show()