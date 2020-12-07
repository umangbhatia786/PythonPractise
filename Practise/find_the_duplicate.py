'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

'''def find_the_duplicate(input_list):
    unique_list = list(set(input_list))

    if len(input_list) == len(unique_list):
        return None
    else:
        num = 0
        for val in unique_list:
            if input_list.count(val) > 1:
                num = val
                break
        return num'''
        
def find_the_duplicate(input_list):
    count_dict = {val:input_list.count(val) for val in input_list}

    for k,v in count_dict.items():
        if v > 1:
            return k



print(find_the_duplicate([6,1,9,5,3,4,9]))