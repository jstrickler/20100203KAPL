#!/usr/bin/env python
from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        knight_name, title, color, quest, comment = line.split(':')
        knight_info[knight_name] = title, color, quest, comment

print(knight_info['Arthur'], '\n')
pprint(knight_info)
print()

#    key,  value  in ANY_DICT.items()
for knight_name, data in knight_info.items():
    print(data[0], knight_name)
print()

# print(knight_info.items())

