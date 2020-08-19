import mysql.connector
import datetime


def sql_queries_static(query,param1=None,param2=None):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='nio_python'
    )
    mycursor = mydb.cursor()
    if param1==None and param2==None:
        mycursor.execute(query)
    else:
        mycursor.execute(query%(param1,param2))
    mydb.commit()
    mydb.close()
    mycursor.close()

def sql_queries_dynamic(query,param1=None,param2=None):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='nio_python'
    )
    mycursor = mydb.cursor()
    if param1==None and param2==None:
        mycursor.execute(query)
    else:
        mycursor.execute(query%(param1,param2))
    req_data = mycursor.fetchall()
    mydb.close()
    mycursor.close()
    return req_data

def upload_mission(file):
    val=file.getvalue()
    upl_time=datetime.datetime.now()
    query="INSERT INTO mission_upload(input,time_stamp,status) VALUES ('%s','%s','UPLOADED')"
    sql_queries_static(query,val,upl_time)


def abort_mission():
    query="DELETE FROM mission_upload ORDER BY id DESC LIMIT 1"
    sql_queries_static(query)


def run_mission():
    query="UPDATE nio_python.mission_upload SET status='RUNNING' WHERE id=( SELECT id FROM mission_upload ORDER BY id DESC LIMIT 1 )"
    sql_queries_static(query)

def table_empty():
    query="SELECT * FROM mission_upload"
    data = sql_queries_dynamic(query)
    if len(data)==0:
        return True
    else:
        return False

def current_uploads():
    query="SELECT * FROM mission_upload"
    return sql_queries_dynamic(query)