"""
Newman Problem 6.12

Glycolysis
"""
import numpy as np


""" Part B +++++++++++++++++++++++++++++++++++++++++++++"""

def update_x(x, y):
    return y*(1 + x*x)

def update_y(x, y):
    return 2./(1 + x*x)

def relax_bro(init_x, init_y):
    difference = 1.
    new_x, new_y = init_x, init_y

    i = 0
    while difference > 1.e-4 and i < 1.e4:
        old_x, old_y = new_x, new_y
        new_x = update_x(old_x, old_y)
        new_y = update_y(old_x, old_y)

        difference = abs(new_x - old_x) + abs(new_y - old_y)
        i += 1

    return new_x, new_y, i

x, y, i = relax_bro(1.3, 1.9)
print(f'x = {x:.3f} and y = {y:.3f} for {i} iterations\n')


""" Part C +++++++++++++++++++++++++++++++++++++++++++++"""

def update_x(x, y):
    return np.sqrt((x - y)/y)

def update_y(x, y):
    return (2 - y)/(4)

def relax_bro(init_x, init_y):
    difference = 1.
    new_x, new_y = init_x, init_y

    i = 0
    while difference > 1.e-4 and i < 1.e7:
        old_x, old_y = new_x, new_y
        new_x = update_x(old_x, old_y)
        new_y = update_y(old_x, old_y)

        difference = abs(new_x - old_x) + abs(new_y - old_y)
        i += 1

    return new_x, new_y, i

x, y, i = relax_bro(1.8, .5)
print(f'x = {x:.3f} and y = {y:.3f} for {i} iterations\n')