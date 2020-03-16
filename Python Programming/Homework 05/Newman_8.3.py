"""
Newman Problem 8.3

The Lorenz Equations
"""
import numpy as np
import matplotlib.pyplot as plt

# Constants
sigma = 10
r = 28
b = 8/3

# Function Declaration
def function(xyz):
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    fx = sigma*(y - x)
    fy = r*x - y - x*z
    fz = x*y - b*z
    return np.array([fx, fy, fz], float)

# Initialization
A = 0.0
B = 100.0
N = 10000
h = (B - A)/N

tpoints = np.arange(A,B,h)
xpoints = []
ypoints = []
zpoints = []

xyz = np.array([0, 1, 0], float)

# Main Loop
for t in tpoints:
    # adding new point to each list
    xpoints.append(xyz[0])
    ypoints.append(xyz[1])
    zpoints.append(xyz[2])

    # calculating next point with RK4
    k1 = h*function(xyz)
    k2 = h*function(xyz+0.5*k1)
    k3 = h*function(xyz+0.5*k2)
    k4 = h*function(xyz+k3)
    xyz += (k1 + 2*k2 + 2*k3 + k4)/6


plt.plot(tpoints, ypoints)
plt.title('Unpredictable Shit ... Wait, I mean stuff ... o_o')
plt.xlabel('t')
plt.ylabel('y')
plt.show()

plt.plot(zpoints, xpoints)
plt.title('Strange Man Incoming!')
plt.xlabel('z')
plt.ylabel('x')
plt.show()
