#Matrix in Python
import numpy as np
from numpy import linalg as LA, linspace
import matplotlib.pyplot as plt
from math import *
# use np.array for matrices
n = 10 #5x5 Matrix
d1 = np.diag(np.ones(n)*2, k=0) # Diagonal 2s
d2 = np.diag(np.ones(n-1), k=1) # Diagonal 1s right
d3 = np.diag(np.ones(n-1), k=-1) # Diagonal 1s left
matrix = d1 + d2 + d3
print(matrix)
G = (1/(2*(1/(n-1)**2)))*matrix
print(G)
r, q = LA.eig(G)
print(r, q)
delta_x = 1/(n + 1)
normal = np.sqrt(np.sum(np.power(q,2)*delta_x)) # np from numpy, np.power(q,2) is equivalent to q**2
eig5 = q[:,n-2]
print(eig5)
x = linspace(0, 1, n+2)
plt.plot(x[1:n+1], eig5)
plt.show()