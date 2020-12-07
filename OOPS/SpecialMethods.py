
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f'Human named {self.first} {self.last}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='New Born', last= self.last, age= 0)
        raise TypeError('Cannot add a non human entity to a human')

    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
        raise TypeError('Cannot multiply human with non int value')
