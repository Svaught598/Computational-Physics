"""
Newman 9.3

Electronic Capacitor
"""
import numpy as np
import matplotlib.pyplot as plt


# Constant Declaration
M = 100
a = 0.01
e0 = 1.0
Vplus = 1.0
Vminus = -1.0
target = 1.e-6
delta = 1.0

# Initialization
phi = np.ones([M+1,M+1],float)
phi[20:80,20:21] = Vplus
phi[20:80,79:80] = Vminus
phiprime = np.empty([M+1,M+1],float)


while delta > target:
    
    # Update potential
    phiprime[0,:] = 0.0
    phiprime[M,:] = 0.0
    phiprime[:,0] = 0.0
    phiprime[:,M] = 0.0
    phiprime[1:M,1:M] = (phi[0:M-1,1:M] + phi[2:M+1,1:M] \
                        + phi[1:M,0:M-1] + phi[1:M,2:M+1] \
                        + a*a/e0*phi[1:M,1:M])/4 

    phiprime[20:80,20:21] = Vplus
    phiprime[20:80,79:80] = Vminus
    
    # Calculate max diff. & swap arrays for next iteration
    delta = np.max(abs(phi-phiprime))
    phi, phiprime = phiprime, phi


# Plotting Stuff
plt.imshow(phiprime)
plt.gray()
plt.show()
