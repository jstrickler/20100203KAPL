#!/usr/bin/env python
import sys

BASE_NAME = 'DATA'

x = 100  # global


if x > 50:
    name = "Bob"

print(name)

def spam():
    x = 0
    for i in range(5):
        x += 1

    m = 100000  # local
    print("in spam(): x =", x)
    y = 42  # local
    print("in spam(): y is", y)

spam()

print("in main: x is", x)
# print(y)

