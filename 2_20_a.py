import urllib.request
import os
 
data_dir = 'c:/temp'
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://wp.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
 
for page in pages:
 
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
 
        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve (page["url"], path)
        print('...done')
        
    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break
 
else:
    print('All pages downloaded successfully!!!')
 