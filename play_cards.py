#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck
from multideck import MultiDeck

d1 = CardDeck('Fred')
print(d1)
print(type(d1))
# print(d1._dealer_name)  BAD PROGRAMMER! NO BISCUIT!
print(d1.dealer_name)   # .dealer_name is a property (not a func)
print(type(d1.dealer_name))

d1.dealer_name = "Waldo"   # CardDeck.dealer_name(d1, "Waldo")

try:
    d1.dealer_name = 1.2345
except TypeError as err:
    print(err)
else:
    print(d1.dealer_name)

d1.shuffle()
print(d1.cards)
print()

for i in range(5):
    print(d1.draw())
print()

print(d1.get_ranks())
print(CardDeck.get_ranks())

j1 = JokerDeck("Anna")
print(j1)
j1.shuffle()
print(j1.cards)

m1 = MultiDeck("Bob", 3)
print(m1.cards)

new_deck = d1 + j1
print(new_deck)
print(new_deck.cards)
