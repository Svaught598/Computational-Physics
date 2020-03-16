"""
Newman Problem 8.9

Vibration in 1-D System
"""
import numpy as np
import matplotlib.pyplot as plt
from math import cos


class RungeKuttaSolver:

    def __init__(self, func, N=5):
        self.function = func
        self.r = np.zeros(N*2, float)
        self.h = 1000
        self.tpoints = np.linspace(0, 20, 1000)
        self.xmatrix = np.empty(self.tpoints.shape+self.r.shape, float)

    def solve(self):
        for i, e in enumerate(self.tpoints):
            # adding new position for each mass
            h = self.h
            func = self.function
            r = self.r
            self.xmatrix[i] = r

            # calculating next point with RK4
            k1 = h*func(self.r, e)
            k2 = h*func(self.r+0.5*k1, e+0.5*h)
            k3 = h*func(self.r+0.5*k2, e+0.5*h)
            k4 = h*func(self.r+k3, e+h)
            self.r += (k1 + 2*k2 + 2*k3 + k4)/6

    def display(self):
        for xpoints in self.xmatrix.transpose():
            plt.plot(self.tpoints, xpoints)
        plt.show()


def function(r, t):
    # unpack argument vector
    N = len(r)//2
    xs = r[:N]
    vs = r[N:]

    # create return array and set new elements
    new_r = np.empty(r.shape, float)
    new_r[:N] = vs
    new_r[N] = k*(xs[1] - xs[0])/m + cos(omega*t)/m
    new_r[-1] = k*(xs[-2] - xs[-1])/m 
    for i in range(N-1):
        new_r[i+N] = k*(xs[i+1] - xs[i])/m + k*(xs[i-1] - xs[i])/m

    # return statement
    return np.array(new_r, float)


# Set Constants
m = 1
k = 6
omega = 2

rks = RungeKuttaSolver(function)
rks.solve()
rks.display()

