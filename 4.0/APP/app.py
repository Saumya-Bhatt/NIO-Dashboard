import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
import schedule
import datetime
import time
import sys
import os
import cv2
import utm
import json

from PIL import Image
from cam import streamVideo
from onlineMap import getOnlineMap
from offlineMap import getOfflineMap
from frame import newline, battery, data_frame, cleanFile
from fileSQL import upload_mission, run_mission, abort_mission, current_uploads, table_empty
from posSQL import get_home_pos, get_boat_pos, get_cbot_pos


st.set_option('deprecation.showfileUploaderEncoding', False)
font = {'family' : 'DejaVu Sans',
        'weight' : 'light',
        'size'   : 5}
matplotlib.rc('font', **font)


#--------------------------VIDEO--------------------------------------------
#video_file = open('video.mp4','rb')
#video_bytes = video_file.read()



#--------------------------HEADING--------------------------------------------
st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine robot dashboard')

newline(2)

dt_time = st.empty()
dt_date = st.empty()

def get_time():
    get_current = datetime.datetime.now()
    current = get_current.strftime("%H:%M:%S")
    return dt_time.markdown('__Time__ : %s'%current)

def get_date():
    today = datetime.date.today()
    return dt_date.markdown('__Date__ : %s'%today)

st.sidebar.markdown('__Battery Status__ : %d %%'%battery)
battery = st.sidebar.progress(battery)

cmd_status = st.sidebar.empty()







#--------------------------POSITION--------------------------------------------
st.sidebar.markdown('### Position')
st.sidebar.markdown('Represents the current location of the C-Bot, home and the boat')
if st.sidebar.checkbox('Open Console',False,key=1):


    st.subheader('Location')
    st.markdown('Represents the current location of the C-Bot, home and the boat. Upload the text file containing locations of the places to be represented. The locations should be in LatLong.')
    newline(1)

    get_home = get_home_pos()
    get_boat = get_boat_pos()
    get_cbot = get_cbot_pos()

    #latitude, longitude
    HOME_POSITION = [float(get_home[1]),float(get_home[2])]   
    BOAT_POSITION = [float(get_boat[1]),float(get_boat[2])]
    CBOT_POSITION = [float(get_cbot[1]),float(get_cbot[2])]

    DATA_INDEX = pd.DataFrame(data_frame([HOME_POSITION,BOAT_POSITION,CBOT_POSITION]),index=['Latitude','Longitude','Marker'])


    if st.checkbox('Open Offline Map',key='offline_map'):

        if st.checkbox('Read Instructions',False,key='inst'):
            st.markdown('__1.__ Enter the file which contains the coordinates of the __top left__ and __bottom right__ points of the image to be used.')
            st.markdown('__2.__ Make sure to delete any last images which might have been used as it might cause problems.')
        newline(1)
        

        REFLOC = st.file_uploader('Enter a reference location file [.TXT]',type='txt',key='refloc')
        if REFLOC is not None:
            data = cleanFile(REFLOC)

        newline(1)

        if st.button('Clear Buffer image'):
            try:
                os.system('del UPLOAD/buffer.png')
                uploaded_file = None
                st.success('You are good to go')
            except:
                st.warning('No image currently in use')
        st.markdown('Not clearing buffer image before proceeding will show the previously used image')

        newline(1)


        UPLOADED_FILE = st.file_uploader("Choose an image file [.PNG]", type="png", key='map')
        if UPLOADED_FILE is not None:

            fig, scale_x, scale_y = getOfflineMap(UPLOADED_FILE, data, HOME_POSITION, BOAT_POSITION, CBOT_POSITION)
            st.pyplot(fig)

            st.markdown('__X-Axis__ : _1 unit = %f m_ &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp&nbsp __Y-Axis__ : _1 unit = %f m_'%((1/scale_x),(1/scale_y)))
            newline(1)

            st.subheader('Coordinates and markers')
            st.markdown('The coordinates are given below are in LatLong but have been converted to UTM for dispalying on map.')
            st.dataframe(DATA_INDEX)


    
    if st.checkbox('Open online Map',key='online_map'):
        st.markdown('The dashboard will display the map of the last location file entered unless a new one is uploaded.')
            

        my_map = getOnlineMap(HOME_POSITION,BOAT_POSITION,CBOT_POSITION)
        st.pydeck_chart(my_map)
        st.subheader('Coordinates and markers')
        st.markdown('The coordinates are given below are in LatLong.')
        st.dataframe(DATA_INDEX)
            


#--------------------------MISSION CONTROL--------------------------------------------
st.sidebar.markdown('### Mission Control')
st.sidebar.markdown('Upload mission files and send it to mission control to execute/abort it.')

if st.sidebar.checkbox('Open Dashboard',False,key=2):

    st.subheader('Upload mission file')
    st.markdown('Upload a mission file here. The current files in the database along with their time-stamp and status are shown below. Hover over the top right corner of the table to view it completely.')

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






#--------------------------CAMERA--------------------------------------------
st.sidebar.markdown('### Camera Feed')
st.sidebar.markdown('Get the live camera feed from the bot')

if st.sidebar.checkbox('Open Dashboard', False,key=3):

    st.subheader('Live Camera Feed')
    st.markdown('Send request to C-Bot to access its live stream and get current location')

    if st.checkbox('Read Instructions',False,key='cam_inst'):
        st.markdown('__1__. Make sure that the browser and the bot are over the same network.')
        st.markdown("__2__. Ensure that the 'IP WebCam' application has been installed on the bot.")
        st.markdown('__3__. In a new tab enter the network URL (eg, 192.168.43.163:8080) and in the window select `Video Render` option as `Javascript`')
        st.markdown('__4__.Enter the same network url (without http://) in the box below and press enter.')
        st.markdown("__5__.A stream window will start in a new window. Press 'q' to exit")
        newline(1)

    URL = st.text_input('Enter the url of the network stream : ')
    try:
        if URL != '':
            streamVideo(URL)
    except:
        cmd_status.warning('Unable to reach the streaming network')



st.sidebar.markdown('### Stop Functions')
st.sidebar.markdown('Do this if dashboard hangs')
if st.sidebar.checkbox('Kill all processes'):
    st.stop()

schedule.every(1).seconds.do(get_time)
schedule.every(1).seconds.do(get_date)


while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)