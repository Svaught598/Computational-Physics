import numpy as np
import matplotlib.pyplot as plt
import time
from numpy import floor

 
def F(pos,vel,n,nsteps):
    for tstep in range(nsteps-1):
            i = 0
            vel[i] = vel[i] 
            pos[i] = pos[i] + vel[i] * dt
            pos[i] -= floor(pos[i]/L)*L
            if tstep%1 == 0:
                plt.scatter(pos[i,0],pos[i,1],color="b",s=2)
                plt.draw()

# initialize
n = 1         # number of particles
L = 10        # box size
nsteps = 200   # number of time steps
dt = .28        # time step

pos = np.zeros([n,2])
vel = np.zeros([n,2])

plt.figure(figsize=[8,8])
plt.axis([0,L,0,L])
plt.ion()

pos_init = np.array([0,0])   # single particle
vel_init = np.array([-1,-0.31456])   # single particle

pos[0,:] = pos_init[:]
vel[0,:] = vel_init[:]

# Now do the hard work!

t0 = time.time()
F(pos,vel,n,nsteps)
print("Execution time = ",time.time() - t0)

plt.show()