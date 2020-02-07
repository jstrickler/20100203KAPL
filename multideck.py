#!/usr/bin/env python
from carddeck import CardDeck

class MultiDeck(CardDeck):
    def __init__(self, dealer, number_of_decks):
        self._number_of_decks = number_of_decks
        super().__init__(dealer)

    def _make_deck(self):
        self._cards = []
        for i in range(self._number_of_decks):
            tmp = CardDeck('')
            self._cards.extend(tmp._cards)

