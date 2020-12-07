'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(key_list, val_list):
    new_dict = {}
    for i in range(0,len(key_list)):
        try:
            new_dict[key_list[i]] = val_list[i]
        except IndexError:
            new_dict[key_list[i]] = None
    return new_dict

print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]))

   