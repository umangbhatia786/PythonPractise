class GrumpyDict(dict):

    def __repr__(self):
        print('NONE OF YOUR BUSINESS!')
        return super().__repr__()

    def __missing__(self, key):
        print(f'You want {key}, well it ain\'t here')
        
    def __setitem__(self, key, value):
        print('What the hell! You want to change the dictionary')
        print('Ok bruh, Fine...Whatever!')
        return super().__setitem__(key,value)

data = GrumpyDict({'name': 'Umang', 'age': 26, 'city': 'Kanpur'})
print(data)
print(data['sun_sign'])
data['city'] = 'Pune'
print(data)

