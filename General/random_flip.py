from random import choice

def flip_coin():
	return choice(['Heads', 'Tails'])

result = flip_coin()

print(f'You got {result}')