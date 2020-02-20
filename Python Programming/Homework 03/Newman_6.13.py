'''
Newman Problem 6.13

Wien's displacement Constant
'''
import numpy as np
from scipy.constants import physical_constants
from math import exp

h, _, _ = physical_constants['Planck constant']
k_b, _, _ = physical_constants['Boltzmann constant']
c, _, _ = physical_constants['speed of light in vacuum']

""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

def binary_search(func, a, b):
    error = 1.
    x1 = a
    x2 = b
    while error > 1.e-6:
        # different signs
        if func(x1)*func(x2) < 0:
            xprime = .5*(x1 + x2)
            fprime = func(xprime)
            if fprime*func(x1) < 0:
                x2 = xprime
                continue
            elif fprime*func(x2) < 0:
                x1 = xprime
                continue   
        else:
            raise Exception('Binary search cannot detect zero in interval')
        error = abs(x2 - x1)
    return .5*(x1 + x2)


function = lambda x: 5*exp(-x) + x - 5

root = binary_search(function, 1, 10)
constant = h*c/(k_b*root)
print('Part B')
print(f"Wien's constant is {constant:0.5f}\n")

""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

wavelength = 502*1.e-9
T = constant / wavelength
print('Part C')
print(f'The estimated surface temperature is: {T:0.1f} K')
print(f'Actual temperature of the sun is:     5778 K')