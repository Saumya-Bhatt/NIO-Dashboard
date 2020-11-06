import streamlit as st

import sqlite3

def newline(x):
    for _ in range(x):
        st.markdown('\n')

def sqlQueries(query,POST=False,arg=None):
    conn = sqlite3.connect('instanceManager.db')
    curr = conn.cursor()

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