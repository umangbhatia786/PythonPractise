class User:
	active_users = 0

	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users +=1

	def __repr__(self):
		return f'{self.first} {self.last} with age {self.age}'
		
	def get_full_name(self):
		return f'{self.first} {self.last}'

	def get_initials(self):
		return f'{self.first[0]}.{self.last[0]}'

	def is_senior(self):
		return self.age >=65

	def logout_user(self):
		User.active_users -= 1
		return f'{self.first} {self.last} has logged out'

	@classmethod
	def get_active_users(cls):
		print(f'There are currently {cls.active_users} active users right now')

	@classmethod
	def from_string(cls, data_string):
		first, last, age = data_string.split(',')
		return cls(first,last,int(age))

class Moderator(User):
	total_mods = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_active_mods(cls):
		return f'There are currently {cls.total_mods} active Moderators'
	def remove_post(self):
		return f'{self.get_full_name()} removed a post from {self.community} community'


# user1 = User('Umang','Bhatia', 26)
# print(user1.get_full_name())
# print(user1.get_initials())

jasmine = Moderator('Umang', 'Bhatia', 26, 'Python')
print(jasmine.get_full_name())
print(jasmine.remove_post())

