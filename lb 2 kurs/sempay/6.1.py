from sympy import *
from sympy.abc import *
from sympy.plotting import *
import math

F1 = lambda x: x**(1/2)
F2 = lambda x: 2 * log(x)
a, b = 0, 5
q = plot((F1(x), (x, a, b)), (x**2, (x, 0, 5)), (F2(x), (x, a, b)), show=False)
q[0].line_color = 'red'
q[1].line_color = 'purple'
q[2].line_color = 'blue'

q.show()
