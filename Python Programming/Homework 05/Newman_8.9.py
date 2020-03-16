"""
Newman Problem 8.9

Vibration in 1-D System
"""
import numpy as np
import matplotlib.pyplot as plt
from math import cos


# setting constnats
m = 1
k = 6
omega = 2
pts = 5

""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

def rk4(r_init, func, t0, t, N):
    '''rk4 in a function. simple.'''

    # function initialization
    h = (t-t0)/N
    tpoints = np.arange(t0,t,h)
    xmatrix = np.empty(tpoints.shape+r_init.shape, float)
    r = r_init

    for i, e in enumerate(tpoints):
        # adding new position for each mass
        xmatrix[i] = r

        # calculating next point with RK4
        k1 = h*func(r, e)
        k2 = h*func(r+0.5*k1, e+0.5*h)
        k3 = h*func(r+0.5*k2, e+0.5*h)
        k4 = h*func(r+k3, e+h)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    return xmatrix, tpoints

        
def function(r, t):
    '''
    iterates to next diff eq. value 
    used with rk4
    '''
    # unpack argument vector
    N = len(r)//2
    xs = r[:N]
    vs = r[N:]

    # create return array and set new elements
    new_r = np.empty(r.shape, float)

    # new positions
    new_r[:N] = vs 

    # new end velocities
    new_r[N] = k*(xs[1] - xs[0])/m + cos(omega*t)/m
    new_r[-1] = k*(xs[-2] - xs[-1])/m 

    # new middle velocities
    for i in range(1, N-1):
        new_r[i+N] = k*(xs[i+1] - xs[i])/m + k*(xs[i-1] - xs[i])/m

    # return statement
    return np.array(new_r, float)


def display(solutions, tpoints):
    '''displays all solutions in a plot'''
    print(solutions[0].shape)
    for i in range(pts):
        xi = solutions[:,i]
        plt.plot(tpoints, xi)
    plt.show()


# calling functions and plotting
r = np.zeros(2*pts, float)
solutions, tpoints = rk4(r, function, 0, 20, 1000)
display(solutions, tpoints)


""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
from vpython import sphere, vector, rate


# generate spheres for animation
objects = []
sep = 2
length = pts*sep
for i in range(pts):
    rest_pos = sep*i - (length - sep)/2
    objects.append(sphere(pos = vector(rest_pos, 0, 0), radius=0.1))

# animate stuff
for i in range(len(solutions)):
    rate(10)
    for j in range(pts):
        rest_pos = sep*j - (length - sep)/2
        objects[j].pos = vector(rest_pos + solutions[i][j], 0, 0)
