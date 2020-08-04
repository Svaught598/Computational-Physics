"""
Newman Problem 2.9

Madelung Constant For NaCl
"""
from numpy import arange

def calculate_madelung(L):

    madelung_cnst = 0

    for i in arange(-L, L, 1):
        for j in arange(-L, L, 1):
            for k in range(-L, L, 1):
                if i == 0 and j == 0 and k == 0:
                    pass
                elif (i + j + k) % 2 == 0:
                    madelung_cnst -= (i**2 + j**2 + k**2)**(-.5)
                else:
                    madelung_cnst += (i**2 + j**2 + k**2)**(-.5)
    
    return madelung_cnst

print(f'madelung constant is: {calculate_madelung(100)}')