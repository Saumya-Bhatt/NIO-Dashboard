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
        'No such Instance with the given ID exists'  
    ]

    success_codes = [
        'AUV bot instance created!',
        'The given AUV instance was deleted!',
        'Session instance running!'
    ]

    warning_codes = [
        'All session tokens destroyed',
        'Current session token was destroyed',
        '__NOTE__ : This will destroy all the generated and the current instances within the database. This will delete all the data related to those instances. Are you sure you want to proceed?'  
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