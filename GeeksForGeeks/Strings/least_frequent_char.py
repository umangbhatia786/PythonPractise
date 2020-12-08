#Python Program to find least frequent character in a string

def get_least_frequent_chars(input_str):
    char_list = list(input_str)
    char_count_dict = {char: char_list.count(char) for char in char_list}
    return [key for key, val in char_count_dict.items() if val == min(char_count_dict.values())]

input_str = 'dafwbgbadfwqqqjy'

print(get_least_frequent_chars(input_str))