class Aquatic:

    def __init__(self, name):
        self.name = name

    def swim(self):
        return f'{self.name} can swim'

    def greet(self):
        return f'{self.name} sends you greetings from inside water.'

class Ambulatory:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return f'{self.name} is walking!'

    def greet(self):
        return f'{self.name} sends you greetings from land'

class Penguin(Ambulatory,Aquatic):

    def __init__(self, name):
        super().__init__(name)


'''In Python while doing multiple inheritance, the class inherited first is provided priority 
in super() and in methods  that are present in both the classes'''

joey = Penguin('Joey')
print(joey.walk())
print(joey.greet())

