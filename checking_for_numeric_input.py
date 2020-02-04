#!/usr/bin/env python

while True:
    raw_number = input("Enter a number: ")
    if raw_number == 'q':
        break
    try:
        number = float(raw_number)
    except ValueError as err:
        print(err)
        continue

    print(number * 5)
