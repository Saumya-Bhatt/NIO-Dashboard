import streamlit as st
import pandas as pd

from text import StatusCodes
from frame import newline, sql_queries, SessionManager, InstanceManager
from streamlit_metrics import metric_row


st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine AUV Dashboard')

status_code = StatusCodes(st.sidebar.empty())
session = SessionManager('sessionManager.db')
instance = InstanceManager('instanceManager.db')

AUV_BOT_NAME = None
AUV_BOT_ID = None

def loginInstance():

    global AUV_BOT_NAME, AUV_BOT_ID
    st.write("_Generate, set, delete AUV instances from this panel. Dashboard's functionalities cannot be accessed if an instance is not set._")

    col1, col2, col3= st.beta_columns([3,3,1])
    temp_name = col1.text_input('Enter AUV bot name :',key='auvBotName')
    temp_id = col2.text_input('Enter AUV bot ID :',key='auvBotID')
    newline(1, element=col3)
    submit = col3.button('Generate Instance')

    if submit:
        if temp_name == '':
            status_code.set_code('error',0)
        elif temp_id == '':
            status_code.set_code('error',1)
        else:
            if instance.generate_instance(temp_name, temp_id):
                status_code.set_code('success',0)
            else:
                status_code.set_code('error',4)

    col4, col5 = st.beta_columns([3,4])
    delAUVInst = col4.text_input('Enter the corresponding ID to remove instance :')
    submitDel = col4.button('Delete AUV Instance')

    if submitDel:
        if delAUVInst == '':
            status_code.set_code('error',2)
        else:
            if instance.delete_instance(delAUVInst):
                status_code.set_code('success',1)
            else:
                status_code.set_code('error',5)


    df = pd.DataFrame(instance.get_all_instances(), columns=['ID','AUV Name','AUV Ref. ID'])
    col5.markdown('__All AUV instances running:__')
    col5.write(df)
    col5.button('Refresh table')

    col4.markdown('Set current AUV Instance session :')
    setInstance = col4.text_input('Enter AUV ID')
    confirmInstance = col4.button('Set AUV Instance')
    if confirmInstance:
        if setInstance == '':
            status_code.set_code('error',3)
        else:
            session.create_session()
            status_code.set_code('success',2)


    newline(1)
    destroyInstances = st.checkbox('⚠️ Destroy all Instances')
    if destroyInstances:
        status_code.set_code('warning',2)
        confirmDelete = st.button('I understand the consequences. Confirm Delete')
        if confirmDelete:
            session.destroy_all_sessions()
            instance.destroy_all_instances()
            status_code.set_code('info',1)
            


   

instance_expander = st.beta_expander("⚙️ AUV Instance generation and monitoring panel")
with instance_expander:
    clicked = loginInstance()

st.sidebar.header('Instance Monitor')
st.sidebar.markdown('Name : &nbsp&nbsp&nbsp **'+str(AUV_BOT_NAME)+'**')
st.sidebar.markdown('Reference ID : &nbsp&nbsp **'+str(AUV_BOT_ID)+'**')
sessionStatus = st.sidebar.empty()
if session.session_status():
    sessionStatus.markdown('Session Token Status : ✅ _RUNNING_')
else:
    sessionStatus.markdown('Session Token status : 🟠 _NOT SET_')
cachedSessions = st.sidebar.checkbox('Destroy cached sessions')
if st.sidebar.button('Remove current session'):
    if session.session_status():
        if cachedSessions:
            session.destroy_all_sessions()
            status_code.set_code('warning',0)
            sessionStatus.markdown('Session Token Status : 🟥 DESTROYED')
        else:
            session.delete_session()
            sessionStatus.markdown('Session Token Status : 🟠 NOT SET')
            status_code.set_code('warning',1)
    else:
        status_code.set_code('info',0)


if session.session_status():
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