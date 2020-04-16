# Matrix in Python
from numpy import *
import matplotlib.pyplot as plt

mu = 5 # Mean
x = linspace(0, 10, 11)
s1 = 0.5
s2 = 1.0
s3 = 1.5

f1 = (1 / 2 * sqrt(2 * pi * s1 ** 2)) * exp(-(x - mu) ** 2 / 2 * s1 ** 2)
f2 = (1 / 2 * sqrt(2 * pi * s2 ** 2)) * exp(-(x - mu) ** 2 / 2 * s2 ** 2)
f3 = (1 / 2 * sqrt(2 * pi * s3 ** 2)) * exp(-(x - mu) ** 2 / 2 * s3 ** 2)
plt.plot(x, f1, x, f2, x, f3)
plt.show()
