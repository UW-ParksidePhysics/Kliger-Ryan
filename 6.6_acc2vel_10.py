import matplotlib.pyplot as plt
import numpy as np

a = 101
dt = 1

def velocity(a, dt):
    n = len(a)
    v = np.zeros(n)
    for k in np.arange(1, n):
        v[k] = v[k-1] + dt*0.5*(a[k-1] + a[k])
    return v


acc = np.loadtxt('acc.data.py')

vel = velocity(acc, dt)
time = np.array([i * dt for i in range(0, len(acc))])

plt.plot(time, acc, color='red', linewidth=2)
plt.plot(time, vel, color='green', linewidth=2)
plt.xlabel('Time')
plt.legend(['Acceleration', 'Velocity'], loc=2.5)
plt.title('Velocity and Acceleration')
plt.show()