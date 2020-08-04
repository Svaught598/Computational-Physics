"""
Newman Problem 5.14

Gravitational pull of a uniform sheet
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw


def integrand(x, y, z):
    return 1/(x*x + y*y + z*z)**1.5


def gaussian_quadrature(func, z, a, b, N):
    """Calculate integral of some function from a to b with
    N sample points

    args:
        - func: function to be integrated
        - z: a constant to be passed to function
        - a: lower limit of integration
        - b: upper limit of integration
        - N: number of sample points
    """

    x, w = gaussxw(N)
    xp = 0.5*(b - a)*x + 0.5*(b + a)
    wp = 0.5*(b - a)*w

    integral = 0.
    for i in range(N):
        for j in range(N):
            integral += wp[i]*wp[j]*func(xp[i], xp[j], z)

    return integral * 6.674*1.e-11 * 100 * z

xs = np.linspace(0, 10, 100)
integrals = [gaussian_quadrature(integrand, i, -5, 5, 100) for i in xs]
plt.plot(xs, integrals)
plt.show()