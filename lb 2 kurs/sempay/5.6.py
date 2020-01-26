from sympy import *


class A:
    def __init__(self, c):
        self.c = c

    def solve(self):
        return solve(self.c)

    def factor(self):
        return factor(self.c)

    def diff(self, t):
        return diff(self.c, t)

    def diff2(self):
        const1, const2 = symbols('const1 const2')
        kr = solve(self.c)
        y = const1*exp(kr[0]*x) + const2*exp(kr[1]*x)
        return y


a, b, x, y, t, k = symbols('a b x y t k')
C1 = 2*(x**2)-5*x+7
C2 = 6*(x**2) + 6*x - 36
C3 = 3*(x**3)-2*(x**2)-2*x+3
C4 = 2*(x**4)+6*(x**2) - 20
C4 = C4.subs(x**2, y)
C5 = t*exp(2*t+3)
C6 = k**2 - 2*k - 3
# C6 = diff(diff(y, x), x) - 2* diff(y, x) - 3
# C6 = C6.subs(diff(diff(y, x), x), k**2)
# C6 = C6.subs(diff(y, x), k))

c1 = A(C1)
c2 = A(C2)
c3 = A(C3)
c4 = A(C4)
c5 = A(C5)
c6 = A(C6)

print("1-е:", c1.solve(),
      '\n2-е:', c2.solve(), '\n', c2.factor(),
      '\n3-е:', c3.factor(),
      '\n4-е:', c4.solve(),
      '\n5-e:', c5.diff(t),
      '\n6-e:', c6.diff2())