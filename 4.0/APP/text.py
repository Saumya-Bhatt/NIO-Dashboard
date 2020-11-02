import streamlit as st

def newline(n):
    for _ in range(n):
        st.markdown('\n')
    return None


class MethodIntro():

    def missionFile(self):
        st.subheader('Upload mission file')
        st.markdown('Upload a mission file here. The current files in the database along with their time-stamp and status are shown below.')
        return None

    def positionConsole(self):
        st.subheader('Position Console')
        st.markdown('Represents the current location of the C-Bot, home and the boat.')
        st.markdown('__Note__: Toggeling between offline and online mode may cause the dashboard to hang up.')
        newline(1)
        return None

    def cameraConsole(self): 
        st.subheader('Live Camera Feed')
        st.markdown('Send request to C-Bot to access its live stream and get current location')
        return None


class Headers():

    def position(self):
        st.sidebar.markdown('### Position')
        st.sidebar.markdown('Represents the current location of the C-Bot, home and the boat')
        return None

    def coordinates(self,offline=True):
        st.subheader('Coordinates and markers')
        if offline:
            st.markdown('The coordinates are given below are in LatLong but have been converted to UTM for dispalying on map.')
            return None
        else:
            st.markdown('The coordinates are given below are in LatLong.')
            return None

    def missionControl(self):
        st.sidebar.markdown('### Mission Control')
        st.sidebar.markdown('Upload mission files and send it to mission control to execute/abort it.')
        return None

    def cameraFeed(Self):
        st.sidebar.markdown('### Camera Feed')
        st.sidebar.markdown('Get the live camera feed from the bot')
        return None


class BigInst():

    def header(self):
        st.title('CSIR - National Institute of Oceanography')
        st.subheader('Marine robot dashboard')
        newline(2)
        return None

    def killProcess(self):
        st.markdown('''
        All functions connecting to the server side has been paused. If the dashboard is malfunctioning, press `ctrl + shft + r` to restart the browser. If any problems still persist, try shutting down the serve and start again.
        \n
        1. Functionalities which involve connecting to the server side has been paused.
        2. You can open the consoles but the data displaying there will not be dynamically updated. Last called data would be displayed.
        3. Communication from the dashboard to the server is allowed but reverse is not true here.
        \n
        Opening any of the consoles will restart the processes.
        ''')
        return None


    def cameraInstr(self):
        st.markdown('''
        \n
        __1__. Make sure that the browser and the bot are over the same network. \n
        __2__. Ensure that the 'IP WebCam' application has been installed on the bot.\n
        __3__. In a new tab enter the network URL (eg, 192.168.43.163:8080) and in the window select `Video Render` option as `Javascript`\n
        __4__.Enter the same network url (without http://) in the box below and press enter.
        __5__.A stream window will start in a new window. Press 'q' to exit
        \n
        ''')
        newline(1)
        return None


    def offlineMapInstr(self):
        st.markdown('''
        \n
        __1.__ Enter the file which contains the coordinates of the __top left__ and __bottom right__ points of the image to be used.\n
        __2.__ Make sure to delete any last images which might have been used as it might cause problems.
        \n
        ''')
        return None