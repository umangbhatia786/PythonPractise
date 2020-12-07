#To check whether a given number is Fibonacci or not
#A given number is fibonacci if any one of 5*n**2 + 4 or 5*n**2 - 4 is a perfect square
from math import sqrt, pow

def is_perfect_square(x):
    s = int(sqrt(x))
    return x == pow(s,2)

def is_fibonacci(num):
    return is_perfect_square(5*pow(num,2) + 4) or is_perfect_square(5*pow(num,2) - 4)

input_num = int('Enter a number here: ')

if is_fibonacci(input_num):
    print('The given number is fibonacci')
else:
    print('No!')