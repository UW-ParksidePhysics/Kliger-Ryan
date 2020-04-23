import matplotlib.pyplot as plt
import numpy as np
x = []
y = []

infile = open('xy.data.py', 'r')
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

print('Minimum x value = %f' % x.min())
print('Maximum x value = %f' % x.max())
print('Minimum y value = %f' % y.min())
print('Maximum y value = %f' % y.max())

plt.plot(x, y, color='red', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()