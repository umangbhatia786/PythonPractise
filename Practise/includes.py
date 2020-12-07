'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(collection, value, start=None):
    flag = True
    if type(collection) == dict:
        if value not in collection.values():
            flag = False
    else:
        if start:
            if value not in collection[start:]:
                flag = False
        else:
            if value not in collection:
                flag = False
    return flag
    