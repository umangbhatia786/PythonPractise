#To create a list of tuples with each tuple containing element and it's cube
from math import pow

def list_tuple_cubes(input_list):
    return [(val,int(pow(val,3))) for val in input_list]

my_list = [1,2,3,4,5]

print(list_tuple_cubes(my_list))