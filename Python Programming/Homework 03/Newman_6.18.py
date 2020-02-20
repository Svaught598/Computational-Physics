"""
Newman Problem 6.18

The temperature of a light bulb
"""
from scipy.constants import physical_constants
import scipy.integrate as intg
import numpy as np
import matplotlib.pyplot as plt


""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# constants
k = physical_constants['Boltzmann constant'][0]
c = physical_constants['speed of light in vacuum'][0]
h = physical_constants['Planck constant'][0]

# function to be integrated
integrand = lambda x: x*x*x/(np.exp(x) - 1)

def calc_efficiency(T):
    # limits of visible spectrum
    lower_visible = 400.e-9
    upper_visible = 800.e-9
    
    # limits of integration
    lower = h*c/(upper_visible*k*T)
    upper = h*c/(lower_visible*k*T)
    
    # integration
    integral = intg.quad(integrand, lower, upper)[0]
    return 15./np.pi**4*integral

Ts = [T for T in range(300, 20000, 100)]
Es = [calc_efficiency(T) for T in Ts]

print('Part A')
plt.plot(Ts, Es)
plt.xlabel('Temperature in K')
plt.ylabel('Efficiency')
plt.show()

""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# golden ratio & accuracy
z = (1+np.sqrt(5))/2.
accuracy = 1.e-6

# initial guesses
x1 = 5000.
x4 = x1*2
x2 = x4 - (x4 - x1)/z
x3 = x1 - (x4 - x1)/z

# value of function at four points
f1 = -1* calc_efficiency(x1)
f2 = -1* calc_efficiency(x2)
f3 = -1* calc_efficiency(x3)
f4 = -1* calc_efficiency(x4)

while (x4 - x1) > accuracy:
    if f2 < f3:
        x4, f4 = x3, f3
        x3, f3 = x2, f2
        x2 = x1 + (x4 - x1)/z
        f2 = calc_efficiency(x2)
    else:
        x1, f1 = x2, f2
        x2, f2 = x3, f3
        x3 = x1 + (x4 - x1)/z
        f3 = calc_efficiency(x3)

        
print('Part B')
print(f"the maximum falls at {x1 + x4: 0.2f} K\n")

print('Part C')
print('Since the melting point of Tungsten is 3,695 K, \nthis isn"t practical for obvious reasons')