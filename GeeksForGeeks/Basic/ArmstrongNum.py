#Python Program to check Armstrong Number
from math import pow

input_num = int(input('Enter a number to check: '))

copy_num = input_num

sum = 0
while copy_num>0:
    rem = copy_num%10
    sum += pow(rem, 3)
    copy_num = copy_num//10

if sum == input_num:
    print('The given number is Armstrong Number')
else:
    print('The given number is not Armstrong')