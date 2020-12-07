from random import shuffle

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


class Deck:

	def __init__(self):
		suits = ['Hearts','Diamonds','Clubs','Spades']
		values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

		self.cards = [Card(suit,value) for suit in suits for value in values]

	def __repr__(self):
		return f'Deck of {self.count()} Cards'

	def __iter__(self):
		return iter(self.cards)

	def count(self):
		return len(self.cards)

	def _deal(self,number):
		count = self.count()
		actual = min(count, number)

		if count == 0:
			raise ValueError('All cards have been dealt')

		cards = self.cards[-actual:0]
		self.cards = self.cards[:-actual]

		return cards 

	def deal_hand(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

	def shuffle:
		if self.count() < 52:
			raise ValueError('Only full decks can be shuffled')

		return shuffle(self.cards)

		return self