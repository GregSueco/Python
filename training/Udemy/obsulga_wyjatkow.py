try:
    tekst = raw_input('Wpisz coś ---> ')
except EOFError:
    print 'Dlaczego użyłeś znaku końca pliku?'
except KeyboardInterrupt:
    print 'Przerwałeś operację.'
else:
    print 'Wpisałeś %s' % tekst
#Rezultat:

#$ python try_except.py
#Wpisz coś ---> Dlaczego użyłeś znaku końca pliku?
#$ python try_except.py
#Wpisz coś ---> ^CPrzerwałeś operację.
#$ python try_except.py
#Wpisz coś ---> tekst nie wywołujący błędów
#Wpisałeś tekst nie wywołujący błędów