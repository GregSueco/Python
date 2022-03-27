'''
W tym zadaniu sprawdzimy, jak zachowują się zmienne podczas modyfikowania ich wartości
W pierwszym przypadku zainicjuj zmienne a, b, c wartością 10. W tym celu wykonaj tylko
jedną instrukcję.
Wyświetl wartości zmiennych oraz ich identyfikatory
Następnie zmień wartość zmiennej a np. na 20
Ponownie wyświetl wartości zmiennych i ich identyfikatory
(identyfikator zmiennej a powinien się zmienić
'''
 
a=b=c=10
 
print(a, b, c)
print(id(a), id(b), id(c))
 
a=20
 
print(a, b, c)
print(id(a), id(b), id(c))
print('-----------------------------')
 
'''
Teraz wykonaj jeszcze raz te same czynności, co poprzednio ale z delikatną różnicą:
-zmienne a, b i c mają mieć przypisaną wartość w postaci listy, np. [1,2,3]
-modyfikacja zmiennej a ma polegać na dodaniu do listy a nowego elementu, np. liczby 4
(identyfikator zmiennej a powinien być teraz taki sam jak b i c, dodatkowo zmieni się jednocześnie lista w zmiennych b i c
'''
 
a=b=[1,2,3]
b.append(4)
print(a)
print(a, b, c)
print(id(a), id(b), id(c))
 
a.append(4)
 
print(a, b, c)
print(id(a), id(b), id(c))
print('-----------------------------')
 
'''
Dlaczego tak się stało?
W pierwszym przykładzie a, b, c były wskaźnikami do komórki pamięci, w której była zapisana liczba, czyli końcowa wartość
W drugim przykładzie a, b, c to wskaźnik do komórki pamięci, w której jest lista. Lista jest wskaźnikiem do elementów tej listy. Kiedy dodajesz nowy element do listy, nie modyfikujesz podstawowej komórki pamięci z listą, dlatego id się nie zmienił
'''
 
'''
Uwaga - tu można się spodziewać, że w różnych wersjach Pytona uzyskamy różne wyniki, ale...
Do zmiennej x przypisz wartość 10
Do zmiennej y przypisz wartość 10 (użyj przypisań w dwóch osobnych liniach!)
Wyświetl id tych zmiennych
(chociaż mamy do czynienia z dwoma niezależnymi zmiennymi, to optymalizator pythona nadał im ten sam id)
'''
 
x=10
y=10
print(id(x), id(y))
 
'''
Do zmiennej y przypisz wartość y plus 1 minus 1.
Sprawdź identyfikatory zmiennych x i y
(identyfikatory nadal powinny być takie same, tzn. optymalizator poradził sobie z prostym działaniem + 1 - 1)
'''
 
y = y + 1 - 1
print(id(x), id(y))
print('-----------------------------')
 
'''
Powtórz operację dodawania i odejmowania od y, ale tym razem dodaj i odejmij wartość 1234567890
Sprawdź identyfikatory zmiennych x i y
(identyfikatory powinny być różne, tzn. optymalizator nie rozpoznał, że zmienne mają nadal te same wartości)
'''
 
y = y + 1234567890 - 1234567890
print(id(x), id(y))
print(x,y)
print('-----------------------------')