#Python code to remove empty list from a list

def remove_empty_list_from_list(input_list):
    return [val for val in input_list if val != []]

my_list = [[],1,2,3,[],6]

print(remove_empty_list_from_list(my_list))