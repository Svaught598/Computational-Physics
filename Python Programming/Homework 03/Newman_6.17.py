"""
Newman Problem 6.17

Nonlinear Circuits
"""
import numpy as np


def update_v1(v1, v2):
    '''function updates v1 from previous v1 & v2'''
    exponential = np.exp((v1 - v2)/0.05 - 1)
    fraction = (v1 - 5)/1000
    return 4000*(fraction + 3.e-9*exponential)


def update_v2(v1, v2):
    '''function updates v2 from previous v1 & v2'''
    exponential = np.exp((v2 - v1)/0.05 - 1)
    fraction = (v2 - 5)/3000
    return 2000*(fraction - 3.e-9*exponential)


def relax_bro(v1_initial, v2_initial):
    old_v1, old_v2 = 0, 0 
    new_v1, new_v2 = v1_initial, v2_initial
    error = 1.

    while error > 1.e-4:
        old_v1, old_v2 = new_v1, new_v2
        new_v1 = update_v1(old_v1, old_v2)
        new_v2 = update_v2(old_v1, old_v2)

        error = abs(new_v1 - old_v1) + abs(new_v2 - old_v2)

    return new_v1, new_v2


v1, v2 = relax_bro(2, 2)
print(v1, v2)