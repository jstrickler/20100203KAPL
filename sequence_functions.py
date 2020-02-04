#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

# fruits = ["pomegranate", "cherry", "apricot", "Apple",
# "lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
# "Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
# "elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(fruits), len(nums))
print(min(fruits), max(fruits))
print(min(nums), max(nums))
print(sum(nums))

print(sorted(fruits))
print(sorted(nums))
actor = 'Chris Hemsworth'


x = ['10', '22', '45']

for num in x:
    print(3 * num, 3 * int(num))
print()

for fruit in reversed(fruits):
    print(fruit)
print()

rf = reversed(fruits)
print(type(rf))
print(rf)

print("round 1:")
for fruit in rf:
    print(fruit)
print()

print("round 2:")
for fruit in rf:
    print(fruit)
print()

rf = reversed(fruits)
print(next(rf))

rf_list = list(rf)
print(rf_list)

rf_list = list(rf)
print(rf_list)

people = ['Manny', 'Moe', 'Jack']
cities = ['Albany', 'Durham', 'Houston']
states = ['NY', 'NC', 'TX']

places = zip(people, cities, states)

print(places, '\n')

for p in places:
    print(p)
print()

places = zip(people, cities, states)
for person, city, state in places:
    print("{} is from {}, {}".format(person, city, state))
print()

colors = ['red', 'blue', 'green']
values = [22, 42, 85, 99]

x = zip(colors, values)
print(x)
print(list(x), '\n')

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()

print(list(enumerate(fruits)), '\n')

values = ['a', 'b', 'c']
start_index = 1
for i, value in enumerate(values, start_index):
    print(i, value)
print()


