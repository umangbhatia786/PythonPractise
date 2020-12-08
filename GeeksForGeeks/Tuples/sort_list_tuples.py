#Python code to sort a list of Tuples according to 2nd element

def sort_list_tuples(input_list):
    return sorted(input_list, key= lambda x: x[1])

my_list = [(1,2), (2,3), (4,5)]

print(sort_list_tuples(my_list))