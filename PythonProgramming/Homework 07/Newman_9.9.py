"""
Newman 9.9

The Schrodinger Equation and the Spectral Method
"""
import numpy as np
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from cmath import exp


# Constant Declaration
N = 1000        # num of slices
L = 1.0e-8     # length of box
x0 = L/2.0      # meters
sigma = 1.0e-10 # meters
kappa = 5.0e10  # 1/meters
M = 9.109e-31   # kg (mass of electron)
a = L/N         # slice size
hbar = 6.62e-34 # reduced plancks constant
timestep = h = 1.e-18
tmax = 1.0e-14  # max time


# Taken from Newman's online resources
######################################################################
# 1D DST Type-I

def dst(y):
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -np.imag(rfft(y2))[:N]
    a[0] = 0.0
    return a


######################################################################
# 1D inverse DST Type-I

def idst(a):
    N = len(a)
    c = np.empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = irfft(c)[:N]
    y[0] = 0.0
    return y


######################################################################

# Had to make a ufunc for exponential of a complex numpy array
# this really should be built into numpy
@np.vectorize
def cexp(a):
    return exp(a)

""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# Initialize position
xs = np.linspace(0, L, N+1)

# Initialize wavefunciton & real & complex
psi = np.empty(N+1, complex)
psi[0:N+1] = cexp(-(xs[0:N+1] - x0)**2/(2*sigma*sigma)) * cexp(kappa*xs[0:N+1]*1j)
r_psi = np.empty(N+1, float)
r_psi = psi.real
i_psi = np.empty(N+1, float)
i_psi = psi.imag

# Discrete Since Transforms
rbs = dst(r_psi)
ibs = dst(i_psi)


""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# Finds real part of wavefunction
k = np.array([i+1 for i in range(N+1)])
t = 1e-16
def iterate(psi, t):
    rbs = dst(psi.real)
    ibs = dst(psi.imag)
    cs = (rbs*np.cos(np.pi**2*hbar*k*k/(2*M*L*L)*t)) \
    - (ibs*np.sin(np.pi**2*hbar*k*k/(2*M*L*L)*t))
    cs *= np.sin(np.pi*k*xs/N)
    psi = idst(cs)
    psi *= np.sin(np.pi*k*xs/N)
    return psi

# plotting one iteration at t = 1.e-16
print(np.max(psi))
new_psi = iterate(psi, 1.e-16)
plt.plot(xs, new_psi)
plt.show()
print(np.max(psi))


""" Part C ++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# Iterations...
real_psis = []
t = 0
while t < tmax:
    new_psi = iterate(psi, 1.e-16)
    real_psis.append(new_psi)
    new_psi, psi = psi, new_psi
    t += h

# Animation Initialization
fig = plt.figure()
ax = plt.axes(ylim = (-.1, .1))
frame, = ax.plot([],[], lw = 3)

# Generating Frames
print("Plotting...")
frame_list = []
for p in real_psis:
    frame, = ax.plot(xs, p, "b")
    frame_list.append([frame,])

# Showing animation
print("done plotting!")
anim = animation.ArtistAnimation(fig, frame_list, interval = 20, blit = True)
plt.show()

