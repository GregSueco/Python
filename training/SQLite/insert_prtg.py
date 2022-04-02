from tkinter import N
import download_xml
import config

file = download_xml.get_file(3354,'2021-11-01','2021-11-02')
list = download_xml.parse_file(file)
df_prtg = download_xml.pd.DataFrame(list)
df_prtg.drop_duplicates(keep='first', inplace=True)
df_prtg.reset_index(drop=True, inplace=True)
print(df_prtg)
#print(df_prtg)
# creating column list for insertion
#cols = "`,`".join([str(i) for i in df_prtg.columns.tolist()])
#print(cols)


# Insert DataFrame recrds one by one.
#for i,row in data.iterrows():
#    sql = "INSERT INTO `book_details` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
#    cursor.execute(sql, tuple(row))
#
#    # the connection is not autocommitted by default, so we must commit to save our changes
#    connection.commit()

 # create a database connection
conn = config.create_connection(config.database)
c = conn.cursor()
if conn is not None:
        # create projects table
        for i in range(len(df_prtg)) :
            sql = """
            INSERT INTO [prtg.test] 
            (datetime
            ,datetime_raw
            ,value_Loading_time
            ,value
            ,[value_raw_Loading_time]
            ,[value_raw]
            ,[Value_Downtime]
            ,[value_raw_Downtime]
            ,coverage
            ,coverage_raw)
            values ('{}','{}','{}','{}',{},{},'{}',{},'{}','{}');
            """.format(df_prtg.loc[i, "datetime"],df_prtg.loc[i, "datetime_raw"],df_prtg.loc[i, "value_Loading_time"],df_prtg.loc[i, "value"],df_prtg.loc[i, "value_raw_Loading_time"],df_prtg.loc[i, "value_raw"],df_prtg.loc[i, "value_Downtime"],df_prtg.loc[i, "value_raw_Downtime"],df_prtg.loc[i, "coverage"],df_prtg.loc[i, "coverage_raw"])
            if c is not None:
                c.execute(sql)
                print('sql executed')
            conn.commit()
else:
    print("Error! cannot create the database connection.")




