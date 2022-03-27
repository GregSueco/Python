""""
W tym LAB pracujemy z klasą z poprzedniej lekcji (jeśli nie masz rozwiązania skopiuj sobie moją propozycję rozwiązania z poprzedniej lekcji)

Do klasy należy dodać atrybut ukryty __text. Odpowiada on za napis umieszczony na torcie.

W funkcji __init__ przyjmij nowy argument text

Zapisz go w zmiennej __text przeprowadzając kontrolę: napis można zapisać w instancji tylko jeżeli kind jest 'cake' lub text jest napisem pustym. Jeśli te warunki nie są spełnione wyświetl diagnostyczny komunikat (print dla Ciebie, żeby było wiadomo co się dzieje)

Dodaj ukrytą funkcję __get_text, która będzie zwracać wartość zapisaną w __text

Dodaj ukrytą funkcje __set_text, która przyjmie dodatkowy argument new_text i zaktualizuje atrybut __text tylko dla wyrobów z kind 'cake'

Zdefiniuj właściwość Text korzystającą z powyższych funkcji.

Tworząc obiekty klasy Cake przekaż dodatkowy argument text - umieść napisy puste lub inne typowo  "tortowe", część poprawnych (czyli napis na torcie) i część niepoprawnych (np. napis na waflu)

Wyświetl wszystkie informacje o wszystkich wypiekach

Spróbuj wstawić do właściwości Text napis na torcie i na innym wypieku nietortowym - prześledź poprawność tych operacji ponownie wyświetlając ofertę cukierni"""

class Cake:
    known_types = []
    bakery_offer = []

    def __init__(self,name,kind,taste,additives,filling,gluten_free,text):
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
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('I cannot insert this text.')

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

    def __get_text(self):
        return self.__text

    def __set_text(self,new_text):
        if self.kind == 'cake':
            self.__text = new_text
    
    Text = property(__get_text,__set_text,None)
        
     
Cake_01 = Cake('Vanilla Cake','cake','vanilla',['chocolate','smietana'],'cream',False,'tekscik na torcie')
Cake_02 = Cake('Chocolade Muffin','muffin','chocolate',['chocolate'],'',False,'tekscik na torcie')
Cake_03 = Cake('Super Sweet Maringue','meringue','very sweet',[],'',True,'tekscik na torcie')

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

Cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',False,'tekscik na torcie')
Cake_05 = Cake('Cocoa waffle','waffle2','cocoa',[],'cocoa',False,'tekscik na torcie')

Cake_03._Cake__gluten_free = False

print("This os our offer: ")
for C in Cake.bakery_offer:
    print(C.showInfo())
    print('Is instance of class Cake: {}'.format(isinstance(C,Cake)))
    print(C.Text)

#print(dir(Cake_03))
#print('Is cake01 of type Cake? (isinstance)', isinstance(Cake_01, Cake))
#print('Is cake01 of type Cake? (type)', type(Cake_01) is Cake)
#print('vars cake01', vars(Cake_01))
#print('vars Cake?', vars(Cake))
#print('dir cake01', dir(Cake_01))
#print('dir Cake?', dir(Cake))