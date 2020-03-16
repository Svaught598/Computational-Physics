"""
Newman Problem 8.4

Nonlinear Pendulum
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi

""" Part A +++++++++++++++++++++++++++++++++++++++++++++++++"""

# constant declaration
g = 9.81
l = 0.1

def f(r):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return np.array([ftheta, fomega], float)

# Initialization
A = 0.0
B = 15.0
N = 10000
h = (B - A)/N

tpoints = np.arange(A,B,h)
theta_pts = []
omega_pts = []
r = np.array([179./180.*pi, 0], float)

# Main Loop
for t in tpoints:
    # adding new point to each list
    theta_pts.append(r[0])
    omega_pts.append(r[1])

    # calculating next point with RK4
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    r += (k1 + 2*k2 + 2*k3 + k4)/6

# Plotting theta vs. time
plt.plot(tpoints, theta_pts)
plt.show()

""" Part B +++++++++++++++++++++++++++++++++++++++++++++++++"""
from vpython import sphere, cylinder, rate, vector
from math import cos, sin, pi
from numpy import arange

# Pendulum declaration with VPython objects
s = sphere(pos=vector(1,0,0), radius=0.1)
c = cylinder(radius=0.05)

# only display every 4 RK steps
for theta in theta_pts[::4]:
    
    # screen update every 30th of a second
    rate(30)
    
    # update positions
    x = -cos(theta)
    y = sin(theta)
    s.pos = vector(y, x, 0)
    c.axis = vector(y, x, 0)
