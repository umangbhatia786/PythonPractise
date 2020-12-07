class Human:

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	#Alternate way of getter and setter i.e by making properties
	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, new_age):
		if new_age >=0:
			self._age = new_age
		else:
			raise ValueError('Age value cannot be set to a negaitive value')

	@property
	def full_name(self):
		return f'{self.first} {self.last}'



	
h1 = Human('Umang', 'Bhatia', 26)
print(f'age is {h1.age}')
h1.age = 25
print(f'new age is {h1.age}')