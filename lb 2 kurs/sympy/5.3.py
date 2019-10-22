from sympy import *

a, b, x, y = symbols('a b x y')
C = (a**b)-(a**2)+2*a*(b**2)-3*a*b+1
C = C.subs(a, x)
C = C.subs(b, x+y**2)
print(C)
