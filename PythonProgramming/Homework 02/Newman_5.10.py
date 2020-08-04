"""
Newman Problem 5.10

Period of an anharmonic oscillator
"""
import numpy as np
from gaussxw import gaussxw
import matplotlib.pyplot as plt


""" Part B ========================================================="""


def integrand(x, a):
    V = lambda x: x**4
    return 1/(np.sqrt(V(a) - V(x)))


def gaussian_quadrature(func, a, b, N):
    """Calculate integral of some function from a to b with
    N sample points

    args:
        - func: function to be integrated
        - a: lower limit of integration
        - b: upper limit of integration
        - N: number of sample points
    """

    x, w = gaussxw(N)
    xp = 0.5*(b - a)*x + 0.5*(b + a)
    wp = 0.5*(b - a)*w

    integral = 0.
    for k in range(N):
        integral += wp[k]*func(xp[k], b)

    return integral * np.sqrt(8)


x = np.linspace(0, 2, 100)
periods = [gaussian_quadrature(integrand, 0., i, 20) for i in x]
plt.plot(x, periods)
plt.show()



