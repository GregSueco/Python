from ssl import enum_certificates


projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for pos,(pro,lead,date) in enumerate(zip(projects,leaders,dates)):
    print(pos,'-','The leader of:',pro,'started',date,'is',lead)
