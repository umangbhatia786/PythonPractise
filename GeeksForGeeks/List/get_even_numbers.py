#To get all even numbers from a list

def get_even_numbers(int_list):
    '''To return list of all even numbers inside a list'''
    return [num for num in int_list if num %2 == 0]

my_list = [1,2,3,4,5,6,7,8,9,10]

for num in get_even_numbers(my_list):
    print(num)
