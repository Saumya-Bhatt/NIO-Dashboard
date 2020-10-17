import streamlit as st
import mysql.connector
import datetime
import time
import csv
import os

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