import mysql.connector

def sql_queries(query):
    conn = mysql.connector.connect(
    user='root', 
    password='', 
    host='127.0.0.1', 
    database='nio_python')

    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone();
    conn.close()
    return result


def get_home_pos():
    query = '''SELECT * from home_position ORDER BY id DESC LIMIT 1'''
    return sql_queries(query)

def get_boat_pos():
    query = '''SELECT * from boat_position ORDER BY id DESC LIMIT 1'''
    return sql_queries(query)

def get_cbot_pos():
    query = '''SELECT * from cbot_position ORDER BY id DESC LIMIT 1'''
    return sql_queries(query)