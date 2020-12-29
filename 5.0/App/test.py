
import mysql.connector
import pandas as pd

COORDINATES = {
'HOME' : [1,2,'🟢'],
'BOAT' : [3,4,'🔵'],
'C-BOT' : [5,6,'🔴']
}

home = pd.DataFrame(data=[COORDINATES['HOME'][0], COORDINATES['HOME'][1]])
boat = pd.DataFrame(data=[COORDINATES['BOAT'][0], COORDINATES['BOAT'][1]])
cbot = pd.DataFrame(data=[COORDINATES['C-BOT'][0], COORDINATES['C-BOT'][1]])

# print(home)

def sql_query(database,query, address=None,sqlite=False,arg=None,returnVal=False):
    if sqlite:
        connection = sqlite3.connect(database)
    else:
        connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = address,
            database = database
        )
    cursor = connection.cursor()
    if returnVal == False:
        if arg is None:
            cursor.execute(query)
        else:
            cursor.execute(query,arg)
        connection.commit()
        cursor.close()
        connection.close()
        return None
    else:
        if arg is None:
            cursor.execute(query)
            records = cursor.fetchall()
        else:
            records = cursor.execute(query,arg)
        connection.close()
        return records

query_ = "SELECT * FROM auvstatus WHERE Instance_AUVStatus_ID = " + str(27)
id = sql_query(address='127.0.0.1', database='nio_server', query=query_,  returnVal=True)[0]
print(id)
