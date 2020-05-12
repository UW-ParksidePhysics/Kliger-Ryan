import numpy as np
data = np.array([[1.0,2.0],[3.0,4.0]])
while True:
    try:
        u = data[0]
        v = data[1]
        break
    except IndexError:
        print('Data Array has inappropriate dimensions, please use array with two dimensions')

#Mean
mean2 = sum(v)/len(v)


print('The mean of the second sample is: ', mean2)
#Standard Deviation
variance2 = sum([((float(i) - mean2)**2) for i in v])/len(v)
res2 = variance2**0.5
print("Standard deviation of the second sample is: " + str(res2))

#Max and Min
maxu= max(u)
maxv = max(v)
print(maxu)
print(maxv)

minu = min(u)
minv = min(v)
print(minu)
print(minv)

values = np.array([mean2, res2, maxu, minu, maxv, minv])
print(values)


