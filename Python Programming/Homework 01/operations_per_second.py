from time import time
from numpy.random import random
import gc



def operations_per_second(seconds):
    """calculates the number of operations performed in some length of time:

    returns a tuple (
        time_counting_operations,
        number_of_operations,
        operations_per_second,
    )
    """
    time_computing_operations = 0
    number_of_operations = 0

    while time_computing_operations < seconds:
        number_of_operations += 1
        float1 = random()
        float2 = random()
        t1 = time()
        float1 * float2
        t2 = time()
        elapsed = t2 - t1
        time_computing_operations += elapsed

    return (
        time_computing_operations, 
        number_of_operations, 
        number_of_operations/time_computing_operations,
    )

_, _, flops = operations_per_second(1)
print(f'floating point operations per second is: {flops}')
