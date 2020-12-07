#Python Code to print all duplicates from a list

def get_duplicates_list(input_list):
    duplicate_set = {val for val in input_list if input_list.count(val)>1}
    if len(duplicate_set)>1:
        return duplicate_set
    return 'No duplicates!'

my_list = [1,3,1,2,2,5,5,6,7,7,7,8]

print(get_duplicates_list(my_list))
