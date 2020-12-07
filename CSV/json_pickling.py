import jsonpickle

class Cat:

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

fluffy = Cat('Fluffy',3, 'Persian')

'''with open('CSV/cat.json','w') as file:
    frozen = jsonpickle.encode(fluffy)
    file.write(frozen)'''

with open('CSV/cat.json') as file:
    content = file.read()
    unfrozen = jsonpickle.decode(content)
    print(unfrozen)

