time = []
y = []
v = 20
g = 9.8
tmax = 2 * v / g
tmax = int(tmax)
for t in range(0, tmax):
    time.append(t)
    y.append(v * t - (1 / 2) * g * t ** 2)
print(time, y)
