#!/usr/bin/python3

ctemps = [-40, 0, 37, 75, 100]

for c in ctemps:
    f = ((9 * c) / 5) + 32
    print(f"{c:5d} C is {f:6.1f} F")

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

clean_fruits = [(f, f.lower().strip()) for f in fruits]
for dirty, clean in clean_fruits:
    print(">{}< >{}<".format(dirty, clean))

