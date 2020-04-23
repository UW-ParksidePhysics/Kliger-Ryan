import matplotlib.pyplot as plt
import numpy as np


x = []
y = []

infile = open('densitywater.py', 'r')
for line in infile:
    coords = line.split()
    if coords[0][0] != '#':
        x.append(float(coords[0]))
        y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

plt.plot(x, y, color='red', linewidth=2)
plt.xlabel('Degrees Celsius')
plt.ylabel('Density')
plt.show()
