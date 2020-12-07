from time import time 
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'Time Elapsed is {end_time - start_time}')

        return result

    return wrapper

@speed_test
def sum_func():
    '''User made function to find some of numbers in range 0 to 100000'''
    return sum(x for x in range(100000))

print(sum_func())




    
