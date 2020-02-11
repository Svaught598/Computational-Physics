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
    U[:] = array

    
    for i in range(N):
        L[i, i] = 1.0
        for j in range(N):
            U[i, j] = array[i, j] - sum(U[k, j]*L[i, k] for k in range(i))

        for j in range(i, N):
            L[i, j] = array[i, j] - sum(U[k, j]*L[i, k] for k in range(j))
            L[i, j] /= U[j, j]


    return L, U



A = np.array(
    [[2, 1, 4, 1],
    [3, 4, -1, -1],
    [1, -4, 1, 5],
    [2, -2, 1, 3]],
    float)
V = np.array([-4, 3, 9, 7], float)
l, u = lu_decomposition(A)
print(f'Original Matrix: \n{A}\n')
print(f'L Matrix: \n{l}\n')
print(f'U Matrix: \n{u}\n')
print(f'Are Equal? \n{np.allclose(A, np.dot(l, u))}\n')


""" Part B ++++++++++++++++++++++++++++++++++++++++++++++++"""
N = len(A)

y = np.empty(N, float)
for i in range(N-1, -1, -1):
    y[i] = V[i]
    for j in range(i+1, N):
        y[i] -= A[i,j]*V[j]

x = np.empty(N, float)
for i in range(N):
    y[i] = V[i]
    for j in range(i+1, N):
        y[i] -= A[i,j]*V[j]

print(x)
print(np.linalg.solve(A,V))
