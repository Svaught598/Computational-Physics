"""
Newman 9.7

The Relaxation Method for Ordinary Differential Equations
"""
import numpy as np
import matplotlib.pyplot as plt


# Constant Declaration
m = 1           # kg
g = 9.81        # m/s^2
tstart = 0      # seconds
tstop = 10      # seconds
N = 100         # number of points
eps = 1.e-6     # desired accuracy
timestep = (tstop - tstart)/N


# Initialization
ts = np.linspace(tstart, tstop, N+1)
xs = np.zeros(N+1, float)


# Function Definition
def iterate(xlist):
    diff = 1
    xs = xlist
    new_xs = np.empty(N+1, float)

    # Loop until desired accuracy
    while diff > eps:
        new_xs[0] = 0
        new_xs[1:N] = (g*timestep*timestep + xs[2:N+1] + xs[0:N-1])/2

        # calc new diff & switch values
        diff = np.max(np.abs(new_xs - xs))
        new_xs, xs = xs, new_xs

    return new_xs


# Plotting stuff
plt.plot(ts, iterate(xs), label = "Trajectory of Ball")
plt.xlabel("Time")
plt.ylabel("Height")
plt.show()

    

