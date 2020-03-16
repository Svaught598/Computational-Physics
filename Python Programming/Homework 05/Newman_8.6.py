"""
Newman Problem 8.6

Harmonic and Anharmonic Oscillators
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi


def runge_kutta(r, f, tpoints):
    """RK4 as a function so code isn't repetitive"""
    xpoints = []
    vpoints = []
    for t in tpoints:
        # adding new point to each list
        xpoints.append(r[0])
        vpoints.append(r[1])

        # calculating next point with RK4
        k1 = h*f(r)
        k2 = h*f(r+0.5*k1)
        k3 = h*f(r+0.5*k2)
        k4 = h*f(r+k3)
        r += (k1 + 2*k2 + 2*k3 + k4)/6  

    return xpoints, vpoints

""" Part A +++++++++++++++++++++++++++++++++++++++++++++++++"""

# constant declaration
omega = 1

# function definition for harmonic oscillator
def harmonic(r):
    x = r[0]
    v = r[1]
    fx = v
    fv = -omega*omega*x
    return np.array([fx, fv], float)

# Initialization
A = 0.0
B = 50.0
N = 10000
h = (B - A)/N

# declaring variables and RK4 call
tpoints = np.arange(A,B,h)
r = np.array([1, 0], float)
xpoints, vpoints = runge_kutta(r, harmonic, tpoints)

# Plotting xpoints vs. time
plt.plot(tpoints, xpoints)
plt.title('Part A')
plt.show()
print("Period looks to be about ~ 6")

""" Part B +++++++++++++++++++++++++++++++++++++++++++++++++"""

# variable declaration and RK4 call
r = np.array([2, 0], float)
xpoints, vpoints = runge_kutta(r, harmonic, tpoints)

# Plotting xpoints vs. time
plt.plot(tpoints, xpoints)
plt.title('Part B')
plt.show()
print('Period still looks to be about ~ 6')

""" Part C.1 +++++++++++++++++++++++++++++++++++++++++++++++++"""

# function defined for anharmonic oscillator
def anharmonic(r):
    x = r[0]
    v = r[1]
    fx = v
    fv = -omega*omega*x*x*x
    return np.array([fx, fv], float)

# variable declaration and RK4 call
r = np.array([1, 0], float)
xpoints, vpoints = runge_kutta(r, anharmonic, tpoints)

# Plotting xpoints vs. time
plt.plot(tpoints, xpoints)
plt.title('Part C.1')
plt.show()
print("Period looks to be about ~ 7")

""" Part C.2 +++++++++++++++++++++++++++++++++++++++++++++++++"""

# variable declaration and RK4 call
r = np.array([2, 0], float)
xpoints, vpoints = runge_kutta(r, anharmonic, tpoints)

# Plotting theta vs. time
plt.plot(tpoints, xpoints)
plt.title('Part C.2')
plt.show()
print('Period looks to be about ~ 3.5 now')
print('The oscillator is oscillating faster at higher amplitudes')

""" Part D +++++++++++++++++++++++++++++++++++++++++++++++++"""

# Plotting v vs. time
plt.plot(xpoints, vpoints)
plt.title('Phase Space (Anharmonic Oscillator)')
plt.show()

""" Part E +++++++++++++++++++++++++++++++++++++++++++++++++"""

# constant declaration
mu = 1

# function definition for Van Der Pol Oscillator
def van_der_pol(r):
    x = r[0]
    v = r[1]
    fx = v
    fv = mu*(1-x*x)*v - omega*omega*x
    return np.array([fx, fv], float)

# Initialization
A = 0.0
B = 20.0
N = 10000
h = (B - A)/N

''' Mu = 1'''

# variable declaration and RK4 call
tpoints = np.arange(A,B,h)
r = np.array([1, 0], float)
xpoints, vpoints = runge_kutta(r, van_der_pol, tpoints)

# Plotting phasespace
plt.plot(xpoints, vpoints)
plt.title('Part E: Phase Space (mu = 1)')
plt.show()

''' Mu = 2'''

# variable declaration and RK4 call
mu = 2
r = np.array([1, 0], float)
xpoints, vpoints = runge_kutta(r, van_der_pol, tpoints)

# Plotting phasespace
plt.plot(xpoints, vpoints)
plt.title('Part E: Phase Space (mu = 2)')
plt.show()

''' Mu = 4'''

# variable declaration and RK4 call
mu = 4
r = np.array([1, 0], float)
xpoints, vpoints = runge_kutta(r, van_der_pol, tpoints)

# Plotting phasespace
plt.plot(xpoints, vpoints)
plt.title('Part E: Phase Space (mu = 4)')
plt.show()
