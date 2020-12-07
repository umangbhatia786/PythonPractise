class Pet:
	allowed = ['cat','dog','rat','rabbit','fish']

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f'You cannot have {species} as a Pet')
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in Pet.allowed:
			raise ValueError(f'You cannot set your pet as {species}')
		self.species = species


cat = Pet('meaow','cat')
dog = Pet('fluffy','dog')

