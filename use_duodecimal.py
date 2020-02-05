#!/usr/bin/env python
from duodecimal import Duodecimal
fmt = "{:3}  {:>8s} {:8d}"
print("  Duodecimal Decimal")
x = Duodecimal('aaaa')
print(fmt.format('x', x.value, x.decimal))

y = Duodecimal('bbbb')
print(fmt.format('y', y.value, y.decimal))

result = x + y
print(fmt.format('x+y', result.value, result.decimal))

result = x - y
print(fmt.format('x-y', result.value, result.decimal))

result = x * y
print(fmt.format('x*y', result.value, result.decimal))

result = x / y
print(fmt.format('x/y', result.value, result.decimal))
