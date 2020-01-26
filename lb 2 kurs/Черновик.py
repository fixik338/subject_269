import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
n = 50
a = 1
b = 2
h = 1 / n


def f(x):
    return np.tan((np.pi * (x ** (1 / m))) / 4) ** k


def tf(x):
    return x ** 2



yR2 = []
j = np.arange(1, n)
x = j * h
