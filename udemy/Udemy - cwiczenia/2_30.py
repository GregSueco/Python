ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']


#connections = [(s,d) for s in ports for d in ports]
#print(connections)

connections_2 = [(s,d) for s in ports for d in ports if s != d if ]

print(connections_2)