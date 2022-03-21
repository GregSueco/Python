"""
Pracujemy z wynikiem LAB z poprzedniej lekcji.

Dodaj do klasy Cake atrybut na poziomie klasy. Nazwij go known_types. Będą w nim przechowywane produkowane w naszej cukierni słodkości. Przypisz do zmiennej listę np. w następującej postaci:

['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

Zmień __init__ tak, że jeżeli jako parametr kind zostanie przekazana wartość znajdująca się na liście known_kinds, to zostanie zaakceptowana, ale jeśli ktoś przekaże wartość spoza tej listy, to do nowo tworzonego obiektu do atrybutu kind zostanie wpisany napis other.

Przetestuj działanie nowej funkcji __init__ tworząc obiekt "wafel kakaowy":

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')



Dodaj do klasy Cake nowy atrybut bakery_offer, który na początku będzie pustą listą.

Zmień __init__ tak, aby po utworzeniu nowego obiektu typu Cake, został on automatycznie dodany do listy bakery_offer

Usuń ze skryptu niepotrzebne już instrukcje tworzące listę bakery_offer i dodające obiekty tej klasy do tej listy.

Zmień pętlę wyświetlającą informację o ofercie cukierni tak, aby korzystała z atrybutu klasy



Sprawdź czy obiekty cake01 i inne są instancjami klasy Cake korzystając z funkcji isinstance i type

Wyświetl informacje o instancji cake01 i o klasie Cake korzystając z funkcji vars i dir
"""
class Cake:
    known_types = []
    bakery_offer = []

    def __init__(self,name,kind,taste,additives,filling):
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
        print('-'*20)
            
    def setFilling(self,filling):
        self.filling = filling

    def addAdditivies(self,additivies):
        self.additivies.extend(additivies)
        
     
Cake_01 = Cake('Vanilla Cake','cake','vanilla','chocolate','cream')
Cake_02 = Cake('Chocolade Muffin','muffin','chocolate',['chocolate'],'')
Cake_03 = Cake('Super Sweet Maringue','meringue','very sweet',[],'')

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

Cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')
Cake_05 = Cake('Cocoa waffle','waffle2','cocoa',[],'cocoa')

print("This os our offer: ")
for C in Cake.bakery_offer:
    print(C.showInfo())
    print('Is instance of class Cake: {}'.format(isinstance(C,Cake)))


print('Is cake01 of type Cake? (isinstance)', isinstance(Cake_01, Cake))
print('Is cake01 of type Cake? (type)', type(Cake_01) is Cake)
print('vars cake01', vars(Cake_01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(Cake_01))
print('dir Cake?', dir(Cake))