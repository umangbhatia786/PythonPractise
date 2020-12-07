'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num1, num2):
    list1 = list(str(num1))
    list2 = list(str(num2))
    
    list1.sort()
    list2.sort()
    
    if list1 == list2:
        return True
    return False