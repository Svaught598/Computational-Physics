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
phi = np.ones([M+1,M+1],float)
phi[1,:] = Vplus
delta = 0

# break when we reach target accuracy
while delta > target:
    
    # Updating Potential
    for i in range(1,M):
        for j in range(1,M):
            difference = (phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])/4 - phi[i,j]
            phi[i,j] = phi[i,j] + (1 + omega)*difference

            # updating delta
            if difference > delta: 
                delta = difference


# Plotting Stuff
plt.imshow(phi)
plt.gray()
plt.show()
