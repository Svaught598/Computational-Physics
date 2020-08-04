"""
Problem 1

Rejection Method
"""
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt


# Distribution Function
@np.vectorize
def f(x, alpha = 1, beta = 3):
    return alpha*np.exp(-beta*x)


# Main function
def gen_dist(distf, Nsamples):
    ran_list = []
    n_accepted = 0
    x = np.linspace(0, 1, 10000)
    y = f(x)
    pmin = 0
    pmax = y.max()
    
    while n_accepted < Nsamples:
        x = ran.uniform(0, 1)
        y = ran.uniform(pmin, pmax)
        
        if y < f(x):
            ran_list.append(x)
            n_accepted += 1
            
    return ran_list
        
    
    
# 1000 N histogram
x = gen_dist(f, 1000)
plt.hist(x,bins=10)
plt.title("1000 Samples")
plt.show()

# 10000 N histogram
x = gen_dist(f, 10000)
plt.hist(x,bins=100)
plt.title("10000 Samples")
plt.show()