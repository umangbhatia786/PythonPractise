class FBUser:

    active_users = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'User with name {self.first_name} {self.last_name} and age as {self.age} years'

    def get_full_user_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_user_initials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'

    def is_senior(self):
        return self.age >= 65

    def logout_user(self):
        FBUser.active_users -= 1
        return f'{self.first_name} {self.last_name} has been logged out'

    @classmethod
    def get_active_users(cls):
        return f'There are currently {cls.active_users} right now'

        
