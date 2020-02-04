#!/usr/bin/env python

animal = "wombat"
number = 42.9
value = 23.5 / 6.99
print(animal, number, value, '\n')
print("next line")

print(animal, number, value, sep='')
print(animal, number, value, sep=':')
print(animal, number, value, sep=', ')

print(animal, number, end="|", sep='<>')
print(value, number, end="|", sep='<>')
print()
print("red", end='')
print("blue", end='')
print("green", end='')

print(value)

print("{:.3f}".format(value))
print("{:.1f}".format(value))
print("{:.10f}".format(value))

print(f"{value:.3f}")

city = 'Albany'
state = 'NY'
print(f"We are in {city}, {state}")
x = 5
print(f"2 times x is {2 * x}")


print("%.3f" % (value))

