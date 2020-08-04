"""
Problem 2

Orthog Modificaton #1
"""
import numpy as np
from pprint import pprint
from numpy.linalg import norm


def orthog():
    """checks two vectors of same length for orthogonality

        - Returns True if the vectors are orthogonal
        - Returns False if the vectors aren't orthogonal
    """
    # input for vectors
    a = np.array(eval(input("Enter the first vector: ")))
    b = np.array(eval(input("Enter the second vector: "))) 
    a, b = a.flatten(), b.flatten()
    
    # dot product if dimension check is True
    if len(a) == len(b):
        dot_product = a.dot(b)
        if dot_product == 0:
            return True
        else: 
            return False

    # Function called recursively until compatible vectors are entered
    else:
        print("Sorry, those arrays aren't the same length")
        orthog()


if orthog():
    print("The two vectors entered are orthogonal!")
else:
    print("They are not orthogonal...")
