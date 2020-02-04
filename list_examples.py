#!/usr/bin/env python

a = 10
b = 20
c = 30
list1 = list()
list2 = [a, b, c]
list3 = [10, 20, 'abc', 30, True, ['a', 'b', 'c']]
list4 = [[1, 2, 3, 99], [5, 6], [7, 8, 9]]
print(list4[0])
print(list4[2])
print(list4[2][1])

#  print(list4[2[1]])
#  list4[2, 1]  OK in NUMPY only
#  []  getitem operator

x = [[[[[5], 6], 7], 8], 9]
print(x)

cities = ['Albany', 'Troy', 'Schenectady', 'Saratoga Springs',
        'Clifton Park', 'Hudson']

print(cities[0])
print(cities[5], cities[-1])
cities.append('Rotterdam')
print(cities)
more_cities = ['Cohoes', 'Watervliet', 'Slingerlands']

cities.extend(more_cities)
print(cities)
# cities.extend("Elmyra")
# print(cities)
cities.insert(0, 'Poughkeepsie')
print(cities)
cities.insert(3, 'Elmira')
print(cities)

del cities[8]
print(cities)

cities.remove('Clifton Park')
print(cities)

try:
    cities.remove('Brooklyn')
except ValueError as err:
    print(err)

# del  LIST.remove()  LIST.pop()

c = cities.pop()
print(c)
print(cities)
c = cities.pop(3)
print(c)
print(cities)

list5 = []
print(list5)
list6 = list()
print(list6)

list8 = "what the heck?"

x = ['a', 'b', 'c']
list7 = list(x)  # real copy (shallow)
print(list7)
list8 = x   # alias, not copy
x.append('huh?')
print(list8)
list8 = x.copy()
print(list8)

m = [1, 2, 3]
copy1 = list(m)
copy2 = m.copy()
copy3 = m[::]




