"""
Newman Problem 8.15

The Double Pendulum
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi


# Constants
g = 9.81 
l = 0.4
t0 = 0
tf = 100
N = 10000.


""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++"""

def rk4(r_init, func, tpoints):
    '''rk4 in a function. simple.'''

    # function initialization
    h = tpoints[2] - tpoints[1]
    r = r_init
    o1points, o2points = [], []
    w1points, w2points = [], []
    epoints = []

    for t in tpoints:
        # adding new angles
        o1points.append(r[0])
        o2points.append(r[1])

        # adding new velocities
        w1points.append(r[2])
        w2points.append(r[3])

        # adding energy
        epoints.append(
            .5*1*(r[2]**2 + r[3]**2) - g*l*(2*cos(r[0]) + cos(r[1]))
        )

        # calculating next point with RK4
        k1 = h*func(r)
        k2 = h*func(r+0.5*k1)
        k3 = h*func(r+0.5*k2)
        k4 = h*func(r+k3)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    return (
        o1points,
        o2points,
        w1points,
        w2points,
        epoints
    )


def function(r):
    # unpacking r vector
    O1 = r[0]
    O2 = r[1]
    w1 = r[2]
    w2 = r[3]

    # setting new angles
    ft1 = w1
    ft2 = w2

    # setting new angular velocities
    fo1 = -(w1**2*sin(2*O1-2*O2) + 2*w2**2*sin(O1 - O2) + g/l*(sin(O1 - 2*O1) + 3*sin(O1)))/(
        3 - cos(2*O1 - 2*O2)
    ) 
    fo2 = (4*w1**2*sin(O1 - O2) + w2**2*sin(2*O1 - 2*O2) + 2*g/l*(sin(2*O1 - O2) - sin(O2)))/(
        3 - cos(2*O1 - 2*O2)
    )

    return np.array([ft1, ft2, fo1, fo2], float)


# initial conditions and functions calls
h = (tf-t0)/N
t = np.arange(t0, tf, h)
R = np.array([pi/2., pi/2., 0, 0], float)
theta1,theta2,_,_,epoints = rk4(R, function, t)

# plotting stuff
plt.plot(t, epoints)
plt.show()

plt.plot(t, theta1)
plt.plot(t, theta2)
plt.show()

# estimating variation in energy
print(f'Variance is about ~{epoints[-1] - epoints[0]:0.3e} Joules')

""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++"""
from vpython import sphere, cylinder, rate, vector

# Pendulum declaration with VPython objects
s1 = sphere(pos=vector(1,0,0), radius=0.1)
c1 = cylinder(radius=0.05)
s2 = sphere(pos=vector(2,0,0), radius=0.1)
c2 = cylinder(radius=0.05)

# only display every 4 RK steps
for t1, t2 in zip(theta1, theta2):

    # screen update every 30th of a second
    rate(30)
    
    # update position of top pendulum
    x = -cos(t1)
    y = sin(t1)
    s1.pos = vector(y, x, 0)
    c1.axis = vector(y, x, 0)
    c2.pos = vector(y, x, 0)

    # update position of bottom pendulum
    cx, cy = -cos(t2), sin(t2)
    x += cx
    y += cy
    s2.pos = vector(y, x, 0)
    c2.axis = vector(cy, cx, 0)
