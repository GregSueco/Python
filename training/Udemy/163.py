"""
Administrator systemu chciałby wiedzieć, ile plików i katalogów znajduje się w określonym katalogu. Słyszał, że da się to zrobić w Pythonie
 i w sumie ma racje...

Zaimportuj moduł os i itertools

Napisz generator scantree, który:

jako argument przyjmie ścieżkę do początkowego katalogu path

następnie dla każdego obiektu zwracanego przez os.scandir:
(zobacz dokumentację - https://docs.python.org/3/library/os.html#os.scandir - obiekty zwracane przez os.scandir to obiekty klasy os.DirEntry 
- https://docs.python.org/3/library/os.html#os.DirEntry)

jeżeli obiekt ten jest katalogiem, czyli metoda obiektu is_dir() zwraca True

zwraca ten obiekt korzystając z yield

wywołuje rekurencyjnie scantree dla tego katalogu

jeżeli obiekt jest plikiem, czyli metoda obiektu is_dir() zwraca False

zwraca ten obiekt korzystając z yield

Przetestuj działanie tej funkcji na wybranym przez siebie nie za dużym katalogu:

do zmiennej listing zapisz wynik wywołania scantree wskazując argumentem na wybrany katalog

następnie przejdź przez listing pętlą for i dla każdego obiektu wyświetl informację o tym czy jest to plik czy katalog oraz pełną ścieżkę do 
tego pliku/katalogu

Korzystając z funkcji groupby z modułu itertools wyświetl informację o ilości katalogów i plików w wybranym przez ciebie katalogu bazowym.
Pamiętaj o ponownym utworzeniu zmiennej listing posortowaniu obiektu listing
"""

import itertools
import os

def scanTree(path):
    with os.scandir(path) as ls:
        for item in ls:
            if item.is_dir():
                yield(item)
                yield from scanTree(item.path)
            else:
                yield(item)
            
listing = scanTree(r'C:\temp')
listing = sorted(listing, key=lambda e: e.is_dir())
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)
for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))

 #for key,element in it.groupby(listing, key = lambda x: