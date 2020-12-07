#To find sum of squares of first N natural numbers
from math import pow

def sum_squares(n):
    sum = 0
    for val in range(1,n+1):
        sum += pow(val,2)
    return sum

print(f'Sum of squares of first 10 natural numbers is {sum_squares(10)}')