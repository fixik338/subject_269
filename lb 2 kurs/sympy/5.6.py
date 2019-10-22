from sympy import *
a, b, x, y, t, f, k, c1, c2 = symbols('a b x y t f k c1 c2')
C = 2*(x**2)-5*x+7
C2 = 6*(x**2) + 6*x - 36
C3 = 3*(x**3)-2*(x**2)-2*x+3
C4 = 2*(x**4)+6*(x**2) - 20
C4 = C4.subs(x**2, y)
C5 = diff(t*exp(2*t+3), t)
C6 = 12345
print("1-е:", solve(C), '\n2-е:', solve(C2), '\n', factor(C2), '\n3-е:',
      factor(C3), '\n4-е:', solve(C4), '\n5-e:', C5, '\n6-e', C6)
