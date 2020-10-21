import streamlit as st
import schedule
import datetime
import time

st.title('This is some function')
if st.checkbox('Stop this function'):
    st.stop()

if st.checkbox('Click me'):
    st.subheader('YAY!')
    
dt = st.empty()
def get_time():
    return dt.markdown(datetime.datetime.now())

schedule.every(3).seconds.do(get_time)

while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)