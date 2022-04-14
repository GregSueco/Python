"""Oto klasa parsująca zawartość pliku CSV:"""

import csv
 
with open('c:/temp/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(next(csvreader))
    #print(next(csvreader))
    #print(next(csvreader))
    #for row in csvreader:
    #    print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break
    print("Everything was processed")



"""
Ta klasa jest "iterable" - można obiekt csvreader przetwarzać pętlą for, jednak czy ta klasa ma iterator?

Przygotuj jakikolwiek plik CSV (przykładowa zawartość może być wzięta z ramki na dole tego zadania)

Uruchom program i zobacz jak on aktualnie dziala

Zakomentuj dwie ostatnie linie skryptu (pętla for)

Najpierw "próbnie" spróbuj pobrać zawartość kolejnych linijek pliku CSV korzystając z kilku ręcznych wywołań funkcji next

Jeśli funkcja next działa, to.... obiekt ma swój iterator i nie trzeba korzystać z funkcji iter()

Napisz pętlę while wykonującą się w nieskończoność

w tej pętli napisz try/except pobierający kolejny element z obiektu csvreader

jeśli dojdzie do błędu StopIteration, to przerwij wykonanie pętli
Przykładowa zawartość pliku CSV:

Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10
"""