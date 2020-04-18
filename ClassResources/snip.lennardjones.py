import numpy as np
import matplotlib.pyplot as plt

def V(r):
    return 4 * ((1/r)**12 - (1/r)**6)
def F(r):
    return 24 * (2*(1/r)**13 - (1/r)**7)

r = np.linspace(0.9,3,200)

plt.plot(r,V(r),label='Potential')
plt.plot(r,F(r),label='Force')
plt.plot([0,3],[0,0],'r--')      # plot y=0 line
plt.legend()

plt.axis([0,3,-2.5,2])

plt.show()