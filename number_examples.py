#!/usr/bin/env python
import math

i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100
print(i1, i2, i3, i4)

# int float boolean complex

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.2093e15

c1 = 1.2J
c2 = 2.1j # etc
print(c1)
print(type(c1))

a = 22
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)
q, r = divmod(a, b)
print(q, r)

values = [5, 1, 18, 9, 2, 7]
print(min(values), max(values))

x = "123"
y = "    456     "
z = "DeadBeef"

print(x * 10, int(x) * 10)
print(y * 10, int(y) * 10)
print(z * 10, int(z, 16) * 10)

flags = "11010001"
print(int(flags, 2))

a = 123
print(str(a) * 5)
print(a * 5)
print(str(a))

