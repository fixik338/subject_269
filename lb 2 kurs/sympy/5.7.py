from sympy import*
x, y = symbols('x y')
y = x**-2
S1 = integrate(y, (x, 2, 7))
print("S1 = ", S1)
y = x**3
S2 = integrate(y, (x, 3))
print("S2 = ", S2)
y = 9 - x**2
S3 = integrate(y, x)
print("S3 = ", S3)
y = sin(x) + 5
i1 = integrate(y, (x, 2, 5))
y = x**-2
i2 = integrate(y, (x, 2, 5))
S4 = i1 + i2
print("S4 = ", S4)
