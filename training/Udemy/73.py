"""
Oto przykład niezbyt dobrze napisanej funkcji wyliczającej wartość w ciągu Finobacciego:

def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result
Funkcja zamiast wyliczać wartości od najmniejszych do największych i korzystać z poprzednich wyników do wyznaczenia kolejnych wartości, każdorazowo wyznacza poprzednie wartości. Zoptymalizuj funkcję metodą cache, (a jak masz ochotę to również przepisz funkcję do lepszej postaci)

przygotuj funkcję do testu pomiaru czasu

zaimportuj moduł time

w zmiennej start zapisz aktualny czas

napisz pętlę wyliczającą wartość ciągu zaczynając od 1, a kończąc na sensownej na Twoim komputerze wartości, na którą masz cierpliwość doczekać (u mnie to do około 33-37)

każdorazowo wyświetl numer iteracji w pętli i różnicę między czasem bieżącym, a czasem ze zmiennej start

zapamiętaj czas trwania obliczeń

zoptymalizuj funkcję

zaimportuj moduł functools

oznacz funkcję fib dekoratorem lru_cache z maksymalną ilością pamiętanych wyników 100

na końcu skryptu dodaj instrukcję wyświetlającą wynik polecenia cache_info

porównaj wyniki

"""


import time
import functools

##def fib(n):
##    if n <= 2:
##        result = n
##    else:
##        result = fib(n-1) + fib(n-2)
##    
##    return result

@functools.lru_cache(maxsize=100)
def fib_cached(n):
    if n <= 2:
        result = n
    else:
        result = fib_cached(n-1) + fib_cached(n-2)
    
    return result

##stime=time.time()
##for i in range (1,25):
##   ## print('Duration on {} iteration is: {} with a result of: {}'.format(i,time.time()-stime,fib(i)))
##   fib(i)
##print('Total execution time is: {}'.format(time.time()-stime))
    ##print('Duration on {} cached iteration is: {} with a result of: {}'.format(i,time.time()-stime,fib_cached(i)))
    

stime=time.time()
for i in range (1,25):
    ##print('Duration on {} iteration is: {} with a result of: {}'.format(i,time.time()-stime,fib(i)))
    ##print('Duration on {} cached iteration is: {} with a result of: {}'.format(i,time.time()-stime,fib_cached(i)))
   result = fib_cached(i)
print('Total execution time is: {}'.format(time.time()-stime))

print(fib_cached.cache_info())