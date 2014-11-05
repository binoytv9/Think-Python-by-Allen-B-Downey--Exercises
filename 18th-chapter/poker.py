class Card(object):
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank

	suit_names=['Clubs','Diamonds','Hearts','Spades']
	rank_names=[None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

	def __str__(self):
		return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])

	def __cmp__(self,other):
		t1=self.suit,self.rank
		t2=other.suit,other.rank
		return cmp(t1,t2)


class Deck(object):
	def __init__(self):
		self.cards=[]
		for suit in range(4):
			for rank in range(1,14):
				card=Card(suit,rank)
				self.cards.append(card)

	def __str__(self):
		res=[]
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self,card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()

	def move_cards(self,hand,num):
		for i in range(num):
			hand.add_card(self.pop_card())


class Hand(Deck):
	def __init__(self,label=''):
		self.cards=[]
		self.label=label


import random
"""
card1=Card(1,12)
print card1

card2=Card(2,1)
print card2

print card1>card2
"""

deck1=Deck()
card=deck1.pop_card()
hand=Hand('new hand')
hand.add_card(card)
print hand
