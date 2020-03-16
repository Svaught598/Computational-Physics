"""
Newman Problem 8.7

Trajectory with Air Resistance
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt

""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++"""

# constant declaration
m = 1
R = 0.08
rho = 1.22
c = 0.47
v = 100
theta = 30*pi/180.
g = 9.81

def func(r):
    # unpacking array
    x, y = r[0], r[1]
    vx, vy = r[2], r[3]

    # intermediate calculations
    _v = sqrt(vx*vx + vy*vy)
    _f = 1/2*pi*R**2*rho*c*_v

    # New values and return array
    fx, fy = vx, vy
    fvx = -_f*vx*_v/m
    fvy = -_f*vy*_v/m - g
    return np.array([fx, fy, fvx, fvy], float)

# Initialization
A = 0.0
B = 5
N = 1000
h = (B - A)/N

tpoints = np.arange(A,B,h)
xpoints = []
ypoints = []
vxpoints = []
vypoints = []
r = np.array([0, 0, v*cos(theta), v*sin(theta)], float)

# Main Loop
for t in tpoints:
    # adding new point to each list
    xpoints.append(r[0])
    ypoints.append(r[1])
    vxpoints.append(r[2])
    vypoints.append(r[3])

    # calculating next point with RK4
    k1 = h*func(r)
    k2 = h*func(r+0.5*k1)
    k3 = h*func(r+0.5*k2)
    k4 = h*func(r+k3)
    r += (k1+2*k2+2*k3+k4)/6.

    # break loop when projectile reaches y=0
    if r[1] < 0:
        break

# plotting and stuff
plt.plot(xpoints, ypoints)
plt.title('Projectile (m = 1)')
plt.show()
print(f'Distance travelled is ~ {xpoints[-1]:0.2f} meters')


""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++"""

# Initialization
A = 0.0
B = 10
N = 1000
h = (B - A)/N

# Function redefined to take mass as argument
def func(r, m):
    # unpacking array
    x, y = r[0], r[1]
    vx, vy = r[2], r[3]

    # intermediate calculations
    _v = sqrt(vx*vx + vy*vy)
    _f = 1/2*pi*R**2*rho*c*_v

    # New values and return array
    fx, fy = vx, vy
    fvx = -_f*vx*_v/m
    fvy = -_f*vy*_v/m - g
    return np.array([fx, fy, fvx, fvy], float)

''' Plot solution for a bunch of masses '''

for m in np.arange(.5, 5, .05):

    # initialization
    xpoints = []
    ypoints = []
    r = np.array([0, 0, v*cos(theta), v*sin(theta)], float)

    # RK4 Loop
    for t in tpoints:
        # adding new point to each list
        xpoints.append(r[0])
        ypoints.append(r[1])

        # calculating next point with RK4
        k1 = h*func(r, m)
        k2 = h*func(r+0.5*k1, m)
        k3 = h*func(r+0.5*k2, m)
        k4 = h*func(r+k3, m)
        r += (k1+2*k2+2*k3+k4)/6.

        # break loop when projectile reaches y=0
        if r[1] < 0:
            break

    # plotting and stuff
    plt.plot(xpoints, ypoints)

'''Plot solution for one really big mass'''

# initialization
xpoints = []
ypoints = []
r = np.array([0, 0, v*cos(theta), v*sin(theta)], float)

# RK4 Loop
for t in tpoints:
    # adding new point to each list
    xpoints.append(r[0])
    ypoints.append(r[1])

    # calculating next point with RK4
    k1 = h*func(r, 50)
    k2 = h*func(r+0.5*k1, 50)
    k3 = h*func(r+0.5*k2, 50)
    k4 = h*func(r+k3, 50)
    r += (k1+2*k2+2*k3+k4)/6.

    # break loop when projectile reaches y=0
    if r[1] < 0:
        break

# plotting and stuff
plt.plot(xpoints, ypoints)
    
# show the results
plt.title('Different Masses & One Really Large Mass')
plt.show()
print('Larger masses travel further')
print('This makes sense because deceleration is inversely proportional to mass')

