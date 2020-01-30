"""
Newman Problem 5.8

Adaptive simpsons rule
"""
import numpy as np


""" Part A =============================================================="""


def function(x):
    return (np.sin(10*np.sqrt(x))**2)


def calculate_T(func, a, b, N):
    """Finds odd slices for adaptive simpsons rule

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
    
    return 2/3. * new_part 


def calculate_S(func, a, b, N):
    """Finds even slices for adaptive simpsons rule

    args:
        - func: function to be integrated
        - a: lower limit of integration
        - b: upper limit of integration
        - N: number of slices
    """
    # Trapezoid width
    h = (b - a)/N

    # Every even slice
    new_part = func(a) + func(b)
    for i in range(2, N, 2):
        new_part += 2 * func(a + i*h) 
    
    return 1/3. * new_part 

 
def adaptive_simpsons(func, a, b):
    N = 2

    s = calculate_S(func, a, b, N)
    t = calculate_T(func, a, b, N)
    estimate_initial = 0
    estimate_final = (b-a)/N * (s + 2*t)

    error = abs(estimate_final - estimate_initial)/15.

    while error > 1.e-6:
        N *= 2
        h = (b-a)/N

        estimate_initial = estimate_final
        s = s + t
        t = calculate_T(func, a, b, N)
        estimate_final = h*(s + 2*t)

        error = abs(estimate_final - estimate_initial)/15.

    return estimate_final, error, N

integral, error, N = adaptive_simpsons(function, 0, 1)
print("Trapezoid Rule: \n \t")
print(f"The value of the integral is {integral: 0.3f} with error: {error} and N: {N}")
