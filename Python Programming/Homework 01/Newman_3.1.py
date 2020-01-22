"""
Newman Problem 3.1 


"""
import numpy as np
import matplotlib.pyplot as plt

import os


DIR = os.path.dirname(os.path.abspath(__file__))
SUNSPOTS = np.loadtxt(os.path.join(DIR, "sunspots.txt"))
SUNSPOTS = SUNSPOTS.transpose()


""" Part A ----------------------------------------------------------"""

plt.plot(SUNSPOTS[0], SUNSPOTS[1])
plt.show()

""" Part B ----------------------------------------------------------"""

plt.plot(SUNSPOTS[0][:1000], SUNSPOTS[1][:1000])
plt.show()

""" Part C ----------------------------------------------------------"""


running_average = np.empty(1000, dtype = np.float64)
for i in range(1000):

    # Beginning edge cases
    if i == 0:
        total = SUNSPOTS[1][0] * 6 + sum(SUNSPOTS[1][1:6])
    elif i == 1:
        total = SUNSPOTS[1][0] * 5 + sum(SUNSPOTS[1][1:7])
    elif i == 2:
        total = SUNSPOTS[1][0] * 4 + sum(SUNSPOTS[1][1:8])
    elif i == 3:
        total = SUNSPOTS[1][0] * 3 + sum(SUNSPOTS[1][1:9])
    elif i == 4:
        total = SUNSPOTS[1][0] * 2 + sum(SUNSPOTS[1][1:10])
    elif i == 5:
        total = SUNSPOTS[1][0] * 1 + sum(SUNSPOTS[1][1:11])

    # End edge cases
    elif i == 994:
        total = sum(SUNSPOTS[1][-10:]) + SUNSPOTS[1][-1] * 1
    elif i == 995:
        total = sum(SUNSPOTS[1][-9:]) + SUNSPOTS[1][-1] * 2
    elif i == 996:
        total = sum(SUNSPOTS[1][-8:]) + SUNSPOTS[1][-1] * 3
    elif i == 997:
        total = sum(SUNSPOTS[1][-7:]) + SUNSPOTS[1][-1] * 4
    elif i == 998:
        total = sum(SUNSPOTS[1][-6:]) + SUNSPOTS[1][-1] * 5
    elif i == 999:
        total = sum(SUNSPOTS[1][-5:]) + SUNSPOTS[1][-1] * 6

    # Normal Cases
    else:
        total = sum(SUNSPOTS[1][i-5:i+5])

    running_average[i] = total/11


plt.plot(SUNSPOTS[0][:1000], SUNSPOTS[1][:1000], SUNSPOTS[0][:1000], running_average)
plt.show()

