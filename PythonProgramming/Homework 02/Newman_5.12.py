"""
Newman Problem 5.12

The Stefan-Boltzmann Constant
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw
from math import pi


""" Part B ++++++++++++++++++++++++++++++++++++++++++++"""


def function(z):
    numerator = z**3
    denominator_1 = (1 - z)**5
    denominator_2 = (np.exp(z/(1-z)) - 1)
    return numerator/(denominator_1*denominator_2)


def integrate(func, a, b, N):
    """Finds odd slices for adaptive trapezoidal rule

    args:
        - func: function to be integrated
        - a: lower limit of integration
        - b: upper limit of integration
        - N: number of slices
    """
    # Trapezoid width 
    h = (b - a)/N

    # Every odd slice
    new_part = 0
    for i in range(1, N//2 + 1):
        new_part += func(a + (2*i - 1)*h) 
    
    return new_part * h

 
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


integral = gaussian_quadrature(function, 0, 1, 10000)
print(f"The value of the integral is {integral: 0.5f} using Gaussian Quadrature with 10000 sample points")
print("""
    Gaussian Quadrature was chosen as the method of
    integration since it is the only method that doesn't 
    require evaluation at endpoints. With the substitution 
    I used, there is a discontinuity at 1.
    When compared to Wolfram Alpha, this evaluation
    of the integral is accurate to 6 decimal places.
""")


""" Part C ++++++++++++++++++++++++++++++++++++++++++++"""


stefans_constant = integral*(1.38*1.e-23)**4
stefans_constant *= 1/4/pi**2
stefans_constant *= 1/(3*1.e8)**2
stefans_constant *= 1/(1.05457 * 1.e-34)**3

print(f"Stefan-Boltzmann constant is {stefans_constant: 0.5e}")