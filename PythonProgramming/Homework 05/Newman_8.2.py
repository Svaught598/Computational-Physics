"""
Newman Problem 8.2

Lotka Volterra Equations
"""
from math import sin
import numpy as np
import matplotlib.pyplot as plt

# Constants
alpha = 1
beta = 1
gamma = 1
delta = 2

# Initialization
a = 0.0
b = 30.0
N = 10000
h = (b-a)/N
tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []
x = y = 2.0

# Function declaration
dxdt = lambda x, y: alpha*x - beta*x*y
dydt = lambda x, y: gamma*x*y - delta*y

# Main Loop
for t in tpoints:
    xpoints.append(x)
    ypoints.append(y)
    xk1, yk1 = h*dxdt(x, y), h*dydt(x, y)
    xk2, yk2 = h*dxdt(x+0.5*xk1, y+0.5*yk1), h*dydt(x+0.5*xk1, y+0.5*yk1)
    xk3, yk3 = h*dxdt(x+0.5*xk2, y+0.5*yk2), h*dydt(x+0.5*xk2, y+0.5*yk2)
    xk4, yk4 = h*dxdt(x+xk3, y+yk3), h*dydt(x+xk3, y+yk3)
    x += (xk1+2*xk2+2*xk3+xk4)/6
    y += (yk1+2*yk2+2*yk3+yk4)/6

# Plotting Populations with Time
plt.plot(tpoints,xpoints, label='Rabbits')
plt.plot(tpoints,ypoints, label='Foxes')
plt.xlabel("t")
plt.ylabel("Population (in 1000s)")
plt.legend()
plt.show()

# Plotting populations by each other
plt.plot(xpoints, ypoints)
plt.xlabel("Rabbit Population")
plt.ylabel("Fox Population")
plt.show()


