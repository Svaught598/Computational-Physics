"""
Problem 1 

Terminal Velocity
"""
import numpy as np
import matplotlib.pyplot as plt


# Declare constants
a = 10
b = 1
v_init_1 = 1
v_init_50 = 50

# diff eq function
def func(v):
    return a - b*v

# euler method
def euler(func, v0, a, b, N):
    
    # setup
    h = (b-a)/N
    v = v0
    tpoints = np.arange(a, b, h)
    vpoints = []
    
    # actual euler method
    for t in tpoints:
        vpoints.append(v)
        v += h*func(v)
        
    return tpoints, vpoints

# Function calls and plotting
ts, vs = euler(func, v_init_1, 0, 20, 1000)
plt.plot(ts, vs, label='Initial V=1 m/s')

ts, vs = euler(func, v_init_50, 0, 20, 1000)
plt.plot(ts, vs, label='Initial V=50 m/s')

plt.title('Terminal Velocity')
plt.legend()
plt.show()