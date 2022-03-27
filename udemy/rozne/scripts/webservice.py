from utilities import *

#app_id = input('Enter application id: ')
#sdate = input('Enter start date: ')
#edate = input('Enter end date: ')
app_id = '3354'
sdate = '2020-10-01'
edate = '2020-10-02'


url = request_url(app_id,sdate,edate)
#print(url)
#send_request(url)

xml_content = send_request(url)

print(xml_content)
