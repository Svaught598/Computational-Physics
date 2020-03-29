"""
Newman Problem 7.9

Image Deconvolution
"""
import numpy as np
import matplotlib.pyplot as plt
from math import exp


""" Part A +++++++++++++++++++++++++++++++++++"""

# loading data and displaying image
blur = np.loadtxt('blur.txt')
plt.imshow(blur)
plt.show()

""" Part B +++++++++++++++++++++++++++++++++++"""
from itertools import product

# initialization & constants
sigma = 25
N = len(blur[0])
grid = np.zeros((N, N), float)

# gaussian function
def gaussian(x, y):
    return (exp(-(x*x + y*y)/(2*sigma*sigma)))

# fillout grid with gaussian points
for i in range(N):
    for j in range(N):
        grid[ i, j] += gaussian(i, j)
        grid[-i,-j] += gaussian(i, j)
        grid[-i, j] += gaussian(i, j)
        grid[ i,-j] += gaussian(i, j)

# display grid
plt.imshow(grid)
plt.show()

""" Part C +++++++++++++++++++++++++++++++++++"""
from numpy.fft import rfft2, irfft2

# loading data and displaying image
blur = np.loadtxt('blur.txt')

# fourier transforms
blur_fft = rfft2(blur)
grid_fft = rfft2(grid)

# deal with zeros and find output fourier data
grid_fft[grid_fft < 1.e-12] = 1.e-12
output_fft = blur_fft/grid_fft/1024/1024

# reverse fourier transform and plotting
output = irfft2(output_fft)
plt.imshow(output)
plt.show()

print("Part D:")
print('''
    When the numbers calculated by the point spread function are 
    sufficiently small, we lose the ability to accurately store 
    their values as floating point numbers. Becuase of this, the
    fft of the point spread function is not as accurate as it could 
    be in theory, thus the deblurred image is not equivalent to
    the original image.''')