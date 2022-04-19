"""
Wyobraź sobie, że jesteś artystą szukającym natchnienia... Chcesz skomponować przebój, ale nie masz pomysłu jaki...

Do dyspozycji masz 7 nutek:

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
Główny motyw ma się składać z 4 nutek. Wyświetl wszystkie możliwe układy składające się z 4 nutek. Podpowiem, że na ile znam się na muzyce, 
kolejność nutek ma znaczenie. Skorzystaj z odpowiedniej funkcji z modułu itertools

Korzystając ze wzoru opisanego tutaj:

https://pl.wikipedia.org/wiki/Wariacja_bez_powt%C3%B3rze%C5%84

policz ile jest takich potencjalnych kandydatów na przebój.

Uwaga: funkcja licząca silnię znajduje się w module math i nazywa się factorial. Funkcja licząca potęgę nazywa się pow

No cóż, nasz artysta przesłuchał wszystkie możliwości, ale nic nie wpadło mu w ucho. Zmieniamy więc założenie.
 Nutki mogą się powtarzać, a kolejność nadal ma znaczenie.  Podpowiem, że chodzi tu o 4-elementową wariację z powtórzeniami zbioru nutek.
  Skorzystaj z funkcji produkt modułu itertools. Policz też ile jest takich potencjalnych układów:

https://pl.wikipedia.org/wiki/Wariacja_z_powt%C3%B3rzeniami

Prawda, że życie artystów jest ciężkie?
"""

import itertools as it

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
progression = []

for n in it.permutations(notes,4):
    progression.append(n)

for p in progression:
    print(p)
    print('***********')
print(len(progression))

print('BREAK BREAK BREAK')

progression_with_repetition = []

for n in it.product(notes,repeat = 4):
    progression_with_repetition.append(n)

for p in progression_with_repetition:
    print(p)
    print('***********')
print(len(progression_with_repetition))