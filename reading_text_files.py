#!/usr/bin/env python

#  f = open("filename", "r")
#  f.close()

# read one line at a time
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

# read entire file into one string
with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("** RAW **")
    print(repr(contents))
    print("** COOKED **")
    print(contents)
print('-' * 60)

# read entire file into list of lines WITH n/l
with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

# read entire file into list of lines WITHOUT n/l
with open('DATA/mary.txt') as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
    print(all_lines)
print('-' * 60)

knight_names = []
with open('DATA/knights.txt') as knights_in:
    for line in knights_in:
        # print(line.rstrip().split(':'))
        name, *_ = line.split(':')
        knight_names.append(name)
print(knight_names)
print('-' * 60)
