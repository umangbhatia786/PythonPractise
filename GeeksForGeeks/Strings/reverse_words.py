#Python Code to Reverse words in a given String in Python

def reverse_words(input_str):
    return ' '.join([word [::-1] for word in input_str.split(' ')])

my_str = 'My Name is Umang'

print('Revered String is: ')
print(reverse_words(my_str))