#!/usr/bin/env python

d1 = dict()
d2 = {'Mary': 18, 'Fred': 17, 'Mohamed': 16}
d3 = {}

keys = ['Albany', 'Detroit', 'Buffalo']
values = ['NY', 'MI', 'NY']
d4 = dict(zip(keys, values))
print(d1)
print(d4)

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'YYC': 'Calgary',
    'YOW': 'Ottawa',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
}

print(airports['MCO'])
print(airports['YYC'])

airports['ALB'] = 'Albany'
airports['ELM'] = 'Elmira'
print(airports, '\n')
del airports['EWR']
print(airports, '\n')
print(len(airports), '\n')

for k in 'IAD', 'DIA', 'AID', 'ELM':
    print(k, k in airports)
print()

airports['IAD'] = "Dulles"
airports['IAD'] = 'Wombat'

print(airports)


print([key for key in airports.keys() if key.startswith('S')])


print(airports.get('LAX'))
print(airports.get('LAX', 'NOT FOUND'))
print(airports.get('RDU'))
print('-' * 60)

for abbr, airport in airports.items():
    print(abbr, airport)
print('-' * 60)

for abbr, airport in sorted(airports.items()):
    print(abbr, airport)
