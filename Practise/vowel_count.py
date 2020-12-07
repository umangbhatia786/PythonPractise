'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(word):
    return {char:word.lower().count(char) for char in word.lower() if char in 'aeiou'}

print(vowel_count('Elie'))