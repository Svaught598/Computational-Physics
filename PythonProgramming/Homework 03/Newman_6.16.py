'''
Newman Problem 6.16

The Lagrange Point
'''
from scipy.constants import physical_constants

G = 6.674*1.e-11
M = 5.974*1.e24
m = 7.348*1.e22
R = 3.844*1.e8
omega = 2.662*1.e-6

orbit = lambda r: (G*M/(r*r)-G*m/(R-r)**2-omega*omega*r)
orbit_prime = lambda r: (-2*G*M/(r**3)-2*G*m/(R-r)**3-omega*omega)

def newtons_method(func, derivative, guess):
    error = 1.
    x1 = guess
    while error > 1.e-9:
        xprime = x1 -func(x1)/derivative(x1)
        error = abs(xprime - x1)
        x1 = xprime
    return x1

L1 = newtons_method(orbit, orbit_prime, 1.e3)
print('Part A')
print(f'L1 is ~{L1:0.3E} m\n')
