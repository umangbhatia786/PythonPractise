#To check whether a number is prime or not

input_num = int(input('Enter a number: '))

is_prime = True

for num in range(2,input_num):
    if input_num % num == 0:
        is_prime = False
        break
if is_prime:
    print('Number is prime')
else:
    print('Number is not prime')

    