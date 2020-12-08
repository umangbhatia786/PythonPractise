#Python Code to get all list of all duplicate characters in a string

def get_duplicate_chars(input_str):
    '''Function that uses set comprehension to get duplicate chars'''
    
    char_list = list(input_str)
    return {char for char in char_list if char_list.count(char) > 1}

my_str = 'aabcdeefgg'

print(get_duplicate_chars(my_str))