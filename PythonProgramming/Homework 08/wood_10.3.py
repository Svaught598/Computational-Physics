"""
Problem 3

Random Walk in 2D
"""
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt


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
    def __init__(self, n_walkers, n_steps):
        """ initialize walkers to origin"""
        self.n_iter = 0
        self.n_steps = n_steps
        self.walkers = np.zeros((2, n_walkers), int)
        self.n_walkers = n_walkers
        
    def iterate(self):
        """update the random walk and call plot method each time"""
        while self.n_iter < self.n_steps:
            # generate random steps & add to current walker coords.
            x = ran.randint(low = -1, high = 2, size = self.n_walkers)
            y = ran.randint(low = -1, high = 2, size = self.n_walkers)
            self.walkers[0] += x
            self.walkers[1] += y
            
            # calls to plot and increment n_iter
            self.plot()
            self.n_iter += 1
        
    def plot(self):
        """plots the walkers if condition is met"""
        N = self.n_steps
        conditions = [
            self.n_iter == 0,
            self.n_iter == N/4,
            self.n_iter == N/2,
            self.n_iter == 3*N/4,
            self.n_iter == N-1
        ]
        if any(conditions):
            plt.scatter(self.walkers[0], self.walkers[1])
            plt.xlim(-250, 250)
            plt.ylim(-250, 250)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"Number of Steps: {self.n_iter}")
            plt.show()
            
    
# putting it all together
sim = random_walk(50, 10000)
sim.iterate()  