#Python code to find Nth Largest number in a list

def nth_larget_num(input_list,n):
    if n > len(input_list):
        raise ValueError('Value of N should not be more than length of list')
    else:
        sorted_list = sorted(input_list)
        return sorted_list[-n]

my_list = [1,3,2,5,6,8,10,22,21,30]

print(f'4rd largest number is {nth_larget_num(my_list,11)}')