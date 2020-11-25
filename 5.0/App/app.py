########################################################

# AUV Dashboard GUI made for NIO
# Author: Saumya Bhatt, BITS Goa

###################################################



import streamlit as st
import pandas as pd

from text import StatusCodes
from models import SessionManager, InstanceManager
from frame import newline, compile_missionFile, global_sessions
from streamlit_metrics import metric_row





#==================================================================================
#===============================           ========================================
#===============================  HEADERS  ========================================
#===============================           ========================================
#==================================================================================


st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine AUV Dashboard')

status_code = StatusCodes(st.sidebar.empty())
session = SessionManager('SessionManager.db')
instance = InstanceManager('127.0.0.1','nio_server')

AUV_BOT_NAME, AUV_BOT_ID = global_sessions(session, instance)





#==================================================================================
#===============================               ====================================
#===============================  LOGIN PANEL  ====================================
#===============================               ====================================
#==================================================================================


def loginInstance():

    global AUV_BOT_NAME, AUV_BOT_ID
    st.write("_Generate, set, delete AUV instances from this panel. Dashboard's functionalities cannot be accessed if an instance is not set._")


    #===================== GENERATE INSTANCE =========================================
    col1, col2, col3= st.beta_columns([3,3,1])
    temp_name = col1.text_input('Enter AUV bot name :',key='auvBotName')
    temp_key = col2.text_input('Enter AUV bot Key :',key='auvBotKey')
    newline(1, element=col3)
    submit = col3.button('Generate Instance')

    if submit:
        if temp_name == '':
            status_code.set_code('error',0)
        elif temp_key == '':
            status_code.set_code('error',1)
        else:
            if instance.generate_instance(temp_name, temp_key):
                status_code.set_code('success',0)
            else:
                status_code.set_code('error',4)


    #============================ DELETE INSTANCE ======================================
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


    #================================ ALL INSTANCES RUNNING ================================
    df = pd.DataFrame(instance.get_all_instances(), columns=['ID','AUV Name','AUV Key'])
    col5.markdown('__All AUV instances running:__')
    col5.write(df)
    col5.button('Refresh table')


    #================================== SET INSTANCE SESSION ================================
    setInstance = col4.text_input('Enter AUV ID to set session')
    confirmInstance = col4.button('Set AUV session')
    if confirmInstance:
        if setInstance == '':
            status_code.set_code('error',3)
        else:
            val = instance.get_instance(setInstance)
            AUV_BOT_NAME = val[0][1]
            AUV_BOT_ID = val[0][2]
            session.create_session(setInstance)
            status_code.set_code('success',2)


    #====================================== DELETE INSTANCES ==================================
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





#==================================================================================
#===============================           ========================================
#===============================  SIDEBAR  ========================================
#===============================           ========================================
#================================================================================== 
   

st.sidebar.header('Instance Monitor')
st.sidebar.markdown('Name : &nbsp&nbsp&nbsp **'+str(AUV_BOT_NAME)+'**')
st.sidebar.markdown('AUV Key : &nbsp&nbsp **'+str(AUV_BOT_ID)+'**')
sessionStatus = st.sidebar.empty()


#==================================================================================
#==============================  INSTANCE MANAGER  ================================
#==================================================================================


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
        AUV_BOT_NAME = None
        AUV_BOT_ID = None
    else:
        status_code.set_code('info',0)


#==================================================================================
#===============================  BOT STATUS  =====================================
#==================================================================================

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


#==================================================================================
#=========================  FUNCTIONALITIES  ======================================
#==================================================================================

    st.sidebar.header('Navigation')
    functionality = st.sidebar.selectbox('Select functionality to open console',
                    ('None','Real-time Mapping','Mission File Upload','Onboard Camera Feed'))


    #====================== MAPPING ================================================
    if functionality == 'Real-time Mapping':
        st.header('Real-time Mapping')


    #======================= FILE UPLOAD ===========================================
    elif functionality == 'Mission File Upload':

        st.header('Mission File Upload')
        mission_file = st.file_uploader('Upload Mission file to server')
        compile = st.button('Compile')
        if compile:
            if mission_file is not None:
                try:
                    compile_missionFile(mission_file)
                    status_code.set_code('success',3)
                except:
                    status_code.set_code('error',7)
            else:
                status_code.set_code('error',6)

    #========================= CAMERA =============================================
    elif functionality == 'Onboard Camera Feed':
        st.header('Onboard Camera Feed')



    else:
        pass


    st.sidebar.markdown('_Press if dashboard overloads_')
    st.sidebar.button('Kill all processes')