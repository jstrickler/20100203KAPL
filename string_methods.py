#!/usr/bin/env python

actor = "Chris Hemsworth"
print(len(actor))

#  pkg.mod
#  mod.name
#  mod.method()
#  mod.obj
#  mod.obj.method()

#     obj.method()
print(actor.upper())
a = actor.upper()
print(a)
print(actor)

#  A-Z a-z 0-9 _

#        mod.var
#  print(foo.bar + 9)
print(actor.title())
print(actor.capitalize())
print(actor.lower())

print(actor)
print(actor.count('h'))
m = "Mississippi"
print(m.count('iss'))
print(actor.count("H"))
print(actor.lower().count('h'))
print(actor.startswith("Chris"))
print(actor.startswith("Liam"))
print(actor.replace('h', ''))
print("Hem" in actor)
print("Haw" in actor)
print(actor.index("wort"))

print(actor)
print(actor.replace("Chris", "Liam"))

s = "     All my exes live in Texas      "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()


s = "xyxxyyxxxyyyAll my exes live in Texasxxxyyyxxyyxy"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()

s = "Knolls:Labs:Schenectady:NY"

fields = s.split(':')
print(fields)
print("/".join(fields))
print(fields[0] + '/' + fields[1] + '/' + fields[2])

s = "This is a test"
print(s.split())


