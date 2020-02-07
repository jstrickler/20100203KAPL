#!/usr/bin/env python
import lxml.etree as ET

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

root = ET.Element('people')
for first_name, last_name, product, dob in people:
    p = ET.SubElement(root, 'person', dob=dob)
    ET.SubElement(p, "first_name").text = first_name
    ET.SubElement(p, "last_name").text = last_name
    product_element = ET.SubElement(p, "product")
    product_element.text = product


xml = ET.tostring(root, pretty_print=True).decode()
print(xml)

doc = ET.ElementTree(root)
doc.write('computer_people.xml', xml_declaration=True, pretty_print=True)
