#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for first_name, last_name, product, dob in sorted(people):
    print(first_name, last_name)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print('-' * 60)

def to_lower(fruit):
    return fruit.lower()

f2 = sorted(fruits, key=to_lower)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def len_and_name(f):
    #      key 1    key 2
    return len(f), f.lower()

f4 = sorted(fruits, key=len_and_name)
print("f4: {}\n".format(f4))

def wacky(s):
    return s[-2]

f5 = sorted(fruits, key=wacky)
print("f5: {}\n".format(f5))

def by_dob(p):
    return p[3]

for first_name, last_name, product, dob in sorted(people, key=by_dob, reverse=True):
    print(first_name, last_name, dob)
print()

def ln_fn(x):
    return x[1], x[0]

for first_name, last_name, product, dob in sorted(people, key=ln_fn):
    print(first_name, last_name, dob)
print()

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'YYC': 'Calgary',
    'YOW': 'Ottawa',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print('-' * 60)

def by_value(elem):
    return elem[1], elem[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print('-' * 60)

print(airports.items())


for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print('-' * 60)

# lambda VAR ...: RETURN_VALUE

f6 = sorted(fruits, key=lambda f: f.lower())
print("f6: {}\n".format(f6))
