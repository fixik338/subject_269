from sympy import *
a, x = symbols('a x')
C = exp(-a*x)*(1+2*cos(a*x))
Cs = C.series(x, 0, 5)
Cd = diff(Cs, a)
print(Cs, '\n', Cd)
