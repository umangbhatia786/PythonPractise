'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(input_list):
    return all([type(val) == list for val in input_list])

print(list_check([[],[1],[2,3]]))