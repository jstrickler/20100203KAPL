#!/usr/bin/env python

alist = ['a', 'b', 'c']

# person = ('Bill', 'Gates', 'Microsoft')
person = 'Bill', 'Gates', 'Microsoft'

print(person[0], person[1])
print(person[-1])

# list, of, variables = ITERABLE
first_name, last_name, product = person


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
]
print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

for person in people:
    first_name, last_name, *_ = person
    print(first_name, last_name)
print()

for first_name, last_name, *products, dob in people:
    # first_name, last_name, product, dob = next(people)
    print(first_name, last_name, products, dob)
print()

place = ['Albany', 'NY']
city, state = place
a = "red"
b = "blue"
print(a, b)
a, b = b, a  # python trick :-)
print(a, b)
print()

city, state = 'Albany', 'NY'

cities = [['Durham', 'NC'], ('Albany', 'NY'), ('Austin', 'TX'),
          ('Pittsburgh', 'PA')]

for city, state in cities:
    print(f"{city} is in {state}")
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
print()

for first_name, last_name, *product in people[:3]:
    print(first_name, last_name, product)



