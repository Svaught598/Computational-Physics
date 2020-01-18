import numpy as np
import matplotlib.pylab as plt

# initialization
r = np.arange(1, 4, 0.01)
x = np.ones(len(r)) * 0.5

# first 1000 iterations
for i in range(1000):
    x = r*x*(1 - x)

# second 1000 iterations
for i in range(1000):
    x = r*x*(1 - x)

# plot feigenbaum tree
plt.plot(r, x, 'ko')
plt.show()