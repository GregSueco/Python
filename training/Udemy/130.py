import datetime as dt
from symtable import Symbol
 
class Trip:

    #list_of_errors=[]

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")
 
    @classmethod
    def publish_offer(cls,trips):
        print("Starting to test trips: ")
        list_of_errors = []
        for t in trips:
            print("Testing trip: {}".format(t.symbol))
            try:
                t.check_data()
            except ValueError as e:
                list_of_errors.append("{}: {}".format(t.symbol,str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(t.symbol,str(e)))
        print("Done testing trips.")
        if len(list_of_errors):
            raise Exception("The list of trips has errors:\n {}".format(list_of_errors))
        else:
            print("the offer will be published...")



trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 13), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]

Trip.publish_offer(trips)

"""
Twoim zadaniem jest napisanie metody klasy o nazwie publish_offer, która:

jako argument przyjmie listę wycieczek

zadeklaruje lokalną listę list_of_errors, w której będą zapamiętane wyniki testu dla wycieczek zawierających błędy

dla każdej wycieczki z listy list_of_errors wywoła metodę check_data

jeżeli błąd to ValueError, to do list_of_errors doda napis  w postaci "<symbol_wycieczki>: <treść błędu>"

jeżeli błąd to Exception, to do  list_of_errors doda napis  w postaci "<symbol_wycieczki>: <treść błędu>"

jeżeli po sprawdzeniu wszystkich wycieczek w list_of_errors są jakieś błędy, to zgłosi exception o treści "The list of trips has errors: <lista_błędów>"

w przeciwnym razie wyświetli komunikat "the offer will be published..." (normalnie w tym miejscu odbywałoby się publikowanie wycieczek, ale my ten punkt pomijamy)

W kodzie poza klasą dodaj wywołanie metody publish_offer w taki sposób, że:

w bloku try:

najpierw zostanie wyświetlony komunikat o rozpoczęciu sprawdzania wycieczek

potem będzie wywołana metoda publish_offer

na zakończenie zostanie wyświetlony napis "done"

w bloku except:

jeśli doszło do błedu, wyświetl "przerażający" komunikat o błędzie i szczegóły tego błędu



W tym ćwiczeniu zobaczyłeś, jak można skumulować kilka mniejszych błędów w jeden większy. Użytkownik od razu mógł zobaczyć wszystkie wadliwe dane, dokonać korekt i ponownie uruchomić swój program.
"""