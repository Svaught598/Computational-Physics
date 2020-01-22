import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(divs, number):

    # initialize array of complex numbers
    complex_numbers = np.empty((divs, divs), dtype = np.complex128)
    temp = np.linspace(-number, number, divs).astype(np.complex128)

    # adding real numbers to array
    for i in range(divs):
        complex_numbers[i] = temp 

    # adding imaginary parts
    complex_numbers = complex_numbers.transpose()
    for i in range(divs):
        complex_numbers[i] += temp * 1j

    # Flip orientation again
    complex_numbers = complex_numbers.transpose()

    # Mandelbrot set initiation
    z = np.zeros((divs, divs), dtype = np.complex128)
    _mandelbrot = np.empty((divs, divs), dtype = np.uint64)

    # Begin loop for Mandbrot set
    for i in range(50):

        # Equation with numpy arrays
        z = np.square(z) + complex_numbers

        # replace values in _mandelbrot with index count where > 2
        _mandelbrot[abs(z) > 2] = i

        """
        The following block was inserted to avoid overflows
        in z, but it runs faster if I comment it out, so...
        """
        # replace values > 2 with 0 to avoid overflows
        z[abs(z) > 2] = 0
     
    return _mandelbrot


plt.imshow(
    mandelbrot(1000, 2),
    cmap = 'hot',
)
plt.show()
