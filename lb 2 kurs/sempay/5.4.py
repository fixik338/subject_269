from sympy import *
a, b, x, y = symbols('a b x y')
C = (x+1+x*y)**2
C = C.subs(y, 3*x-2*b)
C = C.subs(x, b + 2)
print(C)
