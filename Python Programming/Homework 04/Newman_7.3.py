"""
Newman Problem 7.3

Fourier transforms of musical instruments
"""
from numpy.fft import rfft, rfftfreq
import numpy as np
import matplotlib.pyplot as plt


# Loading waveform data into arrays
piano = np.loadtxt('piano.txt')
trumpet = np.loadtxt('trumpet.txt')

# fast fourier transforms
piano_fft = rfft(piano)
piano_freq = rfftfreq(len(piano), d = 1/44100.)
trumpet_fft = rfft(trumpet)
trumpet_freq = rfftfreq(len(trumpet), d = 1/44100.)

# plots of fourier transforms
plt.plot(piano_freq, abs(piano_fft))
plt.title('Piano FFT')
plt.xlim(0, 5000)
plt.show()
plt.plot(trumpet_freq, abs(trumpet_fft))
plt.title('Trumpet FFT')
plt.xlim(0, 5000)
plt.show()

max_piano_freq = piano_freq[np.argmax(piano_fft)]
max_trumpet_freq = piano_freq[np.argmax(trumpet_fft)]

print()
print(max_piano_freq)
print(max_trumpet_freq)
print()
print("""
    Both max frequencies are roughly multiples of 261 Hz, 
    implying that both instruments are playing the note C, 
    just in different octaves.""")