import streamlit as st
import time
import datetime

dt = st.empty()

if st.checkbox('Start Time'):
    if st.checkbox('click me!'):
        st.markdown('YAY!')
    while True:
        dt.markdown(datetime.datetime.now())
        time.sleep(1)
else:
    print(0)

if st.checkbox('Start Header'):
    while True:
        st.header('__Hello World__')
        time.sleep(3)
else:
    print(1)

st.balloons()