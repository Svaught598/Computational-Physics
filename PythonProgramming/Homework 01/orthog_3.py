"""
Problem #4

Orthog Modification #3
"""
import numpy as np
from numpy.linalg import norm


def orthog():
    """finds a vector that is:

        - Orthogonal to a
        - Same magnitude as b
        - In plane made by a & b
    """
    global cross
    global a
    global b
    global dot_product

    # user input for vectors
    a = np.array(eval(input("Enter the first vector: ")))
    b = np.array(eval(input("Enter the second vector: "))) 
    a, b = a.flatten(), b.flatten()

    # checking that both are 3-D
    if len(a) == 3 and len(b) == 3:
        cross = np.cross(a, b)
    else:
        print("Make sure you enter 3-D vectors for BOTH")
        orthog()

    # checking to see if the two vectors are orthogonal
    dot_product = np.dot(a, b)
    if dot_product == 0:
        return None
    else: 
        pass

    # checking that a & b are NOT in same direction
    if norm(cross) != 0:
        pass
    else:
        print("Make sure both vectors are different directions!")
        orthog()

    # finding vector orthogonal to plane of a & b
    unit = cross/norm(cross)

    # finding vector orthogonal to unit
    cross = np.cross(a, unit)
    result = cross/norm(cross)

    # making sure vector is same magnitude as b
    result = unit * norm(b)
    return list(result)

result = orthog()
if result == None:   
    print("The two vectors are orthogonal!")
else:
    print(f"Vector orthogonal to a with magnitude of b: {result}")