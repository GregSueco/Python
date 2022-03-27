from logging import root
import xml.etree.ElementTree as ET  # for parsing XML
import requests
#import numpy as np  # for using pandas
import pandas as pd  # for using dataframes
import xmltodict


webservice_address = 'https://prtg.energykey.dk/api/historicdata.xml?id=3354&avg=300&sdate=2020-10-01&edate=2020-10-02&username=ski&passhash=1406849539'
username = 'ski'
password = '1406849539'

#def request_url(appid,sdate,edate,username = username,password = password):
#    request_url = webservice_address+appid+'&avg=300&sdate='+sdate+'&edate='+edate+'&username='+username+'&passhash='+password
#    return request_url

def request_url(appid,sdate,edate):
    url = webservice_address+appid+'&avg=300&sdate='+sdate+'&edate='+edate+'&username='+username+'&passhash='+password+"'"
    return url   
    
def send_request(request_url):
  response = requests.get(request_url)
  response_xml = xmltodict.parse(response.content)
  print (response_xml['item'])
  #response_xml = ET.fromstring(response.content)
  #print()
  #return  ET.ElementTree(response_xml)
  
#send_request(request_url


def fetch_xml(url):
    """
    Fetch a url and parse the document's XML.

    :param url: the URL that the XML is located at.
    :return: the root element of the XML.
    :raises:
        :requests.exceptions.RequestException: Requests could not open the URL.
        :xml.etree.ElementTree.ParseError: xml.etree.ElementTree failed to parse the XML document.
    """
    xml_content = ET.fromstring(requests.get(url).content)
    return xml_content




#def parse_xml(xml):
 # root = xml.getroot()
 # item_list = []
 # for item in root:
 #   print (item.tag,item.attrib,item.text)
 #   for child in item:
 #     print(child.tag,child.attrib,child.text)
 #     item_list.append(child.text)

 #root = xml.getroot()
 #counter = 0
 #for element in root[1]:
 #  print(element.tag,element.attrib,root[1].text)

  #print(myroot[1].tag)
  #api_results = ET.parse(xml).findall("item/")
  #rint(api_results)
  #subelement = xml.findall("item/")
  #print(subelement)
  #for child in subelement:
  #   print(child.tag, child.attrib, child.text)
     



#tree = ET.parse('prtg.xml')
#root = tree.getroot()
#print(root)


#response = requests.get("http://parabank.parasoft.com/parabank/services/bank/accounts/12345")
#    response_body_as_xml = et.fromstring(response.content)


#def parse_xml(result):
#  xml_file = ET.fromstring(result.content)
#channelid = []
#channel = []
#channel_value = []
#channelid_raw = []
#channel_raw = []
#channel_value_raw = [] 
#for x in xml_file.findall('item'):
#   datetime = x.find('datetime').text
#   datetime_raw = x.find('datetime_raw').text
#   for y in x.iter('value'):
#       channelid.append(y.attrib['channelid'])
#       channel.append(y.attrib['channel'])
#       channel_value.append(y.text)  
#   for y in x.iter('value_raw'):
#       channelid_raw.append(y.attrib['channelid'])
#       channel_raw.append(y.attrib['channel'])
#       channel_value_raw.append(y.text)  
#   value_raw_channelid = x.find('value_raw').attrib['channelid']
#   value_raw_channel_2 = x.find('value_raw').attrib['channel']
#   value_raw_channelid_2 = x.find('value_raw').attrib['channelid']
#   coverage = x.find('coverage').text
#   coverage_raw = x.find('coverage_raw').text
#   value = x.find('value')
#   value_channel = x.find('value').attrib['channel']
#   value_raw =x.find('valueS_raw')
#   coverage = x.find('coverage')
#   coverage_raw = x.find('coverage_raw')
#   print(datetime,datetime_raw,channelid,channel,channel_value,channelid_raw,channel_raw,channel_value_raw)
#channelid = []
#channel = []
#channel_value = []
#channelid_raw = []
#channel_raw = []
#channel_value_raw = []






#r = requests.get('https://prtg.energykey.dk/api/historicdata.xml?id=3353&avg=300&sdate=2021-05-01-00-00-00&edate=2021-05-01-23-59-99&&')


#print(r)

#data =  open(r"C:\Users\Z6GSZ\Documents\GitHub\Python\Python\scripts\prtg.xml") 
#myroot = ET.fromstring(data)
#print(myroot)
#print(myroot.tag)

#mytree = ET.parse(r"C:\Users\Z6GSZ\Documents\GitHub\Python\Python\scripts\prtg.xml") 
#myroot = mytree.getroot()
#print(myroot)

#for x in myroot[1]:
#    print(x.tag, x.attrib)

#channel_id =  mytree.findall('.//value_raw')
#print (channel_id.text)







#myroot = ET.fromstring(data)
#print(myroot)
#print(myroot.tag)

#myroot = ET.fromstring(r.text)  # parse XML
#print(root)
### create a list to store the descriptions
##desc_list = []
##
### loop through each "description" element in the XML
##for description in root.iter('item'):
##        # add the description text to the list of descriptions   
##        desc_list.append(description.text)  
##
### convert the list of descriptions to a dataframe
##properties_df = pd.DataFrame({"item":desc_list})
##
#tree = ET.parse(r)
#myroot = mytree.getroot()
#print(myroot)
#for x in root.findall('item')
#  print('item')
#yroot = myroot[0]
#for x in myroot[1]:
#    print(x.tag, x.attrib)


#channelid = []
#channel = []
#channel_value = []
#channelid_raw = []
#channel_raw = []
#channel_value_raw = []

#for x in myroot.findall('item'):
#
#    datetime = x.find('datetime').text
#    datetime_raw = x.find('datetime_raw').text
#    #value_channelid = x.find('value').attrib['channelid']
#    #value_channel = x.find('value').attrib['channel']
#    #value = x.find('value').text
#    for y in x.iter('value'):
#        channelid.append(y.attrib['channelid'])
#        #print(y.attrib['channelid'])
#        channel.append(y.attrib['channel'])
#        channel_value.append(y.text)  
#    for y in x.iter('value_raw'):
#        channelid_raw.append(y.attrib['channelid'])
#        #print(y.attrib['channelid'])
#        channel_raw.append(y.attrib['channel'])
#        channel_value_raw.append(y.text)  
#
#
#    value_raw_channelid = x.find('value_raw').attrib['channelid']
#    value_raw_channel_2 = x.find('value_raw').attrib['channel']
#    value_raw_channelid_2 = x.find('value_raw').attrib['channelid']
#    coverage = x.find('coverage').text
#    coverage_raw = x.find('coverage_raw').text
#    value = x.find('value')
#    value_channel = x.find('value').attrib['channel']
#    value_raw =x.find('valueS_raw')
#    coverage = x.find('coverage')
#    coverage_raw = x.find('coverage_raw')
#  
#    print(datetime,datetime_raw,channelid,channel,channel_value,channelid_raw,channel_raw,channel_value_raw)
#    channelid = []
#    channel = []
#    channel_value = []
#    channelid_raw = []
#    channel_raw = []
#    channel_value_raw = []
  #  channelid,channel,channel_value,value_raw_channelid,value_raw_channel_2,value_raw_channelid_2,coverage,coverage_raw)
  