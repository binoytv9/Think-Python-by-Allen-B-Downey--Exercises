from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
	self.ranks={}
	for card in self.cards:
		self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
	self.rank_hist()
	for val in self.ranks.values():
		if val >= 2:
			return True
	return False

    def has_twopair(self):
	self.rank_hist()
	pair=0
	for val in self.ranks.values():
		if val >= 2:
			pair+=1
		if pair>=2:
			return True
	return False

    def has_3ofakind(self):
	self.rank_hist()
	for val in self.ranks.values():
		if val >= 3:
			return True
	return False

    def has_4ofakind(self):
	self.rank_hist()
	for val in self.ranks.values():
		if val >= 4:
			return True
	return False

    def has_fullhouse(self):
	return self.has_3ofakind() and self.has_pair()

    def rank_sort(self):
	self.cards.sort(key=lambda x: x.rank)

    def has_straight(self):
	rank_list=[]
	self.rank_sort()
	for card in self.cards:
		rname=Card.rank_names[card.rank]
		sname=Card.suit_names[card.suit]
		if rname not in rank_list:
			rank_list.append(rname)
	for i in range(len(rank_list)-5):
		if ''.join(rank_list[i:i+5]) in 'Ace2345678910JackQueenKingAce':
			return True
	return False

    def has_straightflush(self):
	self.d={}
	self.rank_sort()
	for card in self.cards:
		self.d.setdefault(Card.suit_names[card.suit],[]).append(Card.rank_names[card.rank])
	for key in self.d:
		if len(self.d[key]) >= 5:
			for i in range(len(self.d[key])-5):
				if ''.join(self.d[key][i:i+5]) in 'Ace2345678910JackQueenKingAce':
					return True
	return False
				
    def classify(self):
	methods=['has_straightflush', 'has_4ofakind', 'has_fullhouse', 'has_flush', 'has_straight', 'has_3ofakind', 'has_twopair', 'has_pair']
	for method in methods:
		if getattr(self,method)():
			self.label=method
			return


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    """
    hand=PokerHand()
    hand.add_card(Card(1,1))
    hand.add_card(Card(2,3))
    hand.add_card(Card(2,4))
    hand.add_card(Card(2,6))
    hand.add_card(Card(2,5))
    hand.add_card(Card(2,10))
    hand.add_card(Card(2,7))
    print hand
    """

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print 'has pair : ',hand.has_pair()
        print 'has 2 pair : ',hand.has_twopair()
        print 'has 3 of a kind : ',hand.has_3ofakind()
        print 'has straight : ',hand.has_straight()
        print 'has flush : ',hand.has_flush()
        print 'has full house : ',hand.has_fullhouse()
        print 'has 4 of a kind : ',hand.has_4ofakind()
        print 'has straight flush :',hand.has_straightflush()
        hand.classify()
        print hand.label
        print ''
