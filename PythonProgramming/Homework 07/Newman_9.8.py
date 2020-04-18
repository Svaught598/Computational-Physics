"""
Newman 9.8

The Schrodinger equation & the Crank-Nicolson Method
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from cmath import exp


# Constants & Stuff
N = 1000        # num of slices
L = 1.0e-8     # length of box
x0 = L/2.0      # meters
sigma = 1.0e-10 # meters
kappa = 5.0e10  # 1/meters
M = 9.109e-31   # kg (mass of electron)
a = L/N         # slice size
hbar = 6.62e-34 # reduced plancks constant
timestep = h = 1.e-19
tmax = 4.0e-16  # max time


# Had to make a ufunc for complex exponent of numpy array
# this really should be built into numpy
@np.vectorize
def cexp(a):
    return exp(a)


# Took this function from Newman's online resources
def banded(Aa,va,up,down):

    # Copy the inputs and determine the size of the system
    A = np.copy(Aa)
    v = np.copy(va)
    N = len(v)

    # Gaussian elimination
    for m in range(N):

        # Normalization factor
        div = A[up,m]

        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]

        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]

    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]

    return v


""" Part A +++++++++++++++++++++++++++++++++++++++++"""


# Initialization

# First the 1D arrays
V = np.zeros(N+1, complex)
xs = np.linspace(0, L, N+1)
psi = np.zeros(N+1, complex)
psi[0:N+1] = np.exp(-(xs[0:N+1] - x0)**2/(2*sigma*sigma)) * np.exp(kappa*xs[0:N+1]*1j)

# Then some complex numbers
a1 = complex(1, h*hbar/(2*M*a*a))
a2 = complex(0, -h*hbar/(4*M*a*a))
b1 = complex(1, -h*hbar/(2*M*a*a))
b2 = complex(0, h*hbar/(4*M*a*a))

# Then a Banded matrix
A = np.zeros([3, N+1], complex)
A[0,:] = a2
A[1,:] = a1
A[2,:] = a2

# Function to perform one iteration of the calculation
def iterate(_V, _psi, ):
    V[1:N] = b1*_psi[1:N] + b2*(_psi[2:N+1] + _psi[0:N-1])
    psi = banded(A, V, 1, 1)
    return V, psi
    

""" Part B +++++++++++++++++++++++++++++++++++++++++"""


# Iteration
real_psis = []
t = 0
print("Iterating...")
while t < tmax:
    V, psi = iterate(V, psi)
    real_psi = psi.real
    real_psis.append(real_psi)
    t += h

# Animation Initialization
fig = plt.figure()
ax = plt.axes(ylim = (-1, 1))
frame, = ax.plot([],[], lw = 3)

# Generating Frames
print("Plotting...")
frame_list = []
for p in real_psis:
    frame, = ax.plot(xs, p, "b")
    frame_list.append([frame,])

# Showing animation
anim = animation.ArtistAnimation(fig, frame_list, interval = 20, blit = True)
plt.show()
