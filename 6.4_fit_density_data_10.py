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
infile2 = open('densityair.py', 'r')

x2 = []
y2 = []
for line in infile2:
    coords2 = line.split()
    if coords2[0][0] != '#':
        x2.append(float(coords2[0]))
        y2.append(float(coords2[1]))
infile2.close()

x, y = np.array(x), np.array(y)
print(x)
x2, y2 = np.array(x2), np.array(y2)
d1 = np.polyfit(x, y, 1)
p1 = np.poly1d(d1)
d12 = np.polyfit(x, y, 2)
p12 = np.poly1d(d12)
#print(p1)
d2 = np.polyfit(x2, y2, 1)
p2 = np.poly1d(d2)
d22 = np.polyfit(x2, y2, 2)
p22 = np.poly1d(d22)

#print(p2)
plt.plot(x, y, color='red', linewidth=2,)
plt.plot(x, p1(x), color='green')
plt.plot(x, p12(x), color='yellow')


plt.plot(x2, y2, color='blue', linewidth=2,)
plt.plot(x2, p2(x2), color='purple')
plt.plot(x2, p22(x2), color='orange')

plt.xlabel('Degrees Celsius')
plt.ylabel('Density')
plt.show()
