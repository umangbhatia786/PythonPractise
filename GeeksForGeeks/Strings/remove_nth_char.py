#Python code to remove nth character from a string

def remove_nth_char(input_str,n):
    if n > len(input_str):
        raise ValueError('Value of n cannot be greater than the length of the string')
    else:
        if n == 1:
            return input_str[1:]
        elif n == len(input_str):
            return input_str[:-n]
        else:
            return input_str[:n-1] + input_str[n:]

input_str = 'UmangBhatia'
char_to_remove = 4

print(f'String after removing {char_to_remove}th character is: {remove_nth_char(input_str,char_to_remove)}')