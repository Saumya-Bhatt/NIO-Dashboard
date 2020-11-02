import mysql.connector
import datetime

from frame import sql_queries_dynamic, sql_queries_static


def upload_mission(file):
    val=file.getvalue()
    upl_time=datetime.datetime.now()
    query="INSERT INTO mission_upload(input,time_stamp,status) VALUES ('%s','%s','UPLOADED')"
    sql_queries_static(query,val,upl_time)

def abort_mission():
    query="DELETE FROM mission_upload ORDER BY id DESC LIMIT 1"
    sql_queries_static(query)
    return None

def run_mission():
    query="UPDATE nio_python.mission_upload SET status='RUNNING' WHERE id=( SELECT id FROM mission_upload ORDER BY id DESC LIMIT 1 )"
    sql_queries_static(query)
    return None

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