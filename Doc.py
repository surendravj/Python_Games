# Code for deck of cards  game or poker

from random import shuffle


class card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.suit} of {self.value}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Shades']
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [card(suit, value) for suit in suits for value in values]
        # print(self.cards)

    def __repr__(self):
        return f"{self.count()} cards in the deck"

    def count(self):
        return len(self.cards)

    def _deal(self, no_cards_removed):
        count = self.count()
        actual_cards = min(count, no_cards_removed)
        # return f"The number of cards removed is {actual_cards}"
        if(count == 0):
            raise ValueError('All cards are removed')
        cards = self.cards[-actual_cards:]
        self.cards = self.cards[:-actual_cards]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if(self.count() < 52):
            raise ValueError("Insufficient cards to shuffle")
        shuffle(self.cards)

        return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
print(hand)
print(d.cards)
