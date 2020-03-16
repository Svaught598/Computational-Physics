"""
Newman Problem 8.12

Orbit of the Earth
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi


# constants
# stuff converted to years
G = 6.6738*1.e-11*(3.1709*1.e8)**2  # m^3/kg/year^2
M = 1.9891*1.e30                    # kg
p_vel = 3.0287*1.e4*3.1709*1.e8     # m/year
p_dis = 1.4710*1.e11                # m
h = 0.000114155                     # 1 hour in years


def verlet(f, t0, tf):
    '''verlet method in a function
    
    returns tuple:
        (xpoints, ypoints, vxpoints, vypoints)
    '''
    # function initialization
    tpoints = np.arange(t0,tf,h)
    r = np.array([p_dis, 0, 0, p_vel], float)

    # empty lists for each timestep value
    xpoints, ypoints = [], []
    #vxpoints, vypoints = [], []

    # calculate half steps
    vx_mid = r[2] + h*f(r)[2]/2.
    vy_mid = r[3] + h*f(r)[3]/2.

    for t in tpoints:
        # adding new positions and velocities
        xpoints.append(r[0])
        ypoints.append(r[1])

        # calculate positions
        r[0] += h*vx_mid
        r[1] += h*vy_mid

        # calculate k
        k = h*f(r)

        # calculate velocities
        r[2] = vx_mid + k[2]/2.
        r[3] = vy_mid + k[3]/2.

        # update half steps
        vx_mid += k[2]
        vy_mid += k[3]

    return xpoints, ypoints


def function(r):
    '''
    iterates to next diff eq. value 
    used with verlet method

    returns array:
        [x, y, vx, vy]
    '''
    # unpack argument vector
    x, y = r[0], r[1]
    vx, vy = r[2], r[3]

    # new positions
    fx, fy = vx, vy

    # new velocities
    denom = sqrt(x*x + y*y)**3
    fvx = -G*M*x/denom
    fvy = -G*M*y/denom

    # return statement
    return np.array([fx, fy, fvx, fvy], float)


# initialization of earth at Perihelion & call to Verlet method
xpoints, ypoints = verlet(function, 0, 4)

# Plotting
plt.plot(xpoints, ypoints)
plt.show()

