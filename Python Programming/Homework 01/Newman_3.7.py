import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from pprint import pprint

# Complex Array initialization
temp = np.linspace(-2, 2, 1000)
x = np.vstack([temp, temp])
for i in range(998):
    x = np.vstack([x, temp])
complex_numbers = x + np.transpose(x) * 1J


def mandelbrot(complex_array):
    # local function variables
    z = np.zeros((1000, 1000))
    mandelbrot_set = np.zeros((1000, 1000))

    # Begin loop for Mandbrot set
    for i in range(500):
        z = np.square(z) + complex_array
        mandelbrot_set[np.abs(z) > 2] = i
     
    return mandelbrot_set


plt.imshow(
    mandelbrot(complex_numbers),
)
plt.show()