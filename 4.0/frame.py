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

battery = 78
dt = datetime.datetime.now()