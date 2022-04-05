#W programie zdefiniowano następujące klasy i obiekty:

from datetime import date
from datetime import timedelta  
class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)
 
class Promo():
 
    def __init__(self, discount_name, discount, start_date, end_date, minimal_order):
 
        self.discount_name = discount_name
        self.discount = discount
        self.start_date = start_date
        self.end_date =  end_date
        self.minimal_order = minimal_order
 
    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.discount_name, self.discount)
 
 
#cake = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
#cake.show_info()
 
#promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14),0)
#print(promo10.full_name)

class PromoCake(Promo,Cake):

    def __init__(self,name,discount_name,discount,start_date,end_date,minimal_order,kind,taste,additives,filling):
        Promo.__init__(self, discount_name, discount, start_date, end_date, minimal_order)
        Cake.__init__(self, name, kind, taste, additives, filling)


promoCake_01 = PromoCake('Vanilla Cake',"DISCOUNT - no additional conditions",0.15,date.today(), date.today() + timedelta(days=14),0,'cake','vanilla', ['chocolade', 'nuts'], 'cream')
promoCake_01.show_info()
print(promoCake_01.full_name)
print(PromoCake.__mro__)

"""
W celu organizowania promocji na wypieki należy zdefiniować klasę dziedziczącą zarówno z Cake jak i z Promo

Zdefiniuj klasę PromoCake dziedziczącą z Cake i Promo

W metodzie  __init__ przyjmij argumenty cake i promo, a następnie wywołaj __init__ z klas rodzicielskich

Utwórz obiekt promo_cake z klasy PromoCake

Wywołaj dla tego obiektu metodę show_info. Spróbuj przed uruchomieniem odgadnąć wynik

Wyświetl dla tego obiektu właściwość full_name

Wyświetl "Method Resolution Order" dla klasy  PromoCake
"""