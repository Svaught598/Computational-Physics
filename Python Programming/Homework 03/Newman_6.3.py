"""
newman Problem 6.3

LU Decomposition
"""
import numpy as np

""" Part A ++++++++++++++++++++++++++++++++++++++++++++++++"""


def lu_decomposition(array):
    N = len(array)
    L = np.zeros([N, N], float)
    U = np.zeros([N, N], float)
    # U[:] = array
    
    # loop through rows
    for i in range(N):
        L[i, i] = 1.0

        # loop through columns for U
        for j in range(i, N):
            U[i, j] = array[i, j] - sum(L[i, k]*U[k, j] for k in range(i))

        # loop through columns for L
        for j in range(i):
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
print(f'Are Equal? \n{np.allclose(A, np.dot(l, u))}\n')


""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++"""

# N = len(A)

# y = np.empty(N, float)
# for i in range(N-1, -1, -1):
#     y[i] = V[i]
#     for j in range(N-1, i, -1):
#         y[i] -= u[i,j]*V[j]
#         print(u[i,j])

# x = np.empty(N, float)
# for i in range(N):
#     x[i] = y[i]
#     for j in range(i+1, N):
#         x[i] -= l[i,j]*y[j]

# print(x)
# print(np.linalg.solve(A,V))

