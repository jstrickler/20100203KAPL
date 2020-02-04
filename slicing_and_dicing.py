#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(len(fruits))

print(fruits[0], fruits[9], fruits[-1])

print(fruits[0:5])  # first 5
print(fruits[7:12]) # 7 through 11
print(fruits[:5])   # first 5
print(fruits[18:])  # 18 to end
print(fruits[-5:])  # last 5
print(fruits[:11:2])  # every other one through index 10

#  SEQUENCE[0:len(SEQUENCE):1]
x = fruits[::]

actor = 'Chris Hemsworth'
print(actor[:5], actor[6:9], actor[-5:])
print(actor[::2])
print(actor[1::2])
