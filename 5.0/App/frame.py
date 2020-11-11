import streamlit as st
import sqlite3


class SessionManager():
    live = False

    def __init__(self, database):
        self.database = database
    
    def get_last_row(self):
        query = 'SELECT * FROM sessions ORDER BY id DESC LIMIT 1'
        return sql_queries(database=self.database, query=query)

    def session_status(self):
        self.live = False
        row = self.get_last_row()
        try:
            if row[0][1] == 1 : self.live = True
            return self.live
        except:
            return self.live

    def create_session(self):
        query = 'INSERT INTO sessions VALUES (?,?)'
        sql_queries(database=self.database, query=query, POST=True, arg=(None,1))

    def delete_session(self):
        try:
            row = self.get_last_row()
            query_update = 'UPDATE sessions SET session_status = 0 WHERE id = '+str(row[0][0])
            sql_queries(database=self.database, query=query_update, override=True)
        except:
            pass

    def destroy_all_sessions(self):
        query = 'DELETE FROM sessions'
        sql_queries(database=self.database, query=query, override=True)

    
class InstanceManager():

    def __init__(self, database):
        self.database = database

    def duplicate_row(self,id, auv_id=False):
        if auv_id:
            query = 'SELECT * FROM instance_log WHERE auv_id = ' + str(id)
        else:   
            query = 'SELECT * FROM instance_log WHERE id = ' + str(id)
        try:
            returnedRow = sql_queries(database=self.database, query=query)
            if len(returnedRow) > 0:
                return True
            return False
        except:
            return False

    def generate_instance(self, name, id):
        if self.duplicate_row(id, auv_id=True):
            return False
        else:
            query = 'INSERT INTO instance_log VALUES (?,?,?)'
            arg = [None,name,id]
            sql_queries(database=self.database, query=query, POST=True, arg=arg)
            return True

    def delete_instance(self,id):
        if self.duplicate_row(id):
            query = 'DELETE FROM instance_log WHERE id=?'
            arg = (id,)
            sql_queries(database=self.database, query=query, POST=True, arg=arg)
            return True
        return False

    def get_all_instances(self):
        query = "SELECT * from instance_log"
        records = sql_queries(database=self.database, query=query)
        return records

    def destroy_all_instances(self):
        query = 'DELETE FROM instance_log'
        sql_queries(database=self.database, query=query, override=True)
        


def newline(x, sidebar=False, element=None):
    if element != None:
        for _ in range(x):
            element.markdown('\n')
    if not sidebar:
        for _ in range(x):
            st.markdown('\n')
    else:
        for _ in range(x):
            st.sidebar.markdown('\n')

def sql_queries(database,query,POST=False,arg=None,override=False):
    conn = sqlite3.connect(database)
    curr = conn.cursor()

    if override:
        curr.execute(query)
        conn.commit()
        conn.close()
        return None

    if POST == False:
        curr.execute(query)
        records = curr.fetchall()
        curr.close()
        conn.close()
        return records
    else:
        curr.execute(query,arg)
        conn.commit()
        conn.close()
        return None