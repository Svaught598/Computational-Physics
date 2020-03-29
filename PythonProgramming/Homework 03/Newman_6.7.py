"""
Newman Problem 6.7

A chain of resistors
"""
import numpy as np
from scipy.sparse.linalg import spsolve
from scipy.sparse import diags

""" Part B ===================================="""

voltages = np.array([
    [ 3, -1, -1,  0,  0,  0],
    [-1,  4, -1, -1,  0,  0],
    [-1, -1,  4, -1, -1,  0],
    [ 0, -1, -1,  4, -1, -1],
    [ 0,  0, -1, -1, -4, -1],
    [ 0,  0,  0, -1, -1,  3]])

w = np.array([5, 5, 0, 0, 0, 0])

v = np.linalg.solve(voltages, w)
print('Part B:')
print(v, '\n')

""" Part C ===================================="""

# creating diagonal matrix
matrix = diags(
    [[3]+[4]*9998+[3], [-1]*9999, [-1]*9999, [-1]*9998, [-1]*9998],
    offsets = [0, -1, 1, -2, 2], 
    shape=(10000, 10000))

# creating result vector
w = np.zeros(10000, int)
w[0] = w[1]  = 5
 
# solving with 'scipy.linalg.spsolve'
v = spsolve(matrix, w)
print('Part C:')
print(v, '\n')