import streamlit as st
import sqlite3
import os

from MissionCompiler import readMission
 


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


def compile_missionFile(file):
    data = file.read()
    with open('Mission.txt','w+') as f:
        f.write(data.decode('utf-8'))
    readMission(filename='Mission.txt')
    os.remove('Mission.txt')