#Check If a String Contains only Binary 0 and 1

def check_binary(input_str):
    '''Python Function to Check if a String is made up of only Binary Digits'''
    char_set = set(input_str)
    return '1' in char_set and '0' in char_set and len(char_set) == 2

str1 = '0010110012'

if check_binary(str1):
    print('Accepted!')
else:
    print('Not Accepted!')

