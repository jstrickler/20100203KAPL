#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for fruit in fruits:
    # fruit = next(fruits)  # get next element of fruits
    print(fruit.upper())

city = "Watervliet"
for ch in city:
    print(ch)
print()

for fruit in fruits[:10]:
    print(fruit[:3].upper())
print()

for fruit in fruits[:10]:
    print(fruit.upper())
print()

# for VAR in ITERABLE:
#    # use VAR

fmt = "I am {}"
print(fmt.format("Groot"))
for name in "Manny", "Moe", "Jack":
    print("I am {}".format(name))  # f"I am {name}"
print()

city = 'Albany'
state = 'New York'
a = 'apple'
b = 'banana'
print("{} is in {}".format(a, b))
print(f"{city} is in {state}")

x = "wombat"
a1 = "abc"     # just a string
a2 = r"abc\n"   # raw string
a3 = f"abc {x}"  # formatted string
a4 = b"abc"   # byte string





