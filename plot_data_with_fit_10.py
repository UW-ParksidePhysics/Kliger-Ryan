def plot_data_with_fit(data, fit_curve, data_format=0, fit_format=0):
    import matplotlib.pyplot as plt
    import numpy as np
    un_data = zip(*data)
    data = list(un_data)
    a_x1, a_y1 = np.array(data[0]), np.array(data[1])

    un_fit_curve = zip(*fit_curve)
    fit_curve = list(un_fit_curve)
    a_x2, a_y2 = np.array(fit_curve[0]), np.array(fit_curve[1])
    if data_format == 1:
        plt.plot(a_x1, a_y1, 'r')
    elif data_format == 2:
        plt.plot(a_x1, a_y1, 'y')
    elif data_format == 3:
        plt.plot(a_x1, a_y1, 'b')
    else:
        plt.plot(a_x1, a_y1)

    if fit_format == 1:
        plt.plot(a_x2, a_y2, 'r')
    elif fit_format == 2:
        plt.plot(a_x2, a_y2, 'y')
    elif fit_format == 3:
        plt.plot(a_x2, a_y2, 'b')
    else:
        plt.plot(a_x2, a_y2)

    plt.xlabel("Volume")
    plt.ylabel("Energy")
    return plt.show()