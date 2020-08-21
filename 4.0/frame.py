import streamlit as st
import datetime
import csv

def newline(n):
    for i in range(n):
        st.markdown('\n')

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

battery = 78
dt = datetime.datetime.now()