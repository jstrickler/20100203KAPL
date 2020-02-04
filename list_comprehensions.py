#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

#  [EXPR for VAR ...  in ITERABLE if COND ...]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f2 =[]
for f in fruits:
    if f.startswith('p'):
        f2.append(f.upper())


f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

f4 = [f for f in fruits if len(f) > 8]
print("big_fruits:", f4, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [float(n) * 2 for n in nums if n > 300]
print("n1:", n1, '\n')

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

products = [p[2] for p in people]
print("products:", products, '\n')

names = [f"{p[0]} {p[1]}" for p in people if p[-1] > '1955-00-00']
print(names, '\n')

# NEW_LIST = [EXPR for VAR in ITERABLE]

# NEW_LIST = [EXPR for VAR in ITERABLE if COND]

fgen = (f.upper() for f in fruits)
print(fgen)
for fruit in fgen:
    print(fruit)
print()

fgen = (f.upper() for f in fruits)
trimmer = (f[:3] for f in fgen)
print(fgen)
print(trimmer)
for fruit in trimmer:
    print(fruit)

