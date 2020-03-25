import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x / np.log(x) ** 2


def f_test(x):
    return np.exp(-x ** 2)


# h_test = 0.1
# x_test = np.arange(0, 1, h_test)
# i_test = np.arange(len(x_test) - 1)
# fx_test = f_test(x_test)
# x7_test = x_test - h / 2
# fx7_test = f_test(x7_test)
h = 1/50
x = np.arange(1.5, 3, h)
i = np.arange(len(x) - 1)
fx = f(x)
x7 = x - h / 2
fx7 = f(x7)
Ipr = h * np.sum(fx7)
Itr = h * (((fx[0]+fx[1])/2)+np.sum(fx))
Isim = h / 6 * (fx[0] + fx[-1] + 4 * np.sum(fx7) + 2 * np.sum(fx[i]))
print('', Ipr, '\n', Itr, '\n', Isim)
