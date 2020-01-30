"""
Newman Problem 5.9

Heat capacity of a solid
"""
import numpy as np
from gaussxw import gaussxw
import matplotlib.pyplot as plt


def integrand(x):
    return (x**4 * np.exp(x))/(np.exp(x) - 1)**2


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
        integral += wp[k]*func(xp[k])

    return integral


def cv(T):
    constants = 9*0.001*6.022*1.e28*1.38*1.e-23*(T/428)**3
    integral = gaussian_quadrature(integrand, 0, 428./T,50)
    
    heat_capacity = constants*integral
    return heat_capacity


ts = np.linspace(5, 500, 100)
cvs = [cv(t) for t in ts]

plt.plot(ts, cvs)
plt.title("Heat Capacity of a Solid at \nVarious temperatures")
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity (J/K)")
plt.show()