import time 
import functools

def wrapper_time(a_function):
    def func_with_wrapper(*args,**kwargs):
        time_start = time.time()
        result = a_function(*args,**kwargs)
        time_stop = time.time()
        execution_time = time_stop - time_start
        #print('Funkcja ()  wykonana w czasie ()}'.format(a_function.__name__,execution_time))
        print(">>>>>Function {} executed in {}".format(a_function.__name__, time_stop - time_start))
        return result
    return func_with_wrapper

@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

print(get_sequence(10))