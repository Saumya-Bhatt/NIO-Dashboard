import matplotlib.pyplot as plt
import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

import matplotlib
import schedule
import datetime
import logging
import time
import utm
import cv2
import sys
import os

from fileSQL import upload_mission, run_mission, abort_mission, current_uploads, table_empty
from frame import data_frame, cleanFile, saveImage, positionFrame, sql_queries_dynamic
from posSQL import get_home_pos, get_boat_pos, get_cbot_pos
from text import newline, MethodIntro, BigInst, Headers
from onlineMap import getOnlineMap
from streamlit import caching
from cam import streamVideo





#=============================================================================
#========================== HEADERS ==========================================
#=============================================================================

st.set_option('deprecation.showfileUploaderEncoding', False)
logging.getLogger('schedule').propagate = False
font = {'family' : 'DejaVu Sans',
        'weight' : 'light',
        'size'   : 5}
matplotlib.rc('font', **font)

method = MethodIntro()
instructions = BigInst()
headers = Headers()

instructions.header()
dt_time = st.empty()
dt_date = st.empty()

battery_status = st.sidebar.empty()
battery_status_pg = st.sidebar.empty()
pitch_and_yaw_status = st.sidebar.empty()
cmd_status = st.sidebar.empty()





#=============================================================================
#====================== SCHEDULE FUNCTIONS ===================================
#=============================================================================


def get_time():
    get_current = datetime.datetime.now()
    current = get_current.strftime("%H:%M:%S")
    return dt_time.markdown('__Time__ : %s'%current)

def get_date():
    today = datetime.date.today()
    return dt_date.markdown('__Date__ : %s'%today)

def get_integer_values():

    query0 = "SELECT * FROM battery_value ORDER BY id DESC LIMIT 1"
    query1 = "SELECT * FROM pitch_value ORDER BY id DESC LIMIT 1"
    query2 = "SELECT * FROM yaw_value ORDER BY id DESC LIMIT 1"
    query3 = "SELECT * FROM depth ORDER BY id DESC LIMIT 1"

    returned_battery_data = sql_queries_dynamic(query0)
    returned_data_pitch = sql_queries_dynamic(query1)
    returned_data_yaw = sql_queries_dynamic(query2)

    if len(returned_battery_data) != 0:
        bat_val = returned_battery_data[0][1]
        if isinstance(bat_val,int):
            battery_status_pg.progress(bat_val)
            battery_status.markdown('__Battery Status__ : '+str(bat_val)+' %')
        else:
            battery_status.markdown('__Battery Status__ : NaN')
    else:
        cmd_status.error('BATTERY TABLE ENTRY IS NULL')

    if len(returned_data_pitch) == 0:
        yaw_val = returned_data_yaw[0][1]
        pitch_and_yaw_status.markdown('__Pitch__ : NULL &nbsp&nbsp&nbsp&nbsp&nbsp __Yaw__ : {}'.format(str(yaw_val)))
    elif len(returned_data_yaw) == 0:
        pitch_val = returned_data_pitch[0][1]
        pitch_and_yaw_status.markdown('__Pitch__ : {} &nbsp&nbsp&nbsp&nbsp&nbsp __Yaw__ : NULL'.format(str(pitch_val)))
    else:
        yaw_val = returned_data_yaw[0][1]
        pitch_val = returned_data_pitch[0][1]
        pitch_and_yaw_status.markdown('__Pitch__ : {} &nbsp&nbsp&nbsp&nbsp&nbsp __Yaw__ : {}'.format(str(pitch_val),str(yaw_val)))

    return None





#=========================================================================================
#=============================== POSITION (MAP) ==========================================
#=========================================================================================


headers.position()
if st.sidebar.checkbox('Open Console',False,key=1):

    method.positionConsole()

    get_home = get_home_pos()
    get_boat = get_boat_pos()
    get_cbot = get_cbot_pos()

    DATA_INDEX = pd.DataFrame(data_frame(positionFrame(get_home,get_boat,get_cbot)),index=['Longitude','Latitude','Marker'])

    startOfflineMap = st.checkbox('Open Offline Map',key='offline_map')
    if startOfflineMap:

        if st.checkbox('Read Instructions',False,key='inst'):
            instructions.offlineMapInstr()
        if st.button('Clear Buffer data'):
            try:
                os.system('del UPLOAD/buffer.png')
                uploaded_file = None
                st.success('You are good to go')
            except:
                st.warning('No image currently in use')
        st.markdown('Not clearing buffer data before proceeding will show the previously used data')
        

        REFLOC = st.file_uploader('Enter a reference location file [.TXT]',type='txt',key='refloc')
        UPLOADED_FILE = st.file_uploader("Choose an image file [.PNG]", type="png", key='map')

        if REFLOC is not None and UPLOADED_FILE is not None:

            headers.coordinates()
            offline_locations = st.empty()

            data = cleanFile(REFLOC)
            refloc = [[data[0][0],data[0][1]],[data[1][0],data[1][1]]]
            loc1 = utm.from_latlon(float(refloc[0][0]),float(refloc[0][1]))
            loc2 = utm.from_latlon(float(refloc[1][0]),float(refloc[1][1]))


            width, height, map_plot = saveImage(UPLOADED_FILE)
            scale_x = width/abs(loc1[0]-loc2[0])
            scale_y = height/abs(loc1[1]-loc2[1])
            arr = np.asarray(map_plot)
            bounding_box = (width,0,height,0)
        
            temp = st.empty()
            def animateOffline():
                fig = plt.figure()
                ax = fig.add_subplot()

                # getting data from database (has to be updated in realtime)
                get_home = get_home_pos()
                get_boat = get_boat_pos()
                get_cbot = get_cbot_pos()

                try:
                    HOME_POSITION, BOAT_POSITION, CBOT_POSITION = positionFrame(get_home, get_boat, get_cbot)

                    home = utm.from_latlon(HOME_POSITION[1],HOME_POSITION[0])
                    boat = utm.from_latlon(BOAT_POSITION[1],BOAT_POSITION[0])
                    cbot = utm.from_latlon(CBOT_POSITION[1],CBOT_POSITION[0])

                    latitude = [(loc1[0]-home[0])*scale_x+width,(loc1[0]-boat[0])*scale_x+width,(loc1[0]-cbot[0])*scale_x+width]
                    longitude = [(loc2[1]-home[1])*scale_y+height,(loc2[1]-boat[1])*scale_y+height,(loc2[1]-cbot[1])*scale_y+height]

                    global DATA_INDEX
                    offline_locations.dataframe(DATA_INDEX)

                    # plotting the data onto the figure
                    ax.scatter(latitude[0],longitude[0],color='green',s=20, label='home position')
                    ax.scatter(latitude[1],longitude[1],color='blue',s=20, label='boat position')
                    ax.scatter(latitude[2],longitude[2],color='red',s=20, label='c-bot position')
                    ax.imshow(arr,extent=bounding_box,cmap='gray')
                    plt.legend(loc=2)
                    temp.pyplot(fig)
                    time.sleep(3)
                    plt.close()

                except:
                    st.error('There are currently no positions in the locations database. First add them at the server-side panel.')

                return None

            schedule.every(2).seconds.do(animateOffline).tag('offlineMap')
            while True: 
                schedule.run_pending() 
                time.sleep(2)

    newline(1)

    if st.checkbox('Open online Map',key='online_map'):
        st.markdown('The dashboard will display the map of the last location file entered unless a new one is uploaded.')

        online_map = st.empty()
        headers.coordinates(offline=False)
        online_locations = st.empty()

        def get_online_map():
            get_home = get_home_pos()
            get_boat = get_boat_pos()
            get_cbot = get_cbot_pos()

            try:
                HOME_POSITION, BOAT_POSITION, CBOT_POSITION = positionFrame(get_home, get_boat, get_cbot, reverse=True)

                map_info = getOnlineMap(HOME_POSITION,BOAT_POSITION,CBOT_POSITION)
                online_map.pydeck_chart(map_info)

                global DATA_INDEX
                online_locations.dataframe(DATA_INDEX)
                time.sleep(4)
            except:
                st.error('There are currently no positions in the locations database. First add them at the server-side panel.')

            return None

        schedule.every(2).seconds.do(get_online_map).tag('onlineMap')
        while True: 
            schedule.run_pending() 
            time.sleep(1)





#=====================================================================================================
#===================================== MISSION CONTROL ===============================================
#=====================================================================================================


headers.missionControl()
if st.sidebar.checkbox('Open Dashboard',False,key=2):

    method.missionFile()
    current_table = st.empty()
    current_table.table(current_uploads())
    st.markdown('Press __ctrl + shift + r__ if the table does not refresh automatically.')

    upload_status = st.empty()
    uploaded_file = st.file_uploader("Choose a Mission file", type="txt")

    if st.button('Load Mission'):
        if uploaded_file is None:
            st.error('Please upload a file')
        else:
            try:
                #create_file(uploaded_file)
                upload_mission(uploaded_file)
                cmd_status.success('Uploaded files to server')
                upload_status.markdown('Upload Status : :ok:')
                current_table.table(current_uploads())
            except:
                e = sys.exc_info()[0]
                cmd_status.error('ERROR connecting to database : %s'%(e))

    if st.button('Run Mission'):
        if table_empty()==False:
            try:
                run_mission()
                cmd_status.success('Mission file running successfully')
                upload_status.markdown('Upload Status : :white_check_mark:')
                current_table.table(current_uploads())
            except:
                e = sys.exc_info()[0]
                cmd_status.error('ERROR connecting to database : %s'%(e))
        else:
            st.error('Please upload a file to run')

    if st.button('Abort Mission'):
        if table_empty()==False:
            try:
                abort_mission()
                cmd_status.success('Mission aborted sucessfully')
                upload_status.markdown('Upload Status : :ab:')
                uploaded_file = None
                current_table.table(current_uploads())
            except:
                e = sys.exc_info()[0]
                cmd_status.error('ERROR connecting to database : %s'%(e))
        else:
            st.error('No file is uploaded yet')





#=====================================================================================================
#========================================== CAMERA FEED ==============================================
#=====================================================================================================


headers.cameraFeed()
if st.sidebar.checkbox('Open Dashboard', False,key=3):
    method.cameraConsole()

    if st.checkbox('Read Instructions',False,key='cam_inst'):
        instructions.cameraInstr()

    URL = st.text_input('Enter the url of the network stream : ')
    try:
        if URL != '':
            streamVideo(URL)
    except:
        cmd_status.warning('Unable to reach the streaming network')





#=============================================================================================
#=============================== KILL TASKS ==================================================
#=============================================================================================


if st.sidebar.button('Kill all process'):
    instructions.killProcess()
    schedule.cancel_job(get_time)
    schedule.cancel_job(get_date)
    schedule.cancel_job(get_integer_values)
    schedule.clear('datetime')
    schedule.clear('integer')
    try:
        schedule.clear('offlineMap')
    except:
        print('Offline Mapping stopped')
    try:
        schedule.clear('onlineMap')
    except:
        print('Online Map Stopped')
    caching.clear_cache()
    st.stop()





#================================================================================================
#=============================== TASK SCHEDULING CALLS ==========================================
#================================================================================================


get_date()
get_integer_values()

schedule.every(1).seconds.do(get_time).tag('datetime')
schedule.every(24).hours.do(get_date).tag('datetime')
schedule.every(10).seconds.do(get_integer_values).tag('integer')

while True: 
    schedule.run_pending() 
    time.sleep(1)