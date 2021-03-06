import datetime as dt
 
class TripException(Exception):
    def __init__(self, text, description):
        super().__init__(text)
        self.description = description

    def __str__(self):
        return "{}, info: {}".format(super().__str__(),self.description)

class TripNameException(TripException):
    def __init__(self,text):
        super().__init__(text,'Name of the trip is missing. You need to name the trip somehow...')
        
class TripDateException(TripException):
    def __init__(self,text):
        super().__init__(text,'The dates are incorrect. The starting date should be earlier than the ending date...')


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Title is empty!")
        if self.start > self.end:
            raise TripDateException("Start date is later than end date!")
 
    @classmethod
    def publish_offer(cls, trips):
 
        list_of_errors = []
 
        for trip in trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except TripDateException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
        
        if len(list_of_errors) > 0:
            raise TripException("The list of trips has errors",list_of_errors)
        else:
            print('the offer will be published...')
        
 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]
 
try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')


        
"""
Zmienimy nieco obs??ug?? b????d??w:

Zdefiniuj klas?? TripException, kt??ra rozszerzy ilo???? informacji przedstawianych podczas b????du. Klasa ta b??dzie przechowywa?? po prostu 
dodatkowy atrybut description:

klasa ma dziedziczy?? z Exception

metoda __init__ ma przyj???? argumenty text i description

text zostanie przekazany podczas wywo??ywania metody __init__ klasy rodzicielskiej

description zostanie zapisane jako lokalny atrybut

metoda __str__ ma zwraca?? to co zwr??ci??aby klasa rodzicielska, a dodatkowo informacje zapisane w atrybucie description

Zdefiniuj klas?? TripNameException dziedzicz??c?? z TripException. Ten rodzaj b????du b??dzie zg??aszany zawsze wtedy, gdy pojawi si?? problem z 
nazw?? wycieczki. Wszystkie te b????dy b??d?? mia??y wsp??lne description, dlatego zdefiniujemy je na sta??e w __init__:

metoda __init__ ma przyj???? tylko argument text

argument text zostanie przekazany jako pierwszy argument do __init__ klasy rodzicielskiej

drugi argument mo??e by?? bardziej rozbudowanym opisem usterki, np. 'Name of the trip is missing. You need to name the trip somehow...'

Zdefiniuj klas?? TripDateException dziedzicz??c?? z TripException. Ten rodzaj b????du b??dzie zg??aszany zawsze wtedy, gdy pojawi si?? problem z datami wycieczki. Wszystkie te b????dy b??d?? mia??y wsp??lne description, dlatego zdefiniujemy je na sta??e w __init__:

metoda __init__ ma przyj???? tylko argument text

argument text zostanie przekazany jako pierwszy argument do __init__ klasy rodzicielskiej

drugi argument mo??e by?? bardziej rozbudowanym opisem usterki, np. 'The dates are incorrect. The starting date should be earlier than the ending date...'

Zmie?? wyj??tki zg??aszane w metodzie check_data

w pierwszym przypadku zg??o?? TripNameException i skr???? tekst przekazywany jako argument

w drugim przypadku zg??o?? TripDateException i te?? skr???? tekst przekazywany jako argument

W metodzie publish_offer:

obs??u?? nowe rodzaje b????d??w: TripNameException  i TripNameException

z kolei zg??aszaj??c b????d wykorzystaj TripException przekazuj??c jako argumenty

tekst - "The list of trips has errors"

i jako drugi argument list_of_errors

Przetestuj dzia??anie programu
"""
