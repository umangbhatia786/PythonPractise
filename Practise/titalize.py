'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(sentence):
    words_list = sentence.split(' ')
    return ' '.join(['{}{}'.format(word[0].upper(), word[1:]) for word in words_list])