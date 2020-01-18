import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(x, y):
    c = np.complex(x, y)
    z = 0
    for i in range(500):
        z = z**2 + c
        if abs(z) > 2:
            return 1

xi = np.arange(-2, 2, 1000)
yi = np.arange(-2, 2, 1000)


pixels = np.empty([1000,1000], int)
for i, x in enumerate(xi):
    for k, y in enumerate(yi):
        pixels[i, k] = mandelbrot(x, y)

plt.imshow(pixels, origin = "lower")
plt.winter()
plt.show()

