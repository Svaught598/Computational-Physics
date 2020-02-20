"""
Newman Problem 6.17

Nonlinear Circuits
"""
import numpy as np
from numpy.linalg import solve

# constants
r1 = 1000
r2 = 4000
r3 = 3000
r4 = 2000
vplus = 5
vt = 0.05
Io = 3.e-9

# junction 1
def v1_junction(v1, v2):
    exp = Io*(np.exp((v1 - v2)/vt) - 1)
    fractions = (v1 - vplus)/r1 + v1/r2
    return fractions + exp

# junction 2
def v2_junction(v1, v2):
    exp = -Io*(np.exp((v1 - v2)/vt) - 1)
    fractions = (v2 - vplus)/r3 + v2/r4
    return fractions + exp

# jacobian entries
j00 = lambda x, y: (
    1/r1 + 1/r2 + Io*np.exp((x - y)/vt)/vt)
j01 = lambda x, y: (
    -Io*np.exp((x - y)/vt)/vt)
j10 = lambda x, y: (
    Io*np.exp((x - y)/vt)/vt)
j11 = lambda x, y: (
    1/r3 + 1/r4 - Io*np.exp((x - y)/vt)/vt)

def newtons_method(guess_v1, guess_v2):
    e = 1.
    v1, v2 = guess_v1, guess_v2
    while e > 1.e-4:
        # initialize matrix and vector
        jacobian = [[j00(v1, v2), j01(v1, v2)],
                    [j10(v1, v2), j11(v1, v2)]]
        v = [v1_junction(v1, v2), v2_junction(v1, v2)]
        
        print(np.linalg.det(jacobian))
        # solve linear equations and generate new v1 & v2
        delta_v  = solve(jacobian, v)
        v1prime, v2prime = np.array([v1, v2], float) - delta_v
        
        # calculate error & update v1, v2
        error = 0.5*(v1prime - v1 + v2prime - v2)
        v1, v2 = v1prime, v2prime
        
    return v1, v2

v1, v2 = newtons_method(1, 4)
print(f"Voltage 1 is {v1:0.4f}")
print(f"Voltage 2 is {v2:0.4f}")
        
        