import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
import sys
import os
import cv2
import utm
import json

from PIL import Image
from cam import streamVideo
from onlineMap import getOnlineMap
from fileSQL import *
from frame import *


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
    st.markdown('Represents the current location of the C-Bot, home and the boat. Upload the text file containing locations of the places to be represented. The locations should be in LatLong.')
    newline(1)

    LOC_FILE = st.file_uploader('Enter locations file here [.TXT]',type='txt',key='location')
    if LOC_FILE is not None:
        loc_data = cleanFile(LOC_FILE)
        DATA_INDEX = pd.DataFrame(data_frame(loc_data),index=['Longitude','Latitude','Marker'])
    newline(1)

    if st.checkbox('Open Offline Map',key='offline_map'):

        if st.checkbox('Read Instructions',False,key='inst'):
            st.markdown('__1.__ Enter the file which contains the coordinates of the __top left__ and __bottom right__ points of the image to be used.')
            st.markdown('__2.__ Make sure to delete any last images which might have been used as it might cause problems.')
        newline(1)
        

        REFLOC = st.file_uploader('Enter a reference location file [.TXT]',type='txt',key='refloc')
        if REFLOC is not None:
            data = cleanFile(REFLOC)


        if st.button('Clear Buffer image'):
            try:
                os.system('del UPLOAD/buffer.png')
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
            
            IMG_BUFFER.save('UPLOAD/buffer.png')
            FILE_PATH = 'UPLOAD/buffer.png'

            image = Image.open(FILE_PATH)
            width,height = image.size
            st.markdown('The selected image size is %dp x %dp'%(width,height))

            loc1 = utm.from_latlon(float(data[0][0]),float(data[0][1]))
            loc2 = utm.from_latlon(float(data[1][0]),float(data[1][1]))

            home = utm.from_latlon(float(loc_data[0][0]),float(loc_data[0][1]))
            boat = utm.from_latlon(float(loc_data[1][0]),float(loc_data[1][1]))
            cbot = utm.from_latlon(float(loc_data[2][0]),float(loc_data[2][1]))

            width,height = image.size
            scale_x = width/abs(loc1[0]-loc2[0])
            scale_y = height/abs(loc1[1]-loc2[1])

            map_plot = Image.open(FILE_PATH).convert("L")
            arr = np.asarray(map_plot)
            bounding_box = (width,0,height,0)

            latitude = [(loc1[0]-home[0])*scale_x+width,(loc1[0]-boat[0])*scale_x+width,(loc1[0]-cbot[0])*scale_x+width]
            longitude = [(loc2[1]-home[1])*scale_y+height,(loc2[1]-boat[1])*scale_y+height,(loc2[1]-cbot[1])*scale_y+height]

            fig, ax = plt.subplots()
            ax.scatter(latitude[0],longitude[0],color='green',s=20)
            ax.scatter(latitude[1],longitude[1],color='blue',s=20)
            ax.scatter(latitude[2],longitude[2],color='red',s=20)
            ax.imshow(arr,extent=bounding_box,cmap='gray')
            st.pyplot(fig)

            st.markdown('__X-Axis__ : _1 unit = %f m_ &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp&nbsp __Y-Axis__ : _1 unit = %f m_'%((1/scale_x),(1/scale_y)))
            newline(1)

            st.subheader('Coordinates and markers')
            st.markdown('The coordinates are given below are in LatLong but have been converted to UTM for dispalying on map.')
            st.dataframe(DATA_INDEX)


    
    if st.checkbox('Open online Map',key='online_map'):
        st.markdown('The dashboard will display the map of the last location file entered unless a new one is uploaded.')
            
        with open('location.json','r') as jsonFile:
            dump = json.load(jsonFile)

        dump['home']['latitude'] = [float(loc_data[0][0])]
        dump['home']['longitude'] = [float(loc_data[0][1])]
        dump['boat']['latitude'] = [float(loc_data[1][0])]
        dump['boat']['longitude'] = [float(loc_data[1][1])]
        dump['c-bot']['latitude'] = [float(loc_data[2][0])]
        dump['c-bot']['longitude'] = [float(loc_data[2][1])]

        with open("location.json", "w") as jsonFile:
            json.dump(dump, jsonFile)


        my_map = getOnlineMap()
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