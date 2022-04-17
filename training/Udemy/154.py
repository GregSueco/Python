"""
Pracujesz nad kulinarną wersją sztucznej inteligencji, która tworzy nowy smak. Algorytm łączy ze sobą 3 smaki:  
słodki, kwaśny, słony. Musisz przygotować funkcję, która będzie losowała proporcje smaków.  U nas KSI (kulinarna sztuczna inteligencja)
podejmie 10 prób wymieszania smaków. Wobec tego należy 10 razy wylosować 3 liczby z zakresu 1 - 100, ale liczby te mają się sumować do 100.

Jeśli potrzebujesz dokładniejszych instrukcji, oto one:

Zaimportuj moduł random

Zdefiniuj generator random_with_sum, który:

Przyjmuje argumenty:

number_of_values - ilość wartości do wylosowania (u nas 3)

asserted_sum - założona suma, do której mają się zsumować wylosowane liczby

Zainicjuj zmienne:

trial - na zero - będzie to licznik prób losowania wartości nim uda się wylosować liczby sumujace się do asserted_sum (u nas 100)

numbers - tablica licząca number_of_values wartości (u nas 3)

W nieskończonej pętli while

zwiększ trial o 1

dla liczby i od 0 do number_of_values wylosuj liczby z zakresu 1-100 i zapisz je w tablicy numbers

jeżeli wylosowane liczby sumują się do asserted_sum, to

zwróć tuple (trial, numbers) - skorzystaj z funkcji yield

wyzeruj zmienną trial

W swoim programie:

w pętli for wykonywanej 10 razy

zapisz do tuple (number_of_trials, numbers) kolejną wartość generowaną przez random_with_sum(3, 100)

wyświetl tą wartość

"""
#import random
#
#def random_with_sum(number_of_values,asserted_sum):
#    trial = 0
#    numbers = []
#
#    while True:
#        trial += 1
#
#        for i in range(0,number_of_values):
#            numbers.append(random.randrange(1,100))
#            
#        if sum(numbers) == asserted_sum: 
#            yield
        
import random
 
 
def random_with_sum(number_of_values, asserted_sum):
 
    trial = 0
    numbers = list(range(number_of_values))
    print('List initiated: ')
    print(numbers)
    while True:
 
        trial +=1
        for i in range(number_of_values):
            print('List after change: ')
            numbers[i] = random.randint(1, 10)
            print(numbers)
 
        if sum(numbers) == asserted_sum:
            print('Tuple to be yielded:')
            yield((trial, numbers))
            trial = 0
 
 
for i in range(1):
    (number_of_trials, numbers) = next(random_with_sum(3, 10))
    print(number_of_trials, numbers)
