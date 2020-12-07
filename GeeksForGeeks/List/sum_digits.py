#Python Code to get a list of sum of digits of each number in a list

def get_sum_digits_list(input_list):
    '''Function to return list of sum of digits of each element in a list'''
    return list(map(lambda x: sum(int(digit) for digit in str(x)), input_list))

my_list = [23, 76, 45, 88]

print(get_sum_digits_list(my_list))