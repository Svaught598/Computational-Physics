"""
Newman 9.2

Gauss-Seidel & Overrelaxation
"""
import numpy as np
import matplotlib.pyplot as plt


# Constant Declaration
M = 100
a = 0.01
e0 = 1.0
Vplus = 1.0
target = 1.e-6
delta = 1.0
omega = 0.9

# Initialization
phi = np.zeros([M+1,M+1],float)
phi[0,:] = Vplus

# break when we reach target accuracy
while delta > target:
    
    delta = 0
    # Updating Potential
    for i in range(1,M):
        for j in range(1,M):
            diff = (phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])/4 - phi[i,j]
            phi[i,j] = phi[i,j] + (1 + omega) * diff

            # updating delta
            if diff > delta:
                delta = diff


# Plotting Stuff
plt.imshow(phi)
plt.gray()
plt.show()
