#!/usr/bin/env python

s1 = "spam\n"  # single-delimited
s2 = 'spam\n'
s3 = """spam\n"""  # triple-delimited
s4 = '''spam\n'''
s5 = r'spam\n'
print('spam\\n')  # NOT PYTHONIC


print(len(s1))
print("It's the Python way!")
print('It is the "Python" way!')
print("""It's the "Python" way!""")

query = """
select *
from test_run
where run_number == 1234
"""

print(s5)


