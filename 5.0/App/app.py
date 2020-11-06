import streamlit as st
#st.set_page_config(layout="wide")

st.title('CSIR - National Institute of Oceanography')
st.subheader('Marine AUV Dashboard')

st.sidebar.header('Hello world!')


def my_widget(key):
    col1, col2 = st.beta_columns(2)
    col1.markdown('Upload file')
    col2.file_uploader('Upload file',key=key)

# And within an expander
my_expander = st.beta_expander("Open Offline Map", expanded=False)
with my_expander:
    clicked = my_widget("offline")

my_expander = st.beta_expander("Open Online Map", expanded=False)
with my_expander:
    clicked = my_widget("online")
