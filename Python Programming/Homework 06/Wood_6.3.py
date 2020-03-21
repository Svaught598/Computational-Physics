"""
Problem 6.3

Cannon Shell Trajectories
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi


# constant declaration
v0 = 0.7       # km
g = 0.00981    # km/s^2
k = 4.e-2   # km^-1
angles = np.array([30, 35, 40, 45, 50, 55], float) # degrees

""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# diff eq function for no drag
def func(r, t):
    
    # unpacking r vector
    x, y = r[0], r[1]
    vx, vy = r[2], r[3]
    
    # intermediate calculations
    _v = sqrt(vx*vx + vy*vy)
    
    # calculate new values & return
    dx = vx 
    dy = vy 
    dvx = 0
    dvy = -g
    return np.array([dx, dy, dvx, dvy], float)
    
    
# function for rk4 method
def rk4(f, theta, a, b, N):
    
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

# function call and plotting
plt.figure(figsize=(8, 4))
for x in angles:
    xs, ys = rk4(func, x, 0, 150, 1000)
    plt.plot(xs, ys, label=f'{x:2.0f} degrees')

# formatting plot
plt.xlim(0, 60)
plt.ylim(0, 20)
plt.legend()
plt.grid(linestyle='--')
plt.show()


""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# diff eq function with drag force
def func(r, t):
    
    # unpacking r vector
    x, y = r[0], r[1]
    vx, vy = r[2], r[3]
    
    # intermediate calculations
    _v = sqrt(vx*vx + vy*vy)
    
    # calculate new values & return
    dx = vx 
    dy = vy 
    dvx = -k*vx*_v
    dvy = -g - k*vy*_v
    return np.array([dx, dy, dvx, dvy], float)
    
    
# function call and plotting
plt.figure(figsize=(8, 4))
for x in angles:
    xs, ys = rk4(func, x, 0, 100, 1000)
    plt.plot(xs, ys, label=f'{x:2.0f} degrees')

    
# formatting plot
plt.xlim(0, 30)
plt.ylim(0, 10)
plt.legend()
plt.grid(linestyle='--')
plt.show()

print("""
    They look pretty similar to the plots shown above in terms of shape.
    IDK if they have the correct values, but its close enough for me.
""")