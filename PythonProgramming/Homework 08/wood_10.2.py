"""
Problem 2

Hypersphere Volume
"""
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt


# main function definition
def multisphere_volume(n_dims, n_samples, radius = 1):
    
    # initialize some working params
    n_iter = 0
    points = 0
    
    while n_iter < n_samples:
        # generate random point in space & inc. iteration count 
        r_list = ran.random(n_dims)
        n_iter += 1
        
        # add point if inside sphere
        if np.sum(r_list**2) < 1:
            points += 1
            
    return 2**n_dims/n_iter*points


# function calling & plotting
dim_list = [i for i in range(1, 11)]
vol_list = [multisphere_volume(dim, 100000) for dim in dim_list]
plt.plot(dim_list, vol_list)
plt.title("Volumes of Multidimensional Spheres (r = 1)")
plt.xlim(0,11)
plt.ylim(0,6)
plt.xlabel("Number of Dimensions")
plt.ylabel("Volume")
plt.show()


# printing everything
for dim, vol in zip(dim_list, vol_list):
    print(f"{dim}-dimensions")
    print(f"calculated volume: {vol:0.3f}\n")
