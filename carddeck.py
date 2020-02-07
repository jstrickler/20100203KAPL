#!/usr/bin/env python
import random

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer_name):
        self._dealer_name = dealer_name
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards

    # instance method
    def shuffle(self):
        random.shuffle(self._cards)

    # instance method
    def draw(self):
        return self._cards.pop()


    # getter property
    @property
    def dealer_name(self):
        return self._dealer_name

    # setter property
    @dealer_name.setter
    def dealer_name(self, dealer_name):
        if isinstance(dealer_name, str):
            self._dealer_name = dealer_name
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    def __add__(self, other):
        tmp = type(self)(self.dealer_name)
        tmp._cards = self._cards + other._cards
        return tmp
