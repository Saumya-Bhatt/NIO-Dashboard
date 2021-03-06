import streamlit as st
import mysql.connector
import sqlite3

import pandas as pd


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
    return None



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



def global_sessions(session, instance):
    if session.session_status():
        try:
            instID = session.get_last_row()[0][1]
            val = instance.get_instance(instID)
            return [val[0][0], val[0][1], val[0][2]]
        except:
            return [None, None, None]      
    return [None, None, None]



def df_mission_file(mission):
    return pd.DataFrame(mission.get_missions(), columns=['ID','Mission','Timestamp','Status','Inst'])



def location_frame(data):
    COORDINATES = {
        'HOME' : [float(data[1]),float(data[2]),'🟢'],
        'BOAT' : [float(data[3]),float(data[4]),'🔵'],
        'C-BOT' : [float(data[5]),float(data[6]),'🔴']
    }
    return COORDINATES, pd.DataFrame(COORDINATES, index=['Latitude','Longitude', 'Marker'])