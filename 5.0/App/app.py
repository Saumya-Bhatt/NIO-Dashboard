import streamlit as st
import pandas as pd

import sqlite3
#st.set_page_config(layout="wide")

from frame import newline, sqlQueries

st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine AUV Dashboard')

AUV_BOT_NAME = ''
AUV_BOT_ID = ''

def loginInstance():

    global AUV_BOT_NAME, AUV_BOT_ID

    st.write("Generate, set or delete any AUV instances from this panel. Dashboard's functionalities cannot be used if an instance is not set.")

    col1, col2= st.beta_columns(2)
    temp_name = col1.text_input('Enter AUV bot name :',key='auvBotName')
    temp_id = col2.text_input('Enter AUV bot ID :',key='auvBotID')
    submit = col1.button('Generate AUV Instance')

    if submit:
        if temp_name == '':
            st.error('Please give a name to the AUV bot instance!')
        elif temp_id == '':
            st.error('Please give a reference ID to the AUV bot instance!')
        else:
            query = "INSERT INTO instance_log VALUES (?,?,?)"
            arg = [None,temp_name,temp_id]
            sqlQueries(query=query, POST=True, arg=arg)
            AUV_BOT_NAME = temp_name
            AUV_BOT_ID = temp_id
            temp_name = ''
            temp_id = ''
            st.success('AUV bot instance created!')


    delcol, instanceTable = st.beta_columns(2)

    delAUVInst = delcol.text_input('Enter the AUV bot ID to remove instance :')
    submitDel = delcol.button('Delete AUV Instance')
    if submitDel:
        if delAUVInst == '':
            st.error('Please enter an AUV reference ID to delete!')
        else:
            try:
                query = "DELETE FROM instance_log WHERE auv_id=?"
                arg = (delAUVInst,)
                sqlQueries(query=query, POST=True, arg=arg)
                st.success('The given AUV instance was deleted!')
                if delAUVInst == AUV_BOT_ID:
                    AUV_BOT_ID = ''
                    AUV_BOT_NAME = ''
                    delAUVInst = ''
            except:
                st.error('No instance of the input reference ID is running!') 


    query = "SELECT * from instance_log"
    records = sqlQueries(query=query)


    df = pd.DataFrame(records, columns=['ID','AUV Name','AUV Ref. ID'])
    instanceTable.markdown('All AUV instances running:')
    instanceTable.write(df)

    newline(1)
    st.markdown('Set an AUV instance for this dashboard by specifying its reference ID :')


   

instance_expander = st.beta_expander("AUV Instance generation and monitoring panel")
with instance_expander:
    clicked = loginInstance()


st.sidebar.markdown('__Currently running instance : __')
st.sidebar.markdown('Name : &nbsp&nbsp&nbsp'+AUV_BOT_NAME)
st.sidebar.markdown('Reference ID : &nbsp&nbsp'+AUV_BOT_ID) 
st.sidebar.button('Remove Instance Pointer')