#!/usr/bin/env python
"""
Examples of Python functions
"""
from typing import Union, Any, Dict

# msg = get_message()
# print(msg)
# print(get_message())
# print(get_message)  # not typical

def say_hello():
    """
    Output a greeting provided by the get_message() function

    :return: None
    """
    message = get_message()
    print(message)

def get_message():
    """
    Simple greeting

    :return: None
    """
    return "Hello, world"

say_hello()
say_hello()

def greet(whom: str) -> None:
    print("Hello,", whom)

greet("universe")
greet("Mom")
greet("Newman")
greet(1.234)

Numeric = Union[int, float]
def exp(x: Numeric, y: Numeric) -> Numeric:
    """
    Raise a number to a power

    :param x: Base
    :param y: Exponent
    :return: Numeric result
    """
    return x ** y

print(exp(4, 99))
print(exp(29340293842093, 0))

print(exp(2, .5))

def wacky(value: Any) -> Any:
    """A very wacky function"""
    pass

def doit(value: Dict[str, int]) -> None:
    """
    This function will do it

    :param value: Data -- keys are strings, values are ints
    :return: None
    """
    pass

result = exp(5, 6.8)


def process_files(value, *file_names):
    print("file_names:", file_names)
    for x in file_names:
        print("processing", x)
    print()

process_files(1.2, 'a.txt', 'b.txt')
process_files(1.2, 'a.txt', 'b.txt', 'wombat.txt', 'weasel.txt', 'mango.txt')

process_files(5)

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    print()

config(file_name='wombat.txt', country='Burkina Faso',
       soup="avgolemono")

def wackiest(a, b, *c, **d):
    print("a:", a)
    print("b:", b)
    print("c:", c)
#    print("d:", d)
    print("-" * 10)

wackiest(1, 2)
wackiest(1, 2, 3, 4, 5, 6)
wackiest(1, 2, 3, 4, 5, 6, animal="wombat",
         nerd="Sheldon")

