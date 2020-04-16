# Planet Orbit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
a = 20
b = 20
w = 20
t = 60
n = 90
def data_gen():
    tlist = np.linspace(0, 2 * np.pi / w, n)
    for t in tlist:
        x, y = orbit_path(t, a, b, w)
        yield x, y


        def init():
            ax.set_ylim(-30, 30)
            ax.set_xlim(-30, 30)
            del xdata[:]
            del ydata[:]
            line.set_data(xdata, ydata)
            return line,


        def orbit_path(t, a, b, w):
            return a * np.cos(w * t), b * np.sin(w * t) #Orbit path


        fig, ax = plt.subplots()
        line, = ax.plot([], [])
        ax.grid()
        xdata, ydata = [], []


        def animate_orbit(data):
            x, y = data
            # xdata.append(x)
            # ydata.append(y)
            xmin, xmax = ax.get_xlim()
            ax.scatter(x, y, c='red')


            if x >= xmax:
                ax.set_xlim(xmin, 2 * xmax)
                ax.figure.canvas.draw()
                ax.scatter(x, y)




