"""
Newman Problem 5.6

Checking if trapezoid rule error follows equation
"""
import numpy as np


def function(x):
  return x**4 - 2*x + 1


def error(first_estimate, second_estimate):
    return abs(second_estimate - first_estimate)/3.


def integrate(func, x, N):
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


integral_one = integrate(function, 2, 10)
integral_two = integrate(function, 2, 20)
err1 = error(integral_one, integral_two)
err2 = abs(integral_two - 4.4)
print(f"Calculated Error: {err1}")
print(f"Actual Error: {err2}")





