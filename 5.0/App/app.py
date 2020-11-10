from os import stat
import streamlit as st
import pandas as pd
#st.set_page_config(layout="wide")

from frame import newline, sqlQueries, SessionManager
from streamlit_metrics import metric_row


st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine AUV Dashboard')


status = st.sidebar.empty()
session = SessionManager('sessionManager.db')
AUV_BOT_NAME = ''
AUV_BOT_ID = ''

def loginInstance():

    global AUV_BOT_NAME, AUV_BOT_ID

    st.write("Generate, set or delete any AUV instances from this panel. Dashboard's functionalities cannot be accessed if an instance is not set.")

    col1, col2= st.beta_columns(2)
    temp_name = col1.text_input('Enter AUV bot name :',key='auvBotName')
    temp_id = col2.text_input('Enter AUV bot ID :',key='auvBotID')
    submit = col1.button('Generate AUV Instance')

    if submit:
        if temp_name == '':
            status.error('Please give a name to the AUV bot instance!')
        elif temp_id == '':
            status.error('Please give a reference ID to the AUV bot instance!')
        else:
            query = "INSERT INTO instance_log VALUES (?,?,?)"
            sqlQueries(database='instanceManager.db', query=query, POST=True, arg=[None,temp_name,temp_id])
            AUV_BOT_NAME = temp_name
            AUV_BOT_ID = temp_id
            status.success('AUV bot instance created!')


    delcol, instanceTable = st.beta_columns(2)

    delAUVInst = delcol.text_input('Enter the AUV bot ID to remove instance :')
    submitDel = delcol.button('Delete AUV Instance')
    if submitDel:
        if delAUVInst == '':
            status.error('Please enter an AUV reference ID to delete!')
        else:
            try:
                query = "DELETE FROM instance_log WHERE auv_id=?"
                sqlQueries(database='instanceManager.db', query=query, POST=True, arg=(delAUVInst,))
                status.success('The given AUV instance was deleted!')
                if delAUVInst == AUV_BOT_ID:
                    AUV_BOT_ID = ''
                    AUV_BOT_NAME = ''
                    delAUVInst = ''
            except:
                status.error('No instance of the input reference ID is running!') 


    query = "SELECT * from instance_log"
    records = sqlQueries(database='instanceManager.db', query=query)


    df = pd.DataFrame(records, columns=['ID','AUV Name','AUV Ref. ID'])
    instanceTable.markdown('All AUV instances running:')
    instanceTable.write(df)

    newline(1)
    st.markdown('Set an AUV instance for this dashboard by specifying its reference ID :')
    if st.button('Set session'):
        session.createSession()
        status.success('Session instance running!')


   

instance_expander = st.beta_expander("⚙️ AUV Instance generation and monitoring panel")
with instance_expander:
    clicked = loginInstance()

st.sidebar.header('Currently running instance :')
sessionStatus = st.sidebar.empty()
if session.sessionStatus():
    sessionStatus.markdown('Session Token status : ✅ RUNNING')
else:
    sessionStatus.markdown('Session Token status : 🟠 NOT SET')
st.sidebar.markdown('Name : &nbsp&nbsp&nbsp'+AUV_BOT_NAME)
st.sidebar.markdown('Reference ID : &nbsp&nbsp'+AUV_BOT_ID)
if st.sidebar.button('Remove current session'):
    if session.sessionStatus():
        session.deleteSession()
        sessionStatus.markdown('Session Token status : 🟠 NOT SET')
        status.warning('Current session token was destroyed')
    else:
        status.info('There is no session currently in use')


if session.sessionStatus():
    st.sidebar.markdown('\n')
    battery = 72
    quote = "Battery Status : "+str(battery)+" %"
    st.sidebar.markdown(quote)
    st.sidebar.progress(battery)
    st.sidebar.markdown('\n')
    metric_row(
        {
            "Roll": 100,
            "Pitch": 200,
            "Yaw": 300,
            "Depth": '400 m',
        }
    )



st.sidebar.header('Navigation')
functionality = st.sidebar.selectbox('Select functionality to open console',('None','Real-time Mapping','Mission File Upload','Onboard Camera Feed'))
if functionality == 'Real-time Mapping':
    st.header('Real-time Mapping')
elif functionality == 'Mission File Upload':
    st.header('Mission File Upload')
elif functionality == 'Onboard Camera Feed':
    st.header('Onboard Camera Feed')
else:
    pass


st.sidebar.markdown('\n')
st.sidebar.markdown('_Press if dashboard overloads_')
st.sidebar.button('Kill all processes')