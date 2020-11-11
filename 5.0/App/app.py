import streamlit as st
import pandas as pd

from text import StatusCodes
from frame import newline, sqlQueries, SessionManager
from streamlit_metrics import metric_row


st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine AUV Dashboard')

status_code = StatusCodes(st.sidebar.empty())
session = SessionManager('sessionManager.db')
AUV_BOT_NAME = None
AUV_BOT_ID = None

def loginInstance():

    global AUV_BOT_NAME, AUV_BOT_ID

    st.write("_Generate, set or delete any AUV instances from this panel. Dashboard's functionalities cannot be accessed if an instance is not set._")

    col1, col2, col3= st.beta_columns([3,3,1])
    temp_name = col1.text_input('Enter AUV bot name :',key='auvBotName')
    temp_id = col2.text_input('Enter AUV bot ID :',key='auvBotID')
    submit = col3.button('Generate AUV Instance')

    if submit:
        if temp_name == '':
            status_code.setCode('error',0)
        elif temp_id == '':
            status_code.setCode('error',1)
        else:
            query = "INSERT INTO instance_log VALUES (?,?,?)"
            sqlQueries(database='instanceManager.db', query=query, POST=True, arg=[None,temp_name,temp_id])
            AUV_BOT_NAME = temp_name
            AUV_BOT_ID = temp_id
            status_code.setCode('success',0)

    col4, col5 = st.beta_columns([3,4])
    delAUVInst = col4.text_input('Enter the AUV bot ID to remove instance :')
    submitDel = col4.button('Delete AUV Instance')

    if submitDel:
        if delAUVInst == '':
            status_code.setCode('error',2)
        else:
            try:
                query = "DELETE FROM instance_log WHERE auv_id=?"
                sqlQueries(database='instanceManager.db', query=query, POST=True, arg=(delAUVInst,))
                status_code.setCode('success',1)
                if delAUVInst == AUV_BOT_ID:
                    AUV_BOT_ID = ''
                    AUV_BOT_NAME = ''
                    delAUVInst = ''
            except:
                status_code.setCode('info',1)


    query = "SELECT * from instance_log"
    records = sqlQueries(database='instanceManager.db', query=query)


    df = pd.DataFrame(records, columns=['ID','AUV Name','AUV Ref. ID'])
    col5.markdown('__All AUV instances running:__')
    col5.write(df)
    col5.button('Refresh table')

    newline(1, element=col4)
    col4.markdown('Set an AUV instance for this current session by specifying its reference ID :')
    setInstance = col4.text_input('Enter AUV reference ID')
    confirmInstance = col4.button('Set AUV Instance')
    if confirmInstance:
        if setInstance == '':
            status_code.setCode('error',3)
        else:
            session.createSession()
            status_code.setCode('success',2)


   

instance_expander = st.beta_expander("⚙️ AUV Instance generation and monitoring panel")
with instance_expander:
    clicked = loginInstance()

st.sidebar.header('Instance Monitor')
st.sidebar.markdown('Name : &nbsp&nbsp&nbsp **'+str(AUV_BOT_NAME)+'**')
st.sidebar.markdown('Reference ID : &nbsp&nbsp **'+str(AUV_BOT_ID)+'**')
sessionStatus = st.sidebar.empty()
if session.sessionStatus():
    sessionStatus.markdown('Session Token Status : ✅ _RUNNING_')
else:
    sessionStatus.markdown('Session Token status : 🟠 _NOT SET_')
cachedSessions = st.sidebar.checkbox('Destroy cached sessions')
if st.sidebar.button('Remove current session'):
    if session.sessionStatus():
        if cachedSessions:
            session.destroyAllSessions()
            status_code.setCode('warning',0)
            sessionStatus.markdown('Session Token Status : 🟥 DESTROYED')
        else:
            session.deleteSession()
            sessionStatus.markdown('Session Token Status : 🟠 NOT SET')
            status_code.setCode('warning',1)
    else:
        status_code.setCode('info',1)


if session.sessionStatus():
    newline(1, sidebar=True)
    battery = 72
    quote = "Battery Status : "+str(battery)+" %"
    st.sidebar.markdown(quote)
    st.sidebar.progress(battery)
    metric_row(
        {
            "Roll": 100,
            "Pitch": 200,
            "Yaw": 300,
            "Depth": '400 m',
        }
    )

    st.sidebar.header('Navigation')
    functionality = st.sidebar.selectbox('Select functionality to open console',
                    ('None','Real-time Mapping','Mission File Upload','Onboard Camera Feed'))
    if functionality == 'Real-time Mapping':
        st.header('Real-time Mapping')
    elif functionality == 'Mission File Upload':
        st.header('Mission File Upload')
    elif functionality == 'Onboard Camera Feed':
        st.header('Onboard Camera Feed')
    else:
        pass


    st.sidebar.markdown('_Press if dashboard overloads_')
    st.sidebar.button('Kill all processes')