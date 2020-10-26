import streamlit as st
import mysql.connector
import datetime
import time
import csv
import os

from PIL import Image

def newline(n):
    i =0
    while i<=n:
        st.markdown('\n')
        i+=1

def cleanFile(file):
    data = file.readlines()
    reader = csv.reader(data)
    temp = []
    for row in reader:
        temp.append(row)
    return temp

def data_frame(data):
    frame = {
    'HOME' : [float(data[0][0]),float(data[0][1]),'🟢'],
    'BOAT' : [float(data[1][0]),float(data[1][1]),'🔵'],
    'C-BOT' : [float(data[2][0]),float(data[2][1]),'🔴']
    }
    return frame

def create_file(file_data):
    fname = 'MISSION_FILE__' + str(datetime.datetime.now())+'.txt'
    upload_dir = os.getcwd() + '\\UPLOAD'
    os.chdir(upload_dir)
    with open(fname,'w+') as f:
        f.write(file_data.getvalue())
    os.chdir('..')
    return None

def saveImage(UPLOADED_FILE):
    BASEWIDTH = 1500
    IMG_BUFFER = Image.open(UPLOADED_FILE)
    WPERCENT = (BASEWIDTH/float(IMG_BUFFER.size[0]))
    H_SIZE = int((float(IMG_BUFFER.size[1])*float(WPERCENT)))
    IMG_BUFFER = IMG_BUFFER.resize((BASEWIDTH,H_SIZE), Image.ANTIALIAS)
    FILE_PATH = 'UPLOAD/buffer.png'
    IMG_BUFFER.save(FILE_PATH)

    image = Image.open(FILE_PATH)
    width,height = image.size
    map_plot = Image.open(FILE_PATH).convert("L")
    return width,height,map_plot


kill_process = '''
        All functions connecting to the server side has been paused. If the dashboard is malfunctioning, press `ctrl + shft + r` to restart the browser. If any problems still persist, try shutting down the serve and start again.
        \n
        1. Functionalities which involve connecting to the server side has been paused.
        2. You can open the consoles but the data displaying there will not be dynamically updated. Last called data would be displayed.
        3. Communication from the dashboard to the server is allowed but reverse is not true here.
        \n
        Opening any of the consoles will restart the processes.
        '''

camera_instr = '''
        \n
        __1__. Make sure that the browser and the bot are over the same network. \n
        __2__. Ensure that the 'IP WebCam' application has been installed on the bot.\n
        __3__. In a new tab enter the network URL (eg, 192.168.43.163:8080) and in the window select `Video Render` option as `Javascript`\n
        __4__.Enter the same network url (without http://) in the box below and press enter.
        __5__.A stream window will start in a new window. Press 'q' to exit
        \n
        '''

offline_map_instr = '''
        \n
        __1.__ Enter the file which contains the coordinates of the __top left__ and __bottom right__ points of the image to be used.\n
        __2.__ Make sure to delete any last images which might have been used as it might cause problems.
        \n
        '''