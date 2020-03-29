"""
Newman Problem 7.8

Diffraction Gratings
"""
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
from cmath import pi


# constants
alpha = pi/(20*1.e-6)
omega = 200*1.e-6
wavelength = 500*1.e-9
focal_length = 1.
W = 10*omega
N = 1000

# transmission function declaration
def transmission(u):
    return np.sin(alpha*u)**2

# generating us, xs,  & ys
us = np.array([n*W/N-W/2 for n in range(1000)])
xs = np.array([wavelength*focal_length*n/W for n in range(200)])
ys = np.sqrt(transmission(us))

# setting padding elements to zero
ys[np.abs(us) > omega/2] = 0

# calculating intensity 
ck = fft(ys)
I = (W**2/N**2)*np.abs(ck)**2

# generating total x-axis & total Intensity (mirroring and stuff)
x_axis = np.hstack((-1*xs[::-1], xs)).flatten()
Intensities = np.hstack((I[200:0:-1], I[0:200])).flatten()

# plotting
plt.plot(x_axis*100, Intensities)
plt.xlim(-5,5)
plt.xlabel("cm")
plt.ylabel("Intensity a.u.")
plt.title("Diffraction Grating Interference Pattern")
plt.show()

