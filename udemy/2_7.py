days = ['mon','tue','wed','thu','fri','sat','sun']
workdays = days
print(id(days),id(workdays))
workdays2 = workdays.copy()
print(days,workdays,workdays2)
print(id(days),id(workdays),id(workdays2))
workdays2.remove('fri')
workdays.remove('thu')
print(days,workdays,workdays2)
print(id(days),id(workdays),id(workdays2),id(workdays.append('weekend')))