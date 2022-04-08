import datetime as dt

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        #if len(self.title) == 0:
        #    raise Exception("Title is empty!")
        assert len(self.title) != 0, 'Title is empty'
        #if self.start > self.end:
        #    raise ValueError("Start date is later than end date!")
        assert self.start <= self.end, 'Start date is later than end date!'
        
 
    @classmethod
    def publish_offer(cls, trips):
 
        list_of_errors = []
 
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
        
        #if len(list_of_errors) > 0:
        #    raise Exception("The list of trips has errors: {}".format(list_of_errors))
        assert len(list_of_errors) == 0, "The list of trips has errors: {}".format(list_of_errors)
        print('the offer will be published...')
        #else:
        #    print('the offer will be published...')
        
        
        
 
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 7, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 7, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 11), dt.date(2023, 6, 12))
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
Zmień testy wykonywane w funkcji check_data tak, aby wykorzystywały assert.

Zamień instrukcję if/else z  metody publish_offer na assert

A teraz się zastanów... czy ZAWSZE należy stosować polecenie assert zamiast if/else? Co stałoby się z Twoim programem jeśli uruchomisz go w środowisku, w którym PYTHONOPTIMIZE jest ustawione na TRUE ? Sprawdź to i udziel odpowiedzi!

"""