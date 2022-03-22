""""
W tym zadaniu nadal pracujemy nad klasą "Ciastko"

Dodaj do klasy Cake ukryty atrybut gluten_free. (To jedna z ważniejszych informacji o wypiekach, dlatego staramy się, żeby ten atrybut można było ustawić tylko raz podczas tworzenia obiektu, dzięki czemu później podczas pracy programu nie zmienimy przypadkowo wartości w tym polu)

Zmień funkcję __init__ oraz show_info tak, aby obsługiwały nowy atrybut klasy

Tworząc nowe obiekty wypieków przekazuj wartość True lub False wskazującą na to czy wypiek jest bezglutenowy (o ile wiem jajka nie zawierają glutenu, więc bezy są bezglutenowe)

Przetestuj działanie programu

Spróbuj w kodzie programu (np. po wyświetleniu oferty ciastkarni) zmienić atrybut __gluten_free

Czy po uruchomieniu masz błąd? Dlaczego? Korzystając z polecenia dir(cake03) zobacz jakie atrybuty ma ten obiekt

Zmień wartość atrybutu korzystając ze specjalnie i automatycznie utworzonego atrybutu o specyficznej budowie tak, jak to było zrobione w materiale video

Wyświetl ponownie informacje o cake03 (beza) - czy teraz stała się wyrobem glutenowym?"""

class Cake:
    known_types = []
    bakery_offer = []

    def __init__(self,name,kind,taste,additives,filling,gluten_free):
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.name = name
        #self.kind = kind
        self.taste = taste
        self.additivies = additives
        self.filling = filling
        Cake.bakery_offer.append(self)
        self.__gluten_free = gluten_free

    def showInfo(self):
        print("{}".format(self.name.upper()))
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if len(self.additivies) > 0:
            print("Additives:")
            for a in self.additivies:
                print('\t{}'.format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        print("Is gluten free: {}".format(self.__gluten_free))
        print('-'*20)
            
    def setFilling(self,filling):
        self.filling = filling

    def addAdditivies(self,additivies):
        self.additivies.extend(additivies)
        
     
Cake_01 = Cake('Vanilla Cake','cake','vanilla',['chocolate','smietana'],'cream',False)
Cake_02 = Cake('Chocolade Muffin','muffin','chocolate',['chocolate'],'',False)
Cake_03 = Cake('Super Sweet Maringue','meringue','very sweet',[],'',True)

Cake_02.setFilling('Cream filling')
Cake_03.addAdditivies(['cocoa,chcocolate sprinkles'])

Cake.known_types.append('cake')
Cake.known_types.append('muffin')
Cake.known_types.append('merinque')
Cake.known_types.append('biscuit')
Cake.known_types.append('eclair')
Cake.known_types.append('christmas')
Cake.known_types.append('pretzel')
Cake.known_types.append('other')

Cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',False)
Cake_05 = Cake('Cocoa waffle','waffle2','cocoa',[],'cocoa',False)

Cake_03._Cake__gluten_free = False

print("This os our offer: ")
for C in Cake.bakery_offer:
    print(C.showInfo())
    print('Is instance of class Cake: {}'.format(isinstance(C,Cake)))


print(dir(Cake_03))
#print('Is cake01 of type Cake? (isinstance)', isinstance(Cake_01, Cake))
#print('Is cake01 of type Cake? (type)', type(Cake_01) is Cake)
#print('vars cake01', vars(Cake_01))
#print('vars Cake?', vars(Cake))
#print('dir cake01', dir(Cake_01))
#print('dir Cake?', dir(Cake))