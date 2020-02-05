#!/usr/bin/env python
from collections import Counter

with open('DATA/words.txt') as words_in:
    first_letters = [w[0] for w in words_in]

print(len(first_letters))
print(first_letters[-200:])

counts = Counter(first_letters)
print(counts.most_common(5))
print(counts['x'])

