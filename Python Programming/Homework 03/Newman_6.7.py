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

matrix = diags(
    [[4]*10000, [-1]*9999, [-1]*9999, [-1]*9998, [-1]*9998],
    offsets = [0, -1, 1, -2, 2], 
    shape=(10000, 10000)).toarray()
matrix[0,0] = matrix[9999,9999] = 3

w = np.zeros(10000, int)
w[0] = w[1]  = 5
 
v = spsolve(matrix, w)
print('Part C:')
print(v, '\n')