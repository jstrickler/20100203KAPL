#!/usr/bin/env python

from fortranvars import FortranVars

f1 = FortranVars('spam.f')
f2 = FortranVars('ham.f')
f3 = FortranVars('eggs.f')

print(f1.variables)

class Animal:
    def move(self):
        print("moving...")

a1 = Animal()
a1.move()
a2 = Animal()
a3 = Animal()

class Canid(Animal):
    def bark(self):
        print("Woof! Woof!")

d = Dog()
d.bark()
d.move()

# from president import President
# p = President(26)
# print(p.first_name)
