#Python Code get list of uncommon words from 2 different strings

def get_uncommon_words(input_str1, input_str2):
    '''Function that uses List Comprehension to get uncommon words out of two strings'''
    word_list_1 = input_str1.split(' ')
    word_list_2 = input_str2.split(' ')

    return [word for word in word_list_2 if word not in word_list_1]

'''Testing the Code with Inputs Now'''
A = "Geeks for Geeks" 
B = "Learning from Geeks for Geeks"

print(get_uncommon_words(A,B))


