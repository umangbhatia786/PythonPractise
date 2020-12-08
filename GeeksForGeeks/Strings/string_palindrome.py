#Python Program to check if a string is Palindrome

def check_string_palindrome(input_string):
    return input_string.lower() == input_string.lower()[::-1]

my_string = 'malayalam'

if check_string_palindrome(my_string):
    print('Palindrome')
else:
    print('Not Palindrome!')