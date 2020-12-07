#To Print all prime numbers between given interval

#start = int(input('Enter starting number: '))
#end = int(input('Enter ending number: '))

start = 4
end = 16

prime_list = []
for number in range(start, end+1):
    is_prime = True
    for val in range(2,number):
        if number%val == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(number)
    
print(prime_list)
