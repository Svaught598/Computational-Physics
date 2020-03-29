"""
newman Problem 6.3

LU Decomposition
"""
import numpy as np
import gc
""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++"""

def lu_decomposition(array):
    N = len(array)
    L = np.zeros([N, N], float)
    U = np.zeros([N, N], float)
    # U[:] = array
    
    # loop through columns
    for j in range(N):
        L[j, j] = 1.0

        # loop through rows for U
        for i in range(j+1):
            U[i, j] = array[i, j] - sum(L[i, k]*U[k, j] for k in range(i))

        # loop through columns for L
        for i in range(j, N):
            L[i, j] = array[i, j] - sum(L[i, k]*U[k, j] for k in range(j))
            L[i, j] /= U[j, j]

    return L, U



A = np.array(
    [[2,  1,  4,  1],
    [ 3,  4, -1, -1],
    [ 1, -4,  1,  5],
    [ 2, -2,  1,  3]],
    float)
V = np.array([-4, 3, 9, 7], float)
l, u = lu_decomposition(A)
print(f'Original Matrix: \n{A}\n')
print(f'L Matrix: \n{l}\n')
print(f'U Matrix: \n{u}\n')
print(f'A = LU? {np.allclose(A, np.dot(l, u))}')
print(np.dot(l, u), '\n')


""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++"""

N = len(A)

# double backsubstitution
y = np.zeros(N, float)
for i in range(N):
    y[i] = V[i]
    for j in range(i+1):
        y[i] -= l[i, j]*y[j]
    y[i] /= l[i, i]

x = np.empty(N, float)
for i in range(N-1, -1, -1):
    x[i] = V[i]
    for j in range(N-1, i, -1):
        x[i] -= u[i, j]*V[j]
    x[i] /= u[i,i]
    

print(x)
print(np.linalg.solve(A, V))
print('Could not figure out double backsubstitution part')
