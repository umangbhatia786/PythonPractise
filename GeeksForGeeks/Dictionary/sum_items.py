#Python code to find sum of items in a dictionary

def sum_dict_items(input_dict):
    '''Function to Find Sum of values in a given dict'''
    return sum(input_dict.values())

my_dict = {'a':100, 'b':200, 'c':300}

print(sum_dict_items(my_dict))