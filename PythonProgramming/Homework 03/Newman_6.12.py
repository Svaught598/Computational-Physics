'''
Newman Problem 6.12

Glycolysis
'''
from math import sqrt

def Part_B(x, y, a, b): 
    newx = lambda x, y: y*(a+x*x)
    newy = lambda x, y: b/(a+x*x)
    max_iterations = 1000
    current_iteration = 0
    while current_iteration < max_iterations:
        x, y = newx(x, y), newy(x, y)
        current_iteration += 1
    return x, y

def Part_C(x, y, a, b):
    # since x = b analytically, I just replaced a two x's with b's
    newx = lambda x, y: y*(a+b*x)
    newy = lambda x, y: b/(a+x*b)
    
    max_iterations = 1000
    current_iteration = 0
    while current_iteration < max_iterations:
        x, y = newx(x, y), newy(x, y)
        current_iteration += 1
    return x, y

x, y = Part_B(1, 1, 1, 2)
print('Part A')
print(f'x = {x:0.3f} and y = {y:0.3f}\n')

x, y = Part_C(1, 1, 1, 2)
print('Part B')
print(f'x = {x:0.3f} and y = {y:0.3f}')