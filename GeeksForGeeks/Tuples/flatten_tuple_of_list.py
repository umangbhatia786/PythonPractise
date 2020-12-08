#Python Program to flatten a tuple of list to tuple

def flatten_tuple(input_tuple):
    new_tuple = tuple()
    for val in input_tuple:
        new_tuple += tuple(val)

    return new_tuple

my_tuple_1 = ([5],[6],[7],[8])
my_tuple_2 = ([5,6,7],[9,10,11])

print(flatten_tuple(my_tuple_1))
print(flatten_tuple(my_tuple_2))

