#Python Program to accept strings that contains all the vowels

def check_all_vowels(input_str):
    char_list = [char for char in list(set(input_str.lower())) if char in 'aeiou']

    if len(char_list) == 5:
        return 'Accepted!'
    return 'Not Accepted!'

my_str = 'ABeeIghiObhkUul'
print(check_all_vowels(my_str))



