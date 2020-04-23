"""
Problem 5

Entropy 2: Electric Boogaloo
"""
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from math import log2


class random_walk:
    """
    class for random walk simulation
    
    parameters:
        self.n_iter
            - number of executed iterations
        self.n_steps:
            - number of steps to be performed
        self.walkers:
            - ndarray that holds x & y coords of each walker
            self.walkers[0] are x coords.
            self.walkers[1] are y coords.
    """
    # constants and initialization
    xmax = ymax = 250
    xmin = ymin = -250
    nx = ny = 5
    n_cells = 25
    entropy = []
    n_iter = 0
    
    def __init__(self, n_walkers, n_steps):
        """ initialize walkers to origin"""
        self.walkers = np.zeros((2, n_walkers), int)
        self.n_walkers = n_walkers
        self.n_steps = n_steps
        
    def iterate(self):
        """update the random walk and call plot method each time"""
        while self.n_iter < self.n_steps:
            # generate random steps & add to current walker coords.
            x = ran.randint(low = -1, high = 2, size = self.n_walkers)
            y = ran.randint(low = -1, high = 2, size = self.n_walkers)
            self.walkers[0] += x
            self.walkers[1] += y
            
            # call to check borders, calculate entropy, & increment counter
            self.check_borders()
            self.calc_entropy()
            self.n_iter += 1
            
    def calc_entropy(self):
        """calculates the entropy of the system"""
        # initialized before looooooops
        s = 0
        cells = np.zeros(self.n_cells, int)
        
        # determine the number of walkers in each cell
        for walker in self.walkers.transpose():
            x = walker[0]
            y = walker[1]
            ix = int((x - self.xmin)/(self.xmax - self.xmin) * self.nx)
            iy = int((y - self.ymin)/(self.ymax - self.ymin) * self.ny)
            cells[ix + iy*self.ny] += 1
        
        # calculate the entropy of each cell & append to entropy list
        for i in range(self.n_cells):
            pk = cells[i]/self.n_walkers
            if pk > 0:
                s += -pk * log2(pk)
        self.entropy.append(s)
        
    def check_borders(self):
        self.walkers[0][self.walkers[0] >= self.xmax] = self.xmax - 1
        self.walkers[0][self.walkers[0] <= self.xmin] = self.xmin + 1
        self.walkers[1][self.walkers[1] >= self.ymax] = self.ymax - 1
        self.walkers[1][self.walkers[1] <= self.ymin] = self.ymin + 1
        
    def plot(self):
        """plots the walkers & entropy"""
        # plotting the walkers
        plt.plot(self.walkers[0], self.walkers[1], 'b.')
        plt.xlim(-250, 250)
        plt.ylim(-250, 250)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Number of Steps: {self.n_iter}")
        plt.show()
        
        # plotting the entropy
        plt.plot(self.entropy)
        plt.title("Entropy")
        plt.xlabel("Number of Steps")
        plt.show()
            
            
# putting it all together
sim = random_walk(100, 50000)
sim.iterate()
sim.plot()