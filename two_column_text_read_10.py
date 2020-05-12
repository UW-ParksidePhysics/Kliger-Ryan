# Read two columns
import numpy as np
import matplotlib.pyplot as plt
while True:
    try:
        infile = open('str', 'r') # str is name of file
        break
    except OSError:
        print("File not found, please select different file")

x = [] # column 1
y = [] # column 2

for line in infile:
    content = line.split() #splits two columns for reading
    x.append(content[0])
    y.append(content[1])
infile.close()
print(x)
print(y)

x, y = np.array(x), np.array(y)
plt.plot(x, y, color='red', linewidth=1.5)
plt.xlabel('Enter text')
plt.ylabel('Enter more text')
plt.show()