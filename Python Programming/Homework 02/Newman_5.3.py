import numpy as np
import matplotlib.pyplot as plt


""" Part A ----------------------------------------------------"""

def gaussian(t):
    return np.exp(-t*t)


def integrate_zero_to_x(func, x, N):
    """Uses trapezoidal rule to estimate integral
    from zero to x for function provided

    args:
        - func: function to be integrated
        - x: upper limit of integration
        - N: number of slices
    """
    # Trapezoid width & integration for edges
    h = x/N
    integral = .5*h*(func(0) + func(x))

    # rest of integral
    for i in np.linspace(h, x-h, N-2):
        integral += h*func(i)
    return integral

y_list = []
x_list = np.arange(0, 3.1, 0.1)

for i in x_list:
    y_list.append(integrate_zero_to_x(gaussian, i, 100))

plt.plot(x_list, y_list, "k.")
plt.title("Part A")
plt.show()

""" Part B ----------------------------------------------------"""

def gaussian(t):
    return np.exp(-t*t)


def integrate_zero_to_x(func, x, N):
    """Uses trapezoidal rule to estimate integral
    from zero to x for function provided

    args:
        - func: function to be integrated
        - x: upper limit of integration
        - N: number of slices
    """
    # Trapezoid width & integration for edges
    h = x/N
    integral = .5*h*(func(0) + func(x))

    # rest of integral
    for i in np.linspace(h, x-h, N-2):
        integral += h*func(i)
    return integral

y_list = []
x_list = np.arange(0, 3.1, 0.01)

for i in x_list:
    y_list.append(integrate_zero_to_x(gaussian, i, 100))

plt.plot(x_list, y_list, "k.")
plt.ylim(0, 1.1, "b.")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.title("Part B")
plt.show()