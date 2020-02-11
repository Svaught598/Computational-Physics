"""
Newman Problem 6.8

The QR algorithm
"""
import numpy as np
from numpy.linalg import norm

A = np.array([
    [1, 4, 8, 4],
    [4, 2, 3, 7],
    [8, 3, 6, 9],
    [4, 7, 9, 2]], float)


def qr_decomposition(array):
    N = len(array)
    Q = np.zeros([N, N], float)
    R = np.zeros([N, N], float)
    U = np.zeros([N, N], float)

    U[:,0] = array[:,0]
    Q[:,0] = U[:,0]/norm(U[:,0])
    R[0,0] = norm(U[:,0])

    for i in range(1, N):
        U[:,i] = array[:,i] - sum(np.dot(Q[:,j], array[:,i])*Q[:,j] for j in range(i))
        Q[:,i] = U[:,i]/norm(U[:,i])

        for j in range(i):
            R[i,j] = np.dot(Q[:,i])