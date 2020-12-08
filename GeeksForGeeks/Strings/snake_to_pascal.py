#Python Program to convert Snake Case to Pascal Case

def snake_to_pascal(input_str):
    return ''.join([word.title() for word in input_str.split('_')])

my_str = 'geeks_for_geeks'
print(snake_to_pascal(my_str))