#Python Code to flatten dictionary of key-value pair pairing the equal index elements together

def flatten_dict(input_dict):
    return dict(zip(input_dict['month'], input_dict['name']))

test_dict = {'month' : [1, 2, 3], 
             'name' : ['Jan', 'Feb', 'March']} 

print(flatten_dict(test_dict))