#!/usr/bin/env python

i = 0
while i < 5:
    print(i)
    i += 1   # i = i + 1
print()

print("Welcome to the file processing facility")

while True:
    file_name = input("Please enter the file to process (q to quit): ")
    if file_name == 'q':
        break    # exit loop
    if file_name == '':
        continue # go back to top
    print(f"I am happily processing {file_name} for you")

