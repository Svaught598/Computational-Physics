"""
Newman Problem 2.10
"""
import numpy as np


A1 = 15.67
A2 = 17.23
A3 = 0.75
A4 = 93.2

""" PART A -----------------------------------------------------------------"""

def calculate_B(A, Z):
    # Find A5
    if A % 2 == 0 and Z % 2 == 0:
        A5 = 12
    elif A % 2 == 0:
        A5 = -12
    else: 
        A5 = 0

    # Calculate Binding Energy
    B = A1*A \
        - A2*(A**(2/3)) \
        - A3*(Z**2)/(A**(1/3)) \
        - A4 *((A - 2*Z)**2)/A \
        + A5/(A**2)
    return B

print(calculate_B(58, 28))

""" PART B -----------------------------------------------------------------"""

def calculate_B_per_A(A, Z):
    # Find A5
    if A % 2 == 0 and Z % 2 == 0:
        A5 = 12
    elif A % 2 == 0:
        A5 = -12
    else: 
        A5 = 0

    # Calculate Binding Energy per Nucleon
    B = A1*A \
        - A2*(A**(2/3)) \
        - A3*(Z**2)/(A**(1/3)) \
        - A4 *((A - 2*Z)**2)/A \
        + A5/(A**2)
    return B/A

print(calculate_B_per_A(58, 28))

""" PART C -----------------------------------------------------------------"""

def calculate_B_per_A(Z):

    B_list = []
    for A in range(Z, 3*Z):

        # Find A5
        if A % 2 == 0 and Z % 2 == 0:
            A5 = 12
        elif A % 2 == 0:
            A5 = -12
        else: 
            A5 = 0

        # Calculate Binding Energy per Nucleon
        B = A1*A \
            - A2*(A**(2/3)) \
            - A3*(Z**2)/(A**(1/3)) \
            - A4 *((A - 2*Z)**2)/A \
            + A5/(A**2)
        B_list.append(B/A)

    return(max(B_list))

print(calculate_B_per_A(28))

""" PART C -----------------------------------------------------------------"""

def calculate_B_per_A():

    B_list = []
    for Z in range(1, 101):
        temp = []
        for A in range(Z, 3*Z):
            
            # Find A5
            if A % 2 == 0 and Z % 2 == 0:
                A5 = 12
            elif A % 2 == 0:
                A5 = -12
            else: 
                A5 = 0

            # Calculate Binding Energy per Nucleon
            B = A1*A \
                - A2*(A**(2/3)) \
                - A3*(Z**2)/(A**(1/3)) \
                - A4 *((A - 2*Z)**2)/A \
                + A5/(A**2)
            temp.append(B/A)

        # find max binding energy per nucleon for each Z
        B_list.append(max(temp))

    # return the list of maximum binding energies
    return B_list

final_list = calculate_B_per_A()
for i, B in enumerate(final_list):
    print(f"Z = {i + 1} and most stable B/A = {B}")

final_B = max([B for i, B in enumerate(final_list)])
final_Z = max([i + 1 for i, B in enumerate(final_list) if B == final_B])
print(f"Z = {final_Z} yields the largest Binding energy per nucleon: B = {final_B}")