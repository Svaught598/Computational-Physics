"""
Newman Problem 5.7

Adaptive trapezoidal rule and Romberg integration
"""
import numpy as np


def funcion(x):
    return (np.sin(10*np.sqrt(x))**2)


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
    if N 
    for i in np.linspace(h, x-h, N-2):
        integral += h*func(i)
    return integral


def adaptive_trapezoidal(func, x):
    error = 0
    estimate_1 = 0
    estimate_2 = 0
    while error > 1.e-6:
        try: