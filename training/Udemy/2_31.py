ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']


#connections = [(s,d) for s in ports for d in ports]
#print(connections)

gen = ((s,d) for s in ports for d in ports if s != d and s < d)

iteration = 0

for x in gen:
    print(x) 
    iteration+=1
print("I listed all elements, a total of {}".format(iteration))   
   