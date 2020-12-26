########################################################

# AUV Dashboard GUI made for CSIR-NIO
# Author: Saumya Bhatt, BITS Goa

###################################################


import schedule
import time
import streamlit as st
import pandas as pd

from modules import models
from modules.text import StatusCodes, MethodIntro
from modules.frame import newline, global_sessions, df_mission_file
from functions.Camera import streamVideo






#==================================================================================
#===============================           ========================================
#===============================  HEADERS  ========================================
#===============================           ========================================
#==================================================================================


st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine AUV Dashboard')

status_code = StatusCodes(st.sidebar.empty())
method = MethodIntro()
session = models.SessionManager('SessionManager.db')
instance = models.InstanceManager('127.0.0.1','nio_server')

REFERENCE_ID, AUV_BOT_NAME, AUV_BOT_ID = global_sessions(session, instance)

mission = models.MissionUpload(REFERENCE_ID, instance)
statusValues = models.StatusValues(REFERENCE_ID, instance)






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
    number_instances = len(instance.get_all_instances())
    col5.markdown('__All AUV instances running:__ &nbsp&nbsp' + str(number_instances))
    col5.write(df)



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
st.sidebar.markdown('ID tracking : &nbsp&nbsp **' + str(REFERENCE_ID) + '**')
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
#===============================  VALUE STATUS  ===================================
#==================================================================================


col1, col2 = st.beta_columns([1,2])
if session.session_status():
    newline(1, sidebar=True)
    BATTERY_STATUS = col1.empty()
    BATTERY_STATUS_PG = col1.empty()
    STATUS_VALUES = col2.empty()



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
        method.MissionFileUpload()
        currentTable = st.empty()
        col1, col2 = st.beta_columns([2,1])
        file_status = col1.empty()

        currentTable.table(df_mission_file(mission))
        file_status.markdown('Current Mission File Status : &nbsp&nbsp' + mission.get_status())


        mission_file = col1.file_uploader('Upload Mission file to server')
        if col1.button('Upload mission file'):
            if mission_file is not None:
                MISSION_FILE = mission.compile(mission_file)
                mission.upload(MISSION_FILE)
                status_code.set_code('success',3)
                currentTable.table(df_mission_file(mission))
                file_status.markdown('Current Mission File Status : &nbsp&nbsp' + mission.get_status('upload'))
            else:
                status_code.set_code('error',6)


        mission_ID_Tracking = col2.text_input('Set Mission File ID to perform below mentioned operations')

        if col2.button('Remove set mission file'):
            if mission.remove(mission_ID_Tracking):
                currentTable.table(df_mission_file(mission))
                file_status.markdown('Current Mission File Status : &nbsp&nbsp' + mission.get_status('remove'))
                status_code.set_code('warning',3)
            else:
                status_code.set_code('error',7)

        if col2.button('Abort set mission file'):
            if mission.abort(mission_ID_Tracking):
                currentTable.table(df_mission_file(mission))
                file_status.markdown('Current Mission File Status : &nbsp&nbsp' + mission.get_status('abort'))
                status_code.set_code('warning',4)
            else:
                status_code.set_code('error',7)

        if col2.button('Run set mission file'):
            if mission.run(mission_ID_Tracking):
                currentTable.table(df_mission_file(mission))
                file_status.markdown('Current Mission File Status : &nbsp&nbsp' + mission.get_status('run'))
                status_code.set_code('success',4)
            else:
                status_code.set_code('error',7)



    #========================= CAMERA =============================================
    elif functionality == 'Onboard Camera Feed':

        st.header('Onboard Camera Feed')
        method.OnboardCamera()
        URL = st.text_input('Enter Network URL below [eg.  192.168.43.121:8080] :')
        if st.button('Generate live feed stream'):

            try:
                streamVideo(URL)
                status_code.set_code('success',5)
            except:
                method.MissionFileUpload()



    else:
        pass






#==================================================================================
#===========================                     ==================================
#=========================== SCHEDULE PROCESSES  ==================================
#===========================                     ==================================
#================================================================================== 



#==================================================================================
#============================  SCHEDULE FUNCTIONS  ================================
#==================================================================================


    def update_values():
        values = statusValues.get_current_values()
        quote = "__Battery Status : __"+str(values[1])+" %"
        BATTERY_STATUS.markdown(quote)
        if values[1] != 'NaN':
            BATTERY_STATUS_PG.progress(int(values[1]))

        frame = {
        'ROLL' : [values[2]],
        'PITCH' : [values[3]],
        'YAW' : [values[4]],
        'DEPTH' : [values[5]]
        }
        STATUS_VALUES.table(frame)



#==================================================================================
#============================  KILL PROCESS  ======================================
#==================================================================================


    newline(1,sidebar=True)
    if st.sidebar.checkbox('Kill all processes'):
        method.killProcess()
        schedule.cancel_job(update_values)
        schedule.clear('update_values')
        st.stop()


    
#==================================================================================
#============================  SCHEDULING THREAD  =================================
#==================================================================================


    schedule.every(2).seconds.do(update_values).tag('update_values')

    while True: 
        schedule.run_pending() 
        time.sleep(1)