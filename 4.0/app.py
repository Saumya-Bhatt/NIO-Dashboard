import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
import sys
import os
import cv2
import utm

from PIL import Image
from imageMap import image_browser
from cam import streamVideo
from fileSQL import *
from onlineMap import *
from frame import *


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)


#--------------------------VIDEO--------------------------------------------
#video_file = open('video.mp4','rb')
#video_bytes = video_file.read()



#--------------------------HEADING--------------------------------------------
st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine robot dashboard')

newline(2)

st.sidebar.markdown('__Battery Status__ : %d %%'%battery)
battery = st.sidebar.progress(battery)

cmd_status = st.sidebar.empty()

st.markdown('__Date__  :   %s/%s/%s'%(dt.day,dt.month,dt.year))
st.markdown('__Time__   :   %s:%s:%s'%(dt.hour,dt.minute,dt.second))





#--------------------------POSITION--------------------------------------------
st.sidebar.markdown('### Position')
st.sidebar.markdown('Represents the current location of the C-Bot, home and the boat')
if st.sidebar.checkbox('Open Console',False,key=1):


    st.subheader('Location')
    st.markdown('Represents the current location of the C-Bot, home and the boat. Online maps provide more interactvity while offline map loads faster. Below are the steps inorder to use offline map. Scroll to bottom to access online map.')

    newline(1)

    if st.checkbox('Read Instructions',False,key='inst'):
        st.markdown('__NOTE__: if the image window opens again, just click on the points which were selected before. If problem persists, do a hard refresh.')
        newline(1)
        st.markdown('__1.__ Upload the text file containing locations of the places to be represented. The locations should be in LatLong.')
        st.markdown('__2.__ Enter the file which contains the coordinates of the __top left__ and __bottom right__ points of the image to be used. The preceeding box shall be used as the image for map.')
        st.markdown('__3.__ Make sure to delete any last images which might have been used as it might cause problems.')
        st.markdown('__4.__ A new window will open showing the image. Click on the points whose coordinates have been inputed in the above uploaded file. Do not click on more points. Press "0" to escape the window')

    newline(1)

    LOC_FILE = st.file_uploader('Enter locations file here [.TXT]',type='txt',key='location')
    if LOC_FILE is not None:
        loc_data = cleanFile(LOC_FILE)    
    

    REFLOC = st.file_uploader('Enter a reference location file [.TXT]',type='txt',key='refloc')
    if REFLOC is not None:
        data = cleanFile(REFLOC)


    if st.button('Delete recent image'):

        try:
            os.system('del crop.png')
            os.system('del buffer.png')
            uploaded_file = None

            st.markdown('You are good to go')
        except:
            st.markdown('No image currently in use')


    UPLOADED_FILE = st.file_uploader("Choose an image file [.PNG]", type="png", key='map')


    if UPLOADED_FILE is not None:

        BASEWIDTH = 1500
        IMG_BUFFER = Image.open(UPLOADED_FILE)
        WPERCENT = (BASEWIDTH/float(IMG_BUFFER.size[0]))
        H_SIZE = int((float(IMG_BUFFER.size[1])*float(WPERCENT)))
        IMG_BUFFER = IMG_BUFFER.resize((BASEWIDTH,H_SIZE), Image.ANTIALIAS)
        #IMG_BUFFER = IMG_BUFFER.convert('L')
        
        IMG_BUFFER.save('buffer.png')
        FILE_PATH = 'buffer.png'

        GRID_MAP = image_browser(FILE_PATH)
        image = Image.open('crop.png')
        #image_holder.image(image)

        st.markdown('The selected image size is %dp x %dp'%(GRID_MAP[1][0]-GRID_MAP[0][0], GRID_MAP[1][1]-GRID_MAP[0][1]))

        loc1 = utm.from_latlon(float(data[0][0]),float(data[0][1]))
        loc2 = utm.from_latlon(float(data[1][0]),float(data[1][1]))

        map_plot = plt.imread('crop.png')
        bounding_box = (loc1[0]%10000,loc2[0]%10000,loc1[1]%10000,loc2[1]%10000)

        home = utm.from_latlon(float(loc_data[0][0]),float(loc_data[0][1]))
        boat = utm.from_latlon(float(loc_data[1][0]),float(loc_data[1][1]))
        cbot = utm.from_latlon(float(loc_data[2][0]),float(loc_data[2][1]))

        #loc3 = utm.from_latlon(15.456319, 73.801897)

        latitude = [home[0]%10000,boat[0]%10000,cbot[0]%10000]
        longitude = [(loc2[1]-home[1])%10000-90,(loc2[1]-boat[1])%10000-90,(loc2[1]-cbot[1])%10000-90]

        fig, ax = plt.subplots(figsize=(20,15))
        ax.scatter(latitude[0],longitude[0],color='green',s=400)
        ax.scatter(latitude[1],longitude[1],color='blue',s=400)
        ax.scatter(latitude[2],longitude[2],color='red',s=400)

        ax.imshow(map_plot,extent=bounding_box)
        st.pyplot()
        st.markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _x-axis : Latitude in UTM &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; y-axis : Longitude in UTM_')

        data_frame = {
            'HOME' : [float(loc_data[0][0]),float(loc_data[0][1]),'🟢'],
            'BOAT' : [float(loc_data[1][0]),float(loc_data[1][1]),'🔵'],
            'C-BOT' : [float(loc_data[2][0]),float(loc_data[2][1]),'🔴']
        }

        st.subheader('Coordinates and markers')
        st.markdown('The coordinates are given below are in LatLong but have been converted to UTM for dispalying on map.')
        st.dataframe(data_frame)

    newline(1)
    
    if st.button('Online Map',key='online'):
        st.pydeck_chart(online_map)






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
        st.markdown('__2__. In a new tab enter the network URL (eg, 192.168.43.163:8080) and in the window select `Video Render` option as `Javascript`')
        st.markdown('__3__.Enter the same network url (without http://) in the box below and press enter.')
        st.markdown("__4__.A stream window will start in a new window. Press 'q' to exit")
        newline(1)

    URL = st.text_input('Enter the url of the network stream : ')
    try:
        if URL != '':
            streamVideo(URL)
    except:
        cmd_status.warning('Unable to reach the streaming network')