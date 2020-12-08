#Python Program to replace all occurrences of string with another

def replace_occurrences(input_str, word, replace_with):
    return input_str.replace(word, replace_with)

my_str = 'geeksforgeeks'

print(replace_occurrences(my_str,'geeks','abcd'))