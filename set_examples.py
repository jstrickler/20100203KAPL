#!/usr/bin/env python
molly_visited = ['Ireland', 'Canada', 'US',
                 'Djibouti', 'Brazil', 'Burkina Faso']

fran_visited = ['Canada', 'France', 'Taiwan', 'US',
        'Brazil']


molly = set(molly_visited)
fran = set(fran_visited)

print("Both:", molly & fran)       # intersection
print("Just one:", molly ^ fran)   # Xor
print("Either one:", molly | fran) # union
print("Just Molly:", molly - fran)
print("Just Fran:", fran - molly)

food = ['spam', 'poutine', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'eggs', 'spam',
        'poutine', 'poutine', 'poutine']

unique_food = set(food)
print(unique_food)

ulist = sorted(unique_food)
print(ulist)


my_set = {'red', 'blue', 'blue', 'red', 'green'}
print(my_set)
my_dict = {'red': 5, 'blue': 6}
