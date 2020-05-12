import sys


def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points=100):
    import numpy as np
    try:
        x = np.linspace(minimum_x, maximum_x, number_of_points)
    except ArithmeticError:
        if maximum_x < minimum_x:
            print("max_x < min_x.")

    try:
        y = np.polyval(quadratic_coefficients, x)
    except IndexError:
        if number_of_points <= 2:
            print("Index Error")

    fit_curve = np.vstack((x, y)). T
    return fit_curve


if __name__ == '__main__':
    print(fit_curve_array(sys.argv[1]))
