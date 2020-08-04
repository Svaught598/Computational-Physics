'''
Newman Problem 6.9
PartB

Asymmetric Quantum Well
'''
from scipy.constants import physical_constants
import numpy as np
from numpy.linalg import eigvalsh
from math import pi

""" Part C ===================================================="""

# constants
hbar, _, _ = physical_constants['reduced Planck constant in eV s'] # in eV*seconds
e_m, _, _ = physical_constants['electron mass'] # in Kg
e, _, _ = physical_constants['elementary charge'] # in C
a = 10 # in eV
L = 5.e-10

# function to calculate hamiltonian elements
def calculate_Hmn(m, n):
    if m == n:
        return (pi*hbar*n)**2/(2*e_m*L**2)*(e)+a/2
    elif (m+n)%2 == 1:
        return -8*a/(pi**2)*m*n/(m**2-n**2)**2
    else:
        return 0

# calculating hamiltonian matrix
N = 10
Hamiltonian = np.zeros((N, N), float)
for i in range(N):
    for j in range(N):
        Hamiltonian[i,j] = calculate_Hmn(i+1, j+1)

# getting eigenvalues and printing
Energy = eigvalsh(Hamiltonian)
print('Part C')
for i, e in enumerate(Energy):
    print(f'E{i} = {e:0.6f} eV')
    
print('')
""" Part D ===================================================="""

# calculating hamiltonian matrix
N = 100
Hamiltonian2 = np.zeros((N, N), float)
for i in range(N):
    for j in range(N):
        Hamiltonian2[i,j] = calculate_Hmn(i+1, j+1)
    
# getting eigenvalues and printing
Energy2 = eigvalsh(Hamiltonian)
print('Part D')
for i, e in enumerate(Energy2):
    print(f'E{i} = {e:0.6f} eV')
    if i >8:
        break
        
print('')
print("There doesn't appear to be much difference between N = 10 and N = 100")

'''
Newman Problem 6.9
Part E

Asymmetric Quantum Well
'''
import scipy.integrate as integrate
import numpy as np
from numpy.linalg import eigh
from math import pi
import matplotlib.pyplot as plt

# calculate hamiltonian matrix
N = 100
Hamiltonian = np.zeros((N, N), float)
for i in range(N):
    for j in range(N):
        Hamiltonian[i,j] = calculate_Hmn(i+1, j+1)

# store psi eigenstates
_, psi = eigh(Hamiltonian)

# sum eigenstates with appropriate weights (psi[m,n])
def calc_psi(n, x_list):
    wavefunction = sum(
        [psi[n,i]*np.sin(pi*(i+1)*x_list/L) for i in range(100)])
    return np.sqrt(2./L)*wavefunction

# generating wavefunctions
xs = np.linspace(0, L, 100)
ground = calc_psi(0,xs)
first = calc_psi(1,xs)
second = calc_psi(2,xs)

# plotting
plt.plot(xs, ground*ground,'-b', label='Ground State')
plt.plot(xs, first*first,'-r', label='First State')
plt.plot(xs, second*second,'-g', label='Second State')
plt.xlabel('Distance in Meters')
plt.ylabel('Probability Density A.U.')
plt.legend(bbox_to_anchor=(1,1), loc='best')
plt.show()

# checking normalization of wavefunctions
int_0 = integrate.simps(ground*ground, x = xs)
int_1 = integrate.simps(first*first, x = xs)
int_2 = integrate.simps(second*second, x = xs)
print(f'normalization of ground = {int_0:0.5f}')
print(f'normalization of first excited state = {int_1:0.5f}')
print(f'normalization of second excited state = {int_2:0.5f}\n')
print('Not sure why this is symmetric, I was expecting an asymmetry')