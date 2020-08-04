"""
Problem #3

Orthog Modification #2
"""
import numpy as np
from numpy.linalg import norm


def orthog():
    """Returns a unit vector that is orthogonal to both a & b
    """
    global cross 

    # input for vectors
    a = np.array(eval(input("Enter the first vector: ")))
    b = np.array(eval(input("Enter the second vector: "))) 
    a, b = a.flatten(), b.flatten()

    # checking that both are 3-D
    if len(a) == 3 and len(b) == 3:
        cross = np.cross(a, b)
    else:
        print("Make sure you enter 3-D vectors")
        orthog()

    # making unit vector if cross product not zero
    if norm(cross) == 0:
      return (False)
    else:
      return list(cross/norm(cross))

value = False
while value == False:
    value = orthog()
    if value:
      print(f"Unit vector orthogonal to both input vectors: {value}")
    else:
      print("Both input vectors are in the same direction!")
  