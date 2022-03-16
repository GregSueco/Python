import smtplib

mailFrom = "My python tutorial"
mailTo = 'grzesiek.szwed@gmail.com'
mailSubject = 'My Python tutorial test subject'
mailBody = '''
Hi, 
This is a test email.
Have a nice day
'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom,mailSubject,mailBody)

user = 'grzesiek.szwed@gmail.com'
password = 'lhse vrwz xsla cwdi'

#try:
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login(user,password)
server.sendmail(user,mailTo,message)
server.close()
print('Email sent successfully')
#except:
#    print('Something went wrong')