class Card:

	allowed_suit = ['Hearts','Diamonds','Clubs','Spades']
	allowed_value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

	def __init__(self, suit, value):
		if suit not in Card.allowed_suit:
			raise ValueError(f'{suit} is not a valid suit value')
		elif value not in Card.allowed_value:
			raise ValueError(f'{value} is not a valid card value')

		self.suit = suit
		self.value = value

	def __repr__(self):
		return f'{self.value} of {self.suit}'

		