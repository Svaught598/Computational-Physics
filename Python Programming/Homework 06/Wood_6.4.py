"""
Problem 6.4

Cannon Shells & Variable Air Density
"""
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi, sqrt


# Declare constants
rho_0 = 1.275*1.e9       # kg/km^3
y_0 = 10                 # km
A = 6.5                  # K/km
alpha = 2.5              # no unit
T_0 = 300                # K
v0 = 0.7                 # km/s
k = 4*1.e-2              # km^-1
g = 0.00981              # km/s^2
angles = np.array([35, 45], float) # degrees


# function for rk4 method
def rk4(func, theta, a, b, N):
    
    # initializtaion
    h = (b-a)/N
    t_rads = theta*pi/180.
    R = np.array([0, 0, v0*cos(t_rads), v0*sin(t_rads)], float)
    
    # empty lists
    tpoints = np.arange(a, b, h)
    xpoints = []
    ypoints = []
    
    # rk4 main loop
    for t in tpoints:
        xpoints.append(R[0])
        ypoints.append(R[1])
        
        # rk4 update for R
        k1 = h*func(R, t)
        k2 = h*func(R+0.5*k1, t+0.5*h)
        k3 = h*func(R+0.5*k2, t+0.5*h)
        k4 = h*func(R+k3, t+h)
        R += (k1 + 2*k2 + 2*k3 + k4)/6.
    
    return xpoints, ypoints


# Diff eq function
def no_correction(R, t):
    
    # unpacking vector
    x, y = R[0], R[1]
    vx, vy = R[2], R[3]
    
    # intermediate calculations
    _v = sqrt(vx*vx + vy*vy)
    
    # new values and return
    dx = vx 
    dy = vy 
    dvx = - k*vx*_v
    dvy = -g - k*vy*_v
    return np.array([dx, dy, dvx, dvy], float)


# Diff eq function w/ correction
def correction(R, t):
    
    # unpacking vector
    x, y = R[0], R[1]
    vx, vy = R[2], R[3]
    
    # intermediate calculations
    _v = sqrt(vx*vx + vy*vy)
    rho_ratio = (1 - A*y/T_0)**alpha
    
    # new values and return
    dx = vx 
    dy = vy 
    dvx = - k*vx*_v*rho_ratio
    dvy = -g - k*vy*_v*rho_ratio
    return np.array([dx, dy, dvx, dvy], float)


""" Now the plotting begins! muahahaaa... >=D  +++++++++++++++"""

# declare figsize for canvas
plt.figure(figsize=(8, 4))

# plot solutions for no correction equations
for angle, style in zip(angles, ('g-', 'r-')):
    xs, ys = rk4(no_correction, angle, 0, 100, 1000)
    plt.plot(xs, ys, style, label=f'{angle:2.0f} degrees')
    
# plot solutions for correction equations
for angle, style in zip(angles, ('g.', 'r.')):
    xs, ys = rk4(correction, angle, 0, 100, 1000)
    plt.plot(xs, ys, style, label=f'{angle:2.0f} degrees w/ correction')
    
# Format plot and show!
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('Trajectories of Cannonballs with (& without)\n Air Density Corrections')
plt.xlim(0, 30)
plt.ylim(0, 10)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()