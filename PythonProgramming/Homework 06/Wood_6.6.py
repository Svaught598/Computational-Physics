"""
Problem 6

Crosswind on a Flyball
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# declare constants
v0 = 349 # m/s
wind = 0
no_wind = 0
some_wind = 4.4704


# function for rk4 method
def rk4(func, theta, a, b, N):
    
    # initializtaion
    h = (b-a)/N
    t_rads = theta*pi/180.
    R = np.array([0, 0, 0, 0, v0*cos(t_rads), v0*sin(t_rads)], float)
    
    # empty lists
    tpoints = np.arange(a, b, h)
    xpoints = []
    ypoints = []
    zpoints = []
    z = 1
    
    # rk4 main loop
    for t in tpoints:
        while z >=0:
            xpoints.append(R[0])
            ypoints.append(R[1])
            zpoints.append(R[2])

            # rk4 update for R
            k1 = h*func(R, t)
            k2 = h*func(R+0.5*k1, t+0.5*h)
            k3 = h*func(R+0.5*k2, t+0.5*h)
            k4 = h*func(R+k3, t+h)
            R += (k1 + 2*k2 + 2*k3 + k4)/6.
            z = R[2]
    
    return np.array(xpoints), np.array(ypoints), np.array(zpoints)


# Diff eq function
def flyball(R, t):
    
    # unpacking vector
    x, y, z = R[0], R[1], R[2]
    vx, vy, vz = R[3], R[4], R[5]
    
    # intermediate calculations
    _v = sqrt((vx-wind)**2 + vy**2 + vz**2)
    k = 0.0039 + 0.0058/(1+exp((_v-35)/5.))
    
    # new values and return
    dx = vx 
    dy = vy 
    dz = vz
    dvx = - k*(vx-wind)*_v
    dvy = - k*vy*_v
    dvz = -g - k*vz*_v
    return np.array([dx, dy, dz, dvx, dvy, dvz], float)


""" Everything below this is function call and plotting +++++++++++"""

# some setup for 3d plot
fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')

# do stuff with some wind
wind = some_wind
xs, ys, zs = rk4(flyball, 70, 0, 100, 1000)
wind_vec = np.array([xs[-1], ys[-1]])
ax.plot(xs, ys, zs, label='WE GOT SOME WIND BOYS!!!')

# do stuff without any wind at all
wind = no_wind
xs, ys, za = rk4(flyball, 70, 0, 100, 1000)
no_wind_vec = np.array([xs[-1], ys[-1]])
ax.plot(xs, ys, zs, label="...no wind...")

# find distance between two landing zones
v = wind_vec - no_wind_vec
distance = sqrt(v[0]**2 + v[1]**2)

# Show plot and print some stuff
ax.legend()
plt.show()
print(f'''
    The assumptions here are:
        - initial angle at 70 degrees from horizontal
        - initial speed of flyball is 49 m/s (110 mph)
        
    The difference in distance between the landing area of these two is {distance:0.2f} meters
    That seems pretty far to me
''')