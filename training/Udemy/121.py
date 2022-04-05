class Cake:
    """   
        self.name = name  - cake name e.g. Beza
        self.kind = kind - typ of cake e.g. Tort
        self.taste = taste - e.g. Waniliowy
        self.additives = additives.copy() - list of ingredients
        self.filling = filling - type of filling e.g. cream
        self.bakery_offer.append(self)
 
    """
    bakery_offer = []
 
    def __init__(self, name, kind, taste, additives, filling):
               
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        """ Display cake information"""
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
        """Display cake full name in upper case - consists of cake name & cake typee"""
       
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

"""
Dodaj dokumentację:

do klasy

do metody __init__

do właściwości full_name

Wyświetl help na temat klasy oraz na temat właściwości full_name
"""

help(Cake)