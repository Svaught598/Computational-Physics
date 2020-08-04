"""
Problem 6

Random Walk in 3D
"""
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class RandWalk3D:
    
    def __init__(self, n_walkers, n_steps):
        self.n_walkers = n_walkers
        self.walkers = np.zeros((3, n_walkers), float)
        self.avg2_list = []
        self.n_steps = n_steps
        self.n_iter = 0
        
    def iterate(self):
        """update the random walk"""
        while self.n_iter < self.n_steps:
            # generate random steps & add to current walker coords.
            x = ran.randint(-100, 101, self.n_walkers)
            y = ran.randint(-100, 101, self.n_walkers)
            z = ran.randint(-100, 101, self.n_walkers)
            r = np.sqrt(x*x + y*y + z*z)
            self.walkers[0] += x/r
            self.walkers[1] += y/r
            self.walkers[2] += z/r
            
            # call to check borders, calculate entropy, & increment counter
            self.calc_average()
            self.n_iter += 1
            
    def calc_average(self):
        """calculates the average distance squared of the system"""
        x = self.walkers[0]
        y = self.walkers[1]
        z = self.walkers[2]
        r = x*x + y*y + z*z
        avg2 = np.sum(r)/self.n_walkers
        self.avg2_list.append(avg2)
        
    def plot(self):
        """plots the walkers & entropy"""
        # plotting the walkers
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(self.walkers[0], self.walkers[1], self.walkers[2])
        plt.title(f"3D Random Walk ({self.n_iter} steps)")
        plt.show()
        
        # plotting the average squared
        plt.plot(self.avg2_list)
        plt.title("Average Distance Squared")
        plt.xlabel("Number of Steps")
        plt.show()
    
    
    
# putting it all together
sim = RandWalk3D(1000, 5000)
sim.iterate()
sim.plot()

# Approximating D 
rise = sim.avg2_list[-1]
run = sim.n_iter
D = rise/run
print(f"D is approximately ~{D:0.3f}")