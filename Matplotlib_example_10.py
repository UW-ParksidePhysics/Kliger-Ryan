#Basic Animation in Matplotlib
import ...

plt.ion()
#Make first plot
def f(x, m, s):
    return (1.0 / (sqrt(2 * pi) * s)) * exp(-0.5 * ((x - m) / s) ** 2)


m = 0
s_min = 0.2
s_max = 2
x = linspace(m - 3 * s_max, m + 3 * s_max, 1000)
s_values = linspace(s_max, s_min, 30)
y = f(x, m, s_max)

max_f = f(m, m, s_min)

lines = plt.plot(x, y)
plt.axis([x[0], x[-1], -0.1, max_f])
plt.xlabel('x')
plt.ylabel('f')
#Show Movie
counter = 0
for s in s_values:
    y = f(x, m, s)
    lines[0].set_ydata(y)
    plt.legend(['s=%4.2f'.format(s)])
    plt.draw()
    plt.savefig('tmp_{:04d}.png'.format(counter))
    counter += 1 

