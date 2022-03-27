from datetime import datetime

start = datetime(2019, 1, 1, 0, 0, 0)  
end  = datetime.now()

def CreateFunction():
    source = '''
def f(start, end):
    results = end - start
    results_in_s = results.total_seconds()
    return results_in_s
'''
    exec(source, globals())
    print(source)
    return f


time_span_m = CreateFunction()
time_span_h = CreateFunction('f')
time_span_d = CreateFunction('d')


print(time_span_m(start,end))


#print(time_span_m(start, end))
#print(time_span_h(start, end))
#print(time_span_d(start, end))

