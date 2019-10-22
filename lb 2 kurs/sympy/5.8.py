from sympy import *
x, y = symbols('x y')
L1 = limit(((x**2) - 4)/(x - 2), x, 2)
L2 = limit(1/(x - 5) - 10/((x**2) - 25), x, 5)
L3 = limit(sin(x)/x, x, 0)
L4 = limit(((x + 2*y)/x)**x, x, oo)
L5 = limit((1 + 1/x)**(2*x + 1), x, oo)
L6 = limit(tan(x)/x, x, 0)
print("1-й предел: ", L1, '\n2-й предел:', L2, '\n3-й предел:', L3, '\n4-й предел:', L4, '\n5-й предел:', L5, '\n6-й '
                                                                                                              'предел:', L6)