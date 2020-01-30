"""
Newman Problem 5.7

Adaptive trapezoidal rule and Romberg integration
"""
import numpy as np


""" Part A =============================================================="""


def function(x):
    return (np.sin(10*np.sqrt(x))**2)


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

 
def adaptive_trapezoidal(func, a, b):
    N = 2
    estimate_initial = 0
    estimate_final = (b-a)/N * (func(a) + func(b))
    error = abs(estimate_final - estimate_initial)/3.

    while error > 1.e-6:
        estimate_initial = estimate_final
        estimate_final = estimate_initial/2. + integrate(func, 0, 1, N)
        error = abs(estimate_final - estimate_initial)/3.
        N *= 2

    return estimate_final, error, N/2

integral, error, N = adaptive_trapezoidal(function, 0, 1)
print("Trapezoid Rule: \n \t")
print(f"The value of the integral is {integral: 0.3f} with error: {error} and N: {N}")


""" Part B =============================================================="""


def function(x):
    return (np.sin(10*np.sqrt(x))**2)


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

 
def romberg(func, a, b):
    N = 2
    i = 1

    estimate_initial = 0
    estimate_final = (b-a)/N * (func(a) + func(b))

    R_table = np.zeros((50, 50))
    R_table[0,0] = estimate_final

    error = abs(estimate_final - estimate_initial)/3.

    while error > 1.e-6:
        estimate_initial = estimate_final
        estimate_final = estimate_initial/2. + integrate(func, 0, 1, N)
        
        R_table[i, 0] = estimate_final
        print_string = ""
        for m in range(i):
            R_table[i,m + 1] = R_table[i,m] + 1/(4**(m + 1) - 1)*(R_table[i,m] - R_table[i - 1,m])
            print_string += f"{R_table[i,m]: 0.7f}"

        print(print_string)
        error = abs(R_table[i,m + 1] - R_table[i - 1,m])

        N *= 2
        i += 1

    return estimate_final, error, N/2

integral, error, N = romberg(function, 0, 1)
print("Romberg Integration: \n \t")
print(f"The value of the integral is {integral: 0.3f} with error: {error} and N: {N}")