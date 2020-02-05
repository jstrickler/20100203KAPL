#!/usr/bin/env python
from itertools import count

class Duodecimal():
    def __init__(self, duodecimal):
        self._decimal = int(duodecimal, 12)
        self._duodecimal = duodecimal

    @property
    def decimal(self):
        return self._decimal

    @property
    def value(self):
        return self._duodecimal

    def __add__(self, other):
        return Duodecimal(Duodecimal.to_duodecimal(
            self.decimal + other.decimal
        ))

    @staticmethod
    def to_duodecimal(decimal):
        duodecimal = []
        max_duodecimal = Duodecimal.get_max_duodecimal(decimal)
        for power in range(max_duodecimal, 0, -1):
            power_value = 12 ** power
            digit_value = decimal // power_value
            decimal -= (digit_value * (12 ** power))
            if digit_value == 11:
                digit = 'b'
            elif digit_value == 10:
                digit = 'a'
            else:
                digit = str(digit_value)
            duodecimal.append(str(digit))
        return ''.join(duodecimal).lstrip('0')


    @staticmethod
    def get_max_duodecimal(decimal):
        for i in count(0):
            if 12 ** i > decimal:
                break;
        return i

if __name__ == '__main__':
    x = Duodecimal('abab')
    print(x)
    print(x.decimal)
    print(x.value)
    y = Duodecimal('a')
    print((x + y).value)
