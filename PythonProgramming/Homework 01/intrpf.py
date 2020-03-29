"""
Problem 5

Intrpf Modification
"""
import numpy as np
import matplotlib.pyplot as plt


def intrpf(xi,x,y):
    """Function to interpolate between data points
    using Lagrange polynomial
    Inputs
      x   Vector of x coords of data pints (3 values)
      y   Vector of y coords
      xi  The x value where interpolation is computed
    Output
      yi  The interpolated value evaluated at xi
    """

    # calculate yi = p(xi) using Lagrange polynomial 
    yi = ((xi-x[1])*(xi-x[2])/((x[0]-x[1])*(x[0]-x[2]))) * y[0]\
        +((xi-x[0])*(xi-x[2])/((x[1]-x[0])*(x[1]-x[2]))) * y[1]\
        +((xi-x[0])*(xi-x[1])/((x[2]-x[0])*(x[2]-x[1]))) * y[2]
    return yi

def derivative(xi, x, y):
    """Function to find derivative of Lagrange Polynomial
    Inputs
      x   Vector of x coords of data pints (3 values)
      y   Vector of y coords
      xi  The x value where interpolation is computed
    Output
      yi  The interpolated value evaluated at xi
    """
    yi = ((xi-x[1])+(xi-x[2]))/((x[0]-x[1])*(x[0]-x[2])) * y[0]\
        +((xi-x[0])+(xi-x[2]))/((x[1]-x[0])*(x[1]-x[2])) * y[1]\
        +((xi-x[0])+(xi-x[1]))/((x[2]-x[0])*(x[2]-x[1])) * y[2]
    return yi

def linear(m, b, x, xx):
    """Function to plot tangent line at a point
    """
    y = m*(x - xx) + b
    return y

def find_closest(array, value):
    """Function that returns index and value of
    an array that is closest to the argument value
    """
    array = np.asarray(array)
    index = (np.abs(array - value)).argmin()
    return index, array[index]


# Initialize the data points 
x = np.empty(3)
y = np.empty(3)
for i in range(3):
    temp = np.array(eval(input("Enter pair (e.g., [1,2]): ")))
    x[i] = temp[0]
    y[i] = temp[1]
    
# Establish the range of interpolation
xr = np.array(eval(input("Enter range (e.g., [x_min,xmax]): ")))
    

# Find yi for xi using the function intrpf
nplot = 100
xi = np.empty(nplot)
yi = np.empty(nplot)
slopes = np.empty(nplot)
for i in range(nplot):
    xi[i] = xr[0] + (xr[1]-xr[0]) * i/float(nplot)
    yi[i] = intrpf(xi[i], x, y)
    slopes[i]= derivative(xi[i], x, y)

# initialize tangent line and find slope
yii = np.empty(nplot)
index, _ = find_closest(yi, y[1])
slope = slopes[index]

# find yii for tangent line
for i, xii in enumerate(xi):
    yii[i] = linear(slope, y[1], xii, x[1])

print(f"Derivative at point [{x[1]},{y[1]}] is : {slope}")

# Plot the curve
plt.plot(x,y,'*',xi,yi,'-', xi, yii, '.')
plt.title(f"3-point Interpolation (derivative: {slope:.2f})")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data Points','Interpolation','Tangent Line'])
plt.show()