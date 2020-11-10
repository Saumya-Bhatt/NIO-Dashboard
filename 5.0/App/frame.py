import streamlit as st
import sqlite3


class SessionManager():
    live = False

    def __init__(self, database):
        self.database = database
    
    def getLastRow(self):
        query = 'SELECT * FROM sessions ORDER BY id DESC LIMIT 1'
        return sqlQueries(database=self.database, query=query)

    def sessionStatus(self):
        self.live = False
        row = self.getLastRow()
        try:
            if row[0][1] == 1 : self.live = True
            return self.live
        except:
            return self.live

    def createSession(self):
        query = 'INSERT INTO sessions VALUES (?,?)'
        sqlQueries(database=self.database, query=query, POST=True, arg=(None,1))

    def deleteSession(self):
        try:
            row = self.getLastRow()
            query_update = 'UPDATE sessions SET session_status = 0 WHERE id = '+str(row[0][0])
            sqlQueries(database=self.database, query=query_update, override=True)
        except:
            pass


def newline(x):
    for _ in range(x):
        st.markdown('\n')

def sqlQueries(database,query,POST=False,arg=None,override=False):
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