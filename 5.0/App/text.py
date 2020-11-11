import streamlit as st


class StatusCodes():

    def __init__(self, element):
        self.element = element

    error_codes = [
        'Please give a name to the AUV bot instance!',
        'Please give a reference ID to the AUV bot instance!', 
        'Please enter an AUV reference ID to delete!',
        'Reference ID of AUV Instance not specified!'  
    ]

    success_codes = [
        'AUV bot instance created!',
        'The given AUV instance was deleted!',
        'Session instance running!'
    ]

    warning_codes = [
        'All session tokens destroyed',
        'Current session token was destroyed'  
    ]

    info_codes = [
        'No instance of the input reference ID is running',
        'There is no session currently in use',
    ] 

    def setCode(self,type,code):
        if type == 'error':
            return self.element.error(self.error_codes[code])
        elif type == 'success':
            return self.element.success(self.success_codes[code])
        elif type == 'warning':
            return self.element.warning(self.warning_codes[code])
        else:
            return self.element.info(self.info_codes[code])  