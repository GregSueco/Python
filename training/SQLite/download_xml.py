"""Siemka, mam taki program do napisania i w jednym miejscu sie blokuje:
-korzystam z biblioteki Requests do wyslania metody get, Element Tree do parsowania xml i Pandas do przeksztalcenia do postaci tabelarycznej
- w oparciu o podane url wyslij get request
- zwrocony request (plik xml) zapisz w oparciu o sciezke filename (funkcja get_file)
- zparsuj plik xml do postaci tabelarycznie i zapisz jako .xlsx (funkcja parse_file)
- i tutaj mam problem: wytlumacze na przykladzie kawalka xml:

<histdata totalcount="8760" listend="1">
   <prtg-version>21.4.73.1656</prtg-version>
   <item>
    <datetime>9/1/2021 12:00:00 AM - 1:00:00 AM</datetime>
    <datetime_raw>44439.9583333333</datetime_raw>
    <value channel="Loading time" channelid="0">1,136 msec</value>
    <value_raw channel="Loading time" channelid="0">1135.8333</value_raw>
    <value channel="Downtime" channelid="-4">0 %</value>
    <value_raw channel="Downtime" channelid="-4">0.0000</value_raw>
    <coverage>100 %</coverage>
    <coverage_raw>0000010000</coverage_raw>
   </item>
   <item>

To z czym sie potrafie sobie poradzic to ze element value i value_raw wystepuje 2 razy w otrebie tego samego itemu np.:
    <value channel="Loading time" channelid="0">1,136 msec</value> a potem
    <value channel="Downtime" channelid="-4">0 %</value>

Dwie instancje elementu Value w otrebie tego samego itemu, rozniace sie atrybutem channel i channelid (jeden ma 'Loading time' i 0 a drugi 'Downtime' i -4)
To co probowalem to wyodrebcis atrybuty i dodac jako czesc klucza(zapisuje dane w postaci slownika - czyli klucz skladal by sie z nazwy elementy i jego atrybutow)
stowrzylem cos takiego: key = i.tag + i.attribute ale dostaje wowczas blad:
can only concatenate str (not "dict") to str
"""


import requests
import xml.etree.ElementTree as ET
import pandas as pd


def get_file(app_id,s_date,e_date):
    url = 'https://prtg.energykey.dk/api/historicdata.xml?id={}&avg=300&sdate={}&edate={}&username=ski&passhash=1406849539'.format(app_id,s_date,e_date)
    #print(url) 
    try:    
        prtg = requests.get(url)
    except:
        print('Sorry there was no valid response.')
    else:
        data = prtg.content
        filename = 'C:\prtg\PRTG_{}_{}_{}.xml'.format(app_id,s_date,e_date)
        with open(filename, 'wb') as f:
            f.write(data)
    finally:
        print('Xml file in location: {} was returned in response request'.format(filename))
        return filename
#get_file(3354,'2021-10-01','2021-10-02')
#dest_file = file[:-3]+'xlsx'
#print(dest_file)

def parse_file(file):
    Tree = ET.parse(file)
    Root = Tree.getroot()
    A = [] # Assign empty list
    for element in Root:
        #elementKey=0
        #print(element)
        B = {} # Assign empty dictionary for key:value
        for i in list(element):
                
                element_attribute = {}
                #attributeKey = 1
                #element_attribute.update({i.tag: i.attrib})
                #key = frozenset(element_attribute.items())
                #print(key)
                #key = i.tag + i.attrib
                #print(elementKey,element.tag,i.tag)
                if i.attrib:
                   key = i.tag + '_' + i.attrib['channel'].replace(' ','_')

                   #print(key)
                   B.update({key: i.text})
                   #print(i.tag,i.attrib)
                   #attributeKey += 1
                #print(,i.attrib)
                B.update({i.tag: i.text}) # Update dictionairy
                #print(B)
                A.append(B) # Append B to list
                #print(A)
    print('List created succesfully')
    return A

def create_flatfile(input_list):
    df = pd.DataFrame(input_list) #Create new dataframe
    df.drop_duplicates(keep='first', inplace=True)
    df.reset_index(drop=True, inplace=True)
    dest_file = file.replace("xml","xlsx")
    #print(dest_file)
    writer = pd.ExcelWriter(dest_file, engine='xlsxwriter')
    df.to_excel(writer,'Sheet1')
    #worksheet = writer.sheets['sheet1']
    #worksheet.set_column('B:Z',30)
    writer.save()
    print('File was succesfully converted to excel tabular format')

   # cols = "`,`".join([str(i) for i in df.columns.tolist()])
   #print(cols)

    #def create_prtg(conn, prtg):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

   # sql = r'''INSERT INTO [prtg.test] (datetime,datetime_raw,value_Loading_time,value,[value_raw_Loading_time],[value_raw],[Value_Downtime],[value_raw_Downtime],coverage,coverage_raw)
   #                    VALUES (?,?,?,?,?,?,?,?,?);                           '''
   # cur = conn.cursor()
    #cur.execute(sql, task)
    #conn.commit()

    #return cur.lastrowid


#file = get_file(3354,'2021-11-01','2021-11-02')
#list = parse_file(file)
#create_flatfile(list)

