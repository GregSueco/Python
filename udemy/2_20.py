import os
import urllib.request

data_dir = 'c:/temp/'

pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://onet.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} 
    ]

for page in pages:

    file = data_dir + page['name'] + '.html'
    url = page['url']
    #print(file)
    #print(url)

    try:
        urllib.request.urlretrieve(url,file)
    except:
        print("There was an error")
        break
else:
     print("Everything worked fine!")