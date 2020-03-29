"""
Newman Problem 7.1

Fourier Transform of Simple Functions
"""
from numpy import zeros, loadtxt, linspace
import matplotlib.pyplot as plt
from cmath import exp, pi, sin

# Function declaration and sampling
N = 1000
xs = linspace(-1*pi, pi, N)
sqr_wave = [(lambda x: -1 if x < 0 else 1)(
    y) for y in xs]
sawtooth = [(lambda x: x)(
    y) for y in xs]
modulated = [(lambda x: sin(pi*(x+pi)/2/pi)*sin(20*pi*(x+pi)/2/pi))(
    y) for y in xs]

# DFT code from Newman
def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

# function for repetitive plotting
def plotstuff(dft_list, name):
    plt.plot(abs(dft_list))
    plt.title(name)
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.xlim(0,100)
    plt.show()

# plotting fourier transforms of waves
plotstuff(dft(sqr_wave), "Square Wave Fourier Transform")
plotstuff(dft(sawtooth), "Sawtooth Wave Fourier Transform")
plotstuff(dft(modulated), "Modulated Wave Fourier Transform")
