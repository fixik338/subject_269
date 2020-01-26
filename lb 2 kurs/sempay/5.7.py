from sympy import*

class A:
    def __init__(self, y):
        self.y = y

    def integ(self, x, a, b):
        return integrate(self.y, (x, a, b))

x = symbols('x')
y1 = x**(1/2)
y2 = x**3
y3 = 9 - x**2
y4 = sin(x) + 5
y5 = x**(1/2)

i1 = A(y1)
i2 = A(y2)
i3 = A(y3)
i4 = A(y4)
i5 = A(y5)
print("i1 = ",  i1.integ(x, 2, 7),
      '\ni2 =', i2.integ(x, 0, 3),
      '\ni3 =', i3.integ(x, 0, x),
      '\ni4 =', i4.integ(x, 2, 5) + i5.integ(x, 2, 5))