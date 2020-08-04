"""
Newman Problem 7.4

Fourier filtering and smoothing
"""
import numpy as np
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt


''' Part A +++++++++++++++++++++++++++++++++++++++++++++'''

# reading in dow data and plotting
dow = np.loadtxt('dow.txt')
plt.plot(dow)
plt.title("Part A")
plt.show()

''' Part B, C, D +++++++++++++++++++++++++++++++++++++++'''

# calculating coefficients
coefficients = rfft(dow)

# setting first 10% to zero
N = len(coefficients)
coefficients[-N*9//10:] = 0

# calculating inverse fourier transform
dow_new = irfft(coefficients)

# plotting both original and smoothed on same plot
plt.plot(dow)
plt.plot(dow_new)
plt.title("Part B, C, D")
plt.show()

''' Part E +++++++++++++++++++++++++++++++++++++++++++++'''

# calculating coefficients
coefficients = rfft(dow)

# setting first 10% to zero
N = len(coefficients)
coefficients[-N*98//100:] = 0

# calculating inverse fourier transform
dow_new = irfft(coefficients)

# plotting both original and smoothed on same plot
plt.plot(dow)
plt.plot(dow_new)
plt.title("Part E")
plt.show()