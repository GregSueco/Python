"""Zaczynamy od klasy, która jest rozwiązaniem poprzedniego zadania. Ponieważ obecnie skupiamy się bardziej na pobieraniu kolejnych elementów,
 zrezygnujemy z funkcji opóźniającej program oraz skorzystamy ze zdecydowanie krótszych list produktów, promocji i klientów:"""

class Combinations:
 
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.max_item = len(products) * len(promotions) * len(customers)
    #    self.current_product = 0
    #    self.current_promotion = 0
    #    self.current_customer = 0
 
    #def __next__(self):
    #
    #    if self.current_customer >= len(self.customers):
    #        self.current_customer = 0
    #        self.current_promotion += 1
    #
    #    if self.current_promotion >= len(self.promotions):
    #        self.current_promotion = 0
    #        self.current_product += 1
    #
    #    if self.current_product >= len(self.products):
    #        self.current_product =0
    #        raise StopIteration()
    #
    #    item_to_return = "{} - {} -{}".format(self.products[self.current_product],
    #                                          self.promotions[self.current_promotion],
    #                                          self.customers[self.current_customer])
    #
    #    self.current_customer += 1
    #
    #    return  item_to_return
 
    #def __iter__(self):
    #    return  self

    def __getitem__(self, item):
        if item < self.max_item:
            pos_products = item // (len(self.promotions) * len(self.customers))
            item = item % (len(self.promotions)*len(self.customers))
            pos_promotions = item // len(self.customers)
            item = item % len(self.customers)
            pos_customers = item
            return (" {} - {} - {}".format(self.products[pos_products],self.promotions[pos_promotions],self.customers[pos_customers]))
        else:
            raise StopIteration()

 
 
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]
 
combinations = Combinations(products, promotions, customers)
 
#for i in range(0,31):
#    print(i,combinations[i])
comb = iter(combinations)

print(next(comb))
print(next(comb))
print(next(comb))

for c in comb:
    print(c)


"""
Naszym celem jest eliminacja metody __next__ i jej zamiana na __getitem__, co pozwoli na odwoływanie się do i-tego generowanego elementu.
Jednocześnie jednak chcemy nadal móc wykorzystywać obiekt w pętli for, a wiesz, że domyślnie do tego jest potrzebna metoda __next__. 
Obejdziesz ten problem wykorzystując sztuczkę z funkcją iter()

Ale po kolei:

Usuń definicję metody __next__

Zmienne current_product, current_promotion i current_customer inicjowane w __init__ też nie będą już potrzebne

Dodaj do klasy definicję metody __getitem__

Jeżeli item jest większe od ilości elementów, które może generować obiekt klasy, to zgłoś wyjątek StopIteration

wskazówka - maksymalna ilość generowanych kombinacji to ilość produktów razy ilość promocji razy ilość klientów

W przeciwnym razie musisz wyliczyć jaką kombinację należy zwrócić i w tym celu

w zmiennej pos_products zapisz wynik dzielenia całkowitego wartości item przez ilość promocji razy ilość klientów

zaktualizuj zmienną item zapisując w niej wynik dzielenia modulo wartości item przez ilość promocji razy ilość klientów

w zmiennej pos_promotions zapisz wynik dzielenia całkowitego wartości item przez ilość klientów

zaktualizuj zmienną item zapisując w niej wynik dzielenia modulo wartości item przez ilość klientów

w zmiennej pos_customers zapisz wartość item

teraz zmienne pos_products, pos_promotions i pos_customers wskazują na poprawny elementy list products, promotions i customers, które należy
zwrócić

Zwróć napis składający się z elementu listy products znajdującego  się na pozycji pos_products oraz z elementu listy promotions znajdującego 
się na pozycji pos_promotions oraz z elementu listy customers znajdującego się na pozycji pos_customers

W głównej części skryptu napisz pętlę for, która:

zmiennej sterującej i przypisze wartości od 1  do 30 (tyle mamy obecnie możliwych kombinacji - 3 produkty * 2 promocje * 5 klientów)

w każdym wykonaniu pętli wyświetli  i-ty element z obiektu combinations. Dzięki temu, że klasa Combinations ma teraz metodę 
__getitem__ zobaczysz wszystkie możliwe kombinacje produktów, promocji i klientów

Po zakończonych testach zakomentuj tę pętlę

Sprawdź czy z obiektu combinations można pobierać kolejne elementy korzystając z funkcji next (nie powinno się dać)

Zrób coś żeby się dało! :)

Wskazówka: Pamiętaj o funkcji iter()

Przetestuj pobieranie kolejnych elementów metodą next()

Napisz pętlę for, która przejdzie przez wszystkie możliwe kombinacje zwracane przez obiekt combinations, ale nie korzystaj ze zmiennej 
sterującej!
"""