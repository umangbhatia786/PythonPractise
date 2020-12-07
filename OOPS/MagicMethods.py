from copy import copy
class Human:
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last
        self.age = age

    def __repr__(self):
        return f'Human with name {self.first} {self.last} and age as {self.age} years'

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='NewBorn', last = self.last, age = 0)
        else:
            raise TypeError('Cannot add a non human entity to a human')

    def __mul__(self, number):
        if isinstance(number, int):
            return [copy(self) for i in range(number)]
        else:
            raise TypeError('Cannot multiply to a non integer value')


j = Human('Jessica', 'Jones', 26)
k = Human('Matt', 'Reeves', 28)

''' Using such magic methods allows us to add, multiply or get length og objects '''

print(len(j))
print(j + k)
print(j * 3)
