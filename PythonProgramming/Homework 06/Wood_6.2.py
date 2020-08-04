"""
Problem 2

Coupled Radioactive Decay
"""
import numpy as np
import matplotlib.pyplot as plt


# Assume initial amounts of each nuclei
NA = 1000.
NB = 0.

# Diff eq in function
def func(n):
    # unpacking n
    na = n[0]
    nb = n[1]
    ta = n[2]
    tb = n[3]
    
    # new values of na & nb
    dna = -na/ta
    dnb = na/ta - nb/tb
    
    return np.array([dna, dnb, ta, tb], float)
    
# euler method function
def euler(f, n_init, a, b, N):
    
    # setup
    h = (b-a)/N
    n = n_init
    tpoints = np.arange(a, b, h)
    napoints = []
    nbpoints = []
    
    # actual euler method
    for t in tpoints:
        napoints.append(n[0])
        nbpoints.append(n[1])
        
        n += h*f(n)
        
    return tpoints, napoints, nbpoints

""" Plotting stuff and calling functions below this +++++++++++++++++++++"""

# function to plots stuff
def plot(t, na, nb, title):
    plt.plot(t, na, label='nA population')
    plt.plot(t, nb, label='nB population')
    plt.title(title)
    
# set fig size
plt.figure(figsize=(17,5))

# ta/tb = 1/10
R = np.array([NA, NB, 1, 10], float)
ts, nas, nbs = euler(func, R, 0, 5, 1000)
plt.subplot(1, 6, 1)
plot(ts, nas, nbs, 'ta/tb = 1/10')

# ta/tb = 1/5
R = np.array([NA, NB, 1, 5], float)
ts, nas, nbs = euler(func, R, 0, 5, 1000)
plt.subplot(1, 6, 2)
plot(ts, nas, nbs, 'ta/tb = 1/5')
    
# ta/tb = 1/2
R = np.array([NA, NB, 1, 2], float)
ts, nas, nbs = euler(func, R, 0, 5, 1000)
plt.subplot(1, 6, 3)
plot(ts, nas, nbs, 'ta/tb = 1/2')

# ta/tb = 1/1
R = np.array([NA, NB, 1, 1], float)
ts, nas, nbs = euler(func, R, 0, 5, 1000)
plt.subplot(1, 6, 4)
plot(ts, nas, nbs, 'ta/tb = 1/1')

# ta/tb = 2/1
R = np.array([NA, NB, 2, 1], float)
ts, nas, nbs = euler(func, R, 0, 5, 1000)
plt.subplot(1, 6, 5)
plot(ts, nas, nbs, 'ta/tb = 2/1')

# ta/tb = 5/1
R = np.array([NA, NB, 5, 1], float)
ts, nas, nbs = euler(func, R, 0, 5, 1000)
plt.subplot(1, 6, 6)
plot(ts, nas, nbs, 'ta/tb = 5/1')

plt.show()
print('''
    Generally, it appears as though the populations change more rapidly
    for smaller ratios for ta & tb. When the ratio reaches unity, there 
    is transition from relaxed nb > na to relaxed na > nb. This is easier
    visualized in the next plot
''')


""" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
What happens if we plot the population values limit
for different values of ta/tb?

That's what is happening here!
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""" 

# initialize some stuff
na_ends = []
nb_ends = []
t_ratios = np.linspace(.01, 10, 100)
NA, NB = 1000, 0

# loop through T ratios
for i in t_ratios:
    
    # Not sure why, but this code only works correctly
    # if I multiply each t by some scalar > 3
    # Think it has something to do with the 
    # division in the diff eq, and that it changes too
    # quickly for eulers method to handle for some values
    ta = i*5
    tb = 1.*5
    
    # initialize na & nb and call euler method
    R = np.array([NA, NB, ta, tb], float)
    ts, nas, nbs = euler(func, R, 0, 20, 1000)
    
    # append new relaxed values
    na_ends.append(nas[-1])
    nb_ends.append(nbs[-1])
    
# plotting stuff
plt.plot(t_ratios, na_ends, label='Na')
plt.plot(t_ratios, nb_ends, label='Nb')
plt.xlabel('Ratio of Ta & Tb')
plt.ylabel('Population')
plt.title('Relaxed Populations')
plt.legend()
plt.show()   