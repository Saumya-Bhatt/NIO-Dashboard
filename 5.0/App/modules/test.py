
import mysql.connector


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

query_ = 'SELECT ID FROM auvinstances ORDER BY ID DESC LIMIT 1'
id = sql_query(address='127.0.0.1', database='nio_server', query=query_, returnVal=True)
print(id[0][0])
