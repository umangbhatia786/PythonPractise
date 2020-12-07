class Animal:

	def __init__(self, name, species):
		self.name = name
		self.species = species

	def make_sound(self, sound):
		print(f'{self.name} says {sound}')



class Cat(Animal):
	
	def __init__(self, name, species, breed, toy):
		super().__init__(name, species)
		self.breed = breed
		self.toy = toy


	def play(self):
		print(f'{self.name} plays with {self.toy}')


cat1 = Cat('Meaow', 'Cat','Persian', 'Furball')
print(cat1.play())

