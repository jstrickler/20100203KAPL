#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('computer_people.xml')

print(doc)
root = doc.getroot()
print(root)
for person in root:
    for field in person:
        print(field.text)
print('-' * 60)

for person in root.findall('person'):
    first_name = person.findtext('first_name')
    print(first_name)
print('-' * 60)

for person in doc.findall('.//person'):
    for field in 'first_name', 'last_name':
        print(field, person.findtext(field))
    print('---')


