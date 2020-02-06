#!/usr/bin/env python
try:
    with open("DATA/wombats.txt") as wombats_in:
        for line in wombats_in:
            print(line.rstrip())
except OSError as err:
    print(err)


x = ['a', 'b', 'c']
try:
    print(x[5])
except IndexError as err:
    print(err)

values = 5, 8, 0, 9, 11, 'abc', 4
for v in values:
    try:
        result = 13.7 / v
    except ZeroDivisionError as err:
        print(err)   # print(str(err))
    except (ValueError, TypeError) as err:
        print(err)
        print(err.args)
        # exit()
    except Exception as err:
        print(err)
    else:
        print(result)
    finally:
        print("Blech")



print("All done.")

def grumpy(x):
    print("starting...")
    raise ValueError("Bad value! No biscuit!", x)
    print("ending...")


try:
    grumpy(10)
except ValueError as err:
    print(err.args[0])
    print("Bad value was", err.args[1])

