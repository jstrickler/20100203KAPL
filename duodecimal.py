#!/usr/bin/env python
from itertools import count

BASE = 12

class Duodecimal():
    def __init__(self, duodecimal):
        self._decimal = int(duodecimal, BASE)
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

    def __sub__(self, other):
        return Duodecimal(Duodecimal.to_duodecimal(
            self.decimal - other.decimal
        ))

    def __mul__(self, other):
        return Duodecimal(Duodecimal.to_duodecimal(
            self.decimal * other.decimal
        ))

    def __truediv__(self, other):
        return Duodecimal(Duodecimal.to_duodecimal(
            self.decimal // other.decimal
        ))

    def __floordiv__(self, other):
        return Duodecimal(Duodecimal.to_duodecimal(
            self.decimal // other.decimal
        ))

    @staticmethod
    def to_duodecimal(decimal):
        tmp_duodecimal = []
        max_duodecimal = Duodecimal.get_max_duodecimal(decimal)
        for power in range(max_duodecimal, -1, -1):
            power_value = BASE ** power
            digit_value = decimal // power_value
            decimal -= (digit_value * (BASE ** power))
            if digit_value == 11:
                digit = 'b'
            elif digit_value == 10:
                digit = 'a'
            else:
                digit = str(digit_value)
            tmp_duodecimal.append(str(digit))
            duodecimal = ''.join(tmp_duodecimal)
            if len(duodecimal) > 1:
                duodecimal = duodecimal.lstrip('0')
        return duodecimal


    @staticmethod
    def get_max_duodecimal(decimal):
        for i in count(0):
            if BASE ** i > decimal:
                break;
        return i

if __name__ == '__main__':
    x = Duodecimal('aaaa')
    print(x)
    print(x.decimal)
    print(x.value)
    y = Duodecimal('84')
    result = x + x
    print(result.value, result.decimal)
