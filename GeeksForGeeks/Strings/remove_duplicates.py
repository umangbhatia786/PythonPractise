#Python Program to remove duplicates from a String

def remove_duplicates(input_str):
    '''Function To remove duplicates without preserving the order of chars'''
    return ''.join(list(set(input_str)))

def remove_duplicates_with_order(input_str):
    '''Function To remove duplicates preserving the order of chars'''
    char_list = list(input_str)
    count_dict = {char: char_list.count(char) for char in char_list}
    return ''.join([char for char in count_dict.keys()])

input_string = 'abaacddeff'

print(remove_duplicates(input_string))
print(remove_duplicates_with_order(input_string))