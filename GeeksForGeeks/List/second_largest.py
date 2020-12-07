#Python Program to find 2nd Largest num

input_list = [1,5,3,6,8,7,10]

def get_second_largest(int_list):
    sorted_list = sorted(int_list)
    return sorted_list[-2]

print(f'Second largest number in given list is {get_second_largest(input_list)}')