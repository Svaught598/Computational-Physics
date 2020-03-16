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
m = 5.972*1.e24                     # kg
p_vel = 3.0287*1.e4*3.1709*1.e8     # m/year
p_dis = 1.4710*1.e11                # m
h = 0.000114155                     # 1 hour in years


""" Part A ++++++++++++++++++++++++++++++++++++++++++++++"""

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
    vxpoints, vypoints = [], []

    # calculate half steps
    vx_mid = r[2] + h*f(r)[2]/2.
    vy_mid = r[3] + h*f(r)[3]/2.

    for t in tpoints:
        # adding new positions and velocities
        xpoints.append(r[0])
        ypoints.append(r[1])
        vxpoints.append(r[2])
        vypoints.append(r[3])

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

    return xpoints, ypoints, vxpoints, vypoints


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
xpoints, ypoints, vxpoints, vypoints = verlet(function, 0, 4)

# Plotting
plt.plot(xpoints, ypoints)
plt.show()

""" Part B ++++++++++++++++++++++++++++++++++++++++++++++"""

def verlet_energy(f, t0, tf):
    '''verlet method in a function
    
    returns tuple:
        (xpoints, ypoints, vxpoints, vypoints)
    '''
    # function initialization
    tpoints = np.arange(t0,tf,h)
    r = np.array([p_dis, 0, 0, p_vel], float)

    # empty lists for each timestep value
    xpoints, ypoints = [], []
    potential, kinetic = [], []

    # calculate half steps
    vx_mid = r[2] + h*f(r)[2]/2.
    vy_mid = r[3] + h*f(r)[3]/2.

    for t in tpoints:
        # adding new positions and energies
        xpoints.append(r[0])
        ypoints.append(r[1])
        potential.append(-G*M*m/sqrt(r[0]**2 + r[1]**2)/(3.1709*1.e8)**2)
        kinetic.append(.5*m*(r[2]**2 + r[3]**2)/(3.1709*1.e8)**2)

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

    return xpoints, ypoints, kinetic, potential, tpoints


# initialization of earth at Perihelion & call to Verlet method
_,_, potential, kinetic, tpoints = verlet_energy(function, 0, 4)
ttl_energy = np.array(potential, float) + np.array(kinetic, float)

# Plotting
plt.plot(tpoints, potential, label='potential')
plt.plot(tpoints, kinetic, label='kinetic')
plt.plot(tpoints, ttl_energy, label = 'total')
plt.title('Potential, Kinetic, & Total Energy of Earths Orbit')
plt.legend()
plt.show()

""" Part C ++++++++++++++++++++++++++++++++++++++++++++++"""

plt.plot(tpoints, ttl_energy, label = 'total')
plt.title('Total Energy (Conserved in Long Term)')
plt.legend()
plt.show()