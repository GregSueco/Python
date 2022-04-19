"""
Liczba doskonała – liczba naturalna, która jest sumą wszystkich swych dzielników właściwych (to znaczy od niej mniejszych).

No to poszukajmy liczb doskonałych w przedziale od 1 - 10000. Oto funkcja wyznaczająca dzielniki liczby:

def get_factors(x):
 
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list
Przetestuj funkcję wyznaczając dzielniki liczby 20.

W zmiennej candidate_list zapisz liczby od 1 do 10000 (przetwarzanie będzie trochę trwało, więc możesz zacząć od mniejszej wartości np. 100)

W zmiennej filtered_list zapisz tylko te liczby z candidate_list, które są doskonałe

skorzystaj z funkcji filterfalse z modułu itertools

na każdym liczbie z listy candidate_list

sprawdzaj, czy suma liczb z listy zwróconej przez get_factors dla tej liczby jest różna od tej liczby

wynik skonwertuj do listy

Dla każdego elementu z listy filtered_list wyświetl tą liczbę oraz listę jej dzielników (ponownie wywołaj get_factors)



A teraz coś, czego nie było na lekcji VIDEO: islice

Obiekt islice jest stworzony w oparciu o generator.  Wiesz, że generatory często przypominają listy, a w listach można się odwoływać do podzbiorów za pomocą operacji cięcia (slice). Idea korzystania z operatora islice jest taka, że gerator wygeneruje liczby dopiero w momencie kiedy je wytniesz (operacja slice). 

Załóżmy, że poszukujemy liczb pierwszych do 10000. Do sprawdzenia czy liczba ma dzielniki można by użyć:

def check_if_has_dividers(x):
 
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False
Zakładając, że chcesz wyświetlić WSZYSTKIE liczby pierwsze do 10000 możesz to zrobić tak:

# not optimal:
prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
print(prime_numbers)
Zauważ, że komputer przez chwilę musiał to liczyć... Jeśli zechcesz wyświetlić tylko 10 początkowych wartości zrobisz to tak:

print(prime_numbers[:10])
Mimo tego,  że wyświetlamy tylko 10 początkowych liczb pierwszych i tak najpierw musiały być wyliczone wszystkie. A to trwa.... i tu z pomocą przychodzi islice:

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))
Zobacz, że inincjując ten obiekt robimy to aż do 10000000. Mimo tego wyniki dostajemy bardzo szybko. Dlaczego? Bo islice skończy generować kolejne liczby kiedy uda mu się zwrócić owe 10. Sprytne! W formie ćwiczenia przepisz/skopiuj ten kod do siebie i zobacz jak to działa.


"""
import itertools

def get_factors(x):
 
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list
#Przetestuj funkcję wyznaczając dzielniki liczby 20.

#print(get_factors(20))

candidate_list = list(range(1,100))
print(candidate_list)

filtered_list = itertools.filterfalse(lambda x: x != sum(get_factors(x)),candidate_list)

print('*****')
print(filtered_list)

for each in filtered_list:
    #print(each)
    print('Perfect number - {} has the followwing divisors that sum up to this number: {}'.format(each,get_factors(each)))
    