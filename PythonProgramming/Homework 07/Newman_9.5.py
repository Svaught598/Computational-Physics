"""
Newman 9.5

FTCS Solution of the Wave Equation
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


""" Part A +++++++++++++++++++++++++++++++++++++++++++"""


# Constant Declaration
vel = 100.0             # 1 m/s
L = 1.0                 # 1 meter
d = 0.1                 # 10 cm
C = 1.0                 # 1 m/s
N = 200                 # No. of grid divisions
sigma = 0.3             # 30 cm
t = 0.0                 # start time at 0
tmax = 100.0e-3         # total time 1 second
a = L/N                 # spacing


# It took a lot of trial and error to get a timestep that didn't
# immediately explode into chaos
timestep = 5.0005e-5    


# Function Definitions
def fpsi(x):
    exp_part = np.exp(-(x-d)*(x-d)/2/sigma/sigma)
    return C*x*(L - x)/L**2*exp_part


# Initialization
xs = np.linspace(0, L, N+1)
phi = np.zeros(N+1, float)
psi = fpsi(xs)


# Main function
def iterate(phi, psi):
    t = 0.0
    # Main Loop
    while t < tmax:
        # new values of psi & phi & t
        phi[1:N] += timestep*psi[1:N]
        psi[1:N] += timestep*vel**2/(a**2)*(phi[2:N+1] + phi[0:N-1] - 2*phi[1:N])
        t += timestep
        yield phi


""" Part B +++++++++++++++++++++++++++++++++++++++++++"""


# Animation Initialization
fig = plt.figure()
ax = plt.axes(xlim = (0,1), ylim = (-.005,.005))
frame, = ax.plot([],[], lw = 2)

# Addding frames
frame_list = []
for p in iterate(phi, psi):
    frame, = ax.plot(xs, phi, "b")
    frame_list.append([frame,])

# Showing animation
anim = animation.ArtistAnimation(fig, frame_list, interval = 5, blit = True)
plt.show()
   
