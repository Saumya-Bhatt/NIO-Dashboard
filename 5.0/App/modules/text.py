import streamlit as st





class StatusCodes():

    def __init__(self, element):
        self.element = element

    error_codes = [
        'Please give a name to the AUV bot instance',
        'Please give a reference ID to the AUV bot instance', 
        'Please enter an AUV reference ID to delete',
        'Reference ID of AUV Instance not specified',
        'The entered AUV Reference ID Instance already exists',
        'No such Instance with the given ID exists',
        'Please load a mission file!',
        'The entered Mission File ID does not exist. Please enter a valid ID',
        'Please check the network URL is correct or that you have followed the steps properly.',
        'Received NaN for coordinates. Check database entry.'
    ]

    success_codes = [
        'AUV bot instance created!',
        'The given AUV instance was deleted!',
        'Session instance running!',
        'File compiled and uploaded successufully',
        'Specified Mission File is Running',
        'Live video stream is running on new window',
    ]

    warning_codes = [
        'All session tokens destroyed',
        'Current session token was destroyed',
        '__NOTE__ : This will destroy all the generated and the current instances within the database. This will delete all the data related to those instances. Are you sure you want to proceed?',
        'The file was removed from the server',
        'Specified Mission File was aborted'  
    ]

    info_codes = [
        'There is no session currently in use',
        'All global instances and sessions were deleted'
    ] 

    def set_code(self,type,code):
        if type == 'error':
            return self.element.error(self.error_codes[code])
        elif type == 'success':
            return self.element.success(self.success_codes[code])
        elif type == 'warning':
            return self.element.warning(self.warning_codes[code])
        else:
            return self.element.info(self.info_codes[code])  





class MethodIntro():

    def mission_file_upload(self):
        st.markdown('Upload your mission files to the server via this panel and moniter their status. Given below is a list of all the mission files currently available on server.')

    def onboard_camera(self):
        st.markdown('''
        This feature uses a 3rd-party application to run. Follow the steps given below : \n
        1. Ensure that the GUI and the AUV are on same network.
        2. Open application 'IP Webcam' and enter the IPv4 network URL into below field.
        ''')

    def realtime_mapping(self):
        st.markdown('Real-time updated mapping functionality with offline and online accessability. Coordinates given in lat-long in the table.')


    def kill_process(self):
        st.markdown('''
        All functions connecting to the server side has been paused. If the dashboard is malfunctioning, press `ctrl + shft + r` to restart the browser. If any problems still persist, try shutting down the serve and start again from the command prompt.
        \n
        1. Functionalities which involve connecting to the server side has been paused.
        2. You can open the consoles but the data displaying there will not be dynamically updated. 
        3. Last called data would be displayed.
        \n
        Toggel the kill process checkbox in the sidebar to restart the processes.
        ''')