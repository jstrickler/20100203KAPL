#!/usr/bin/env python
from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call ancestor's method
        joker1 = 'J1', "Joker"
        joker2 = 'J2', 'Joker'
        self._cards.append(joker1)
        self._cards.append(joker2)


