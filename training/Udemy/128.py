"""
Rozpocznij zadanie od rozwiązania z poprzedniej lekcji (jeśli nie masz swojego, możesz skorzystać z mojego)

Obsłuż niezależnie następujące kategorie błędów:

requests.exceptions.ConnectionError - ten błąd łatwo sprowokujesz wpisując nieprawidłowy adres URL

PermissionError - ten błąd uzyskasz zaznaczając atrybut "tylko do odczytu" dla pliku spis.html

FileNotFoundError - może się pojawić w trakcie prób, gdy plik download.tmp nie będzie istniał, a wykonywać będzie się instrukcja kopiowania plików

Exception - ogólna obsługa błędów "na wszelki wypadek"

Obsługując błędy wyświetlaj po prostu komunikaty
"""

import requests
import os
import shutil
from os.path import exists
from stat import S_IREAD

 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
#file = os.chmod('spis.html', S_IREAD)
#print(file)
file = 'spis.html'
 
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

if exists(tmpfile_path):
    os.remove(tmpfile_path)
    
try: 
    save_url_to_file(url,tmpfile_path)    
    shutil.move(tmpfile_path,file_path)
except requests.exceptions.ConnectionError as e:
    print("Sorry to inform but there was a connection error: \n{}".format(e))
except PermissionError as e:
    print("Sorry there was an error related to read-only file: \n{}".format(e))
except FileNotFoundError as e:
    print("Sorry there was an error - file: {} does not exist: \n".format(file))
except Exception as e:
    print("Sorry to inform but there was an error: \n{}".format(e))
else: 
    print("Success!")
finally:
    if exists(tmpfile_path):
        os.remove(tmpfile_path)
        print('Temp file removed succesfully!')
