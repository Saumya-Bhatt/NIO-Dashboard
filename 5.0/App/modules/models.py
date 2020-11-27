from modules.frame import sql_query
from functions.MissionCompiler import readMission

import datetime
import json
import os



class SessionManager():
    live = False

    def __init__(self, database):
        self.database = database
    
    def get_last_row(self):
        query = 'SELECT * FROM gui_sessions ORDER BY ID DESC LIMIT 1'
        return sql_query(database=self.database, query=query, sqlite=True, returnVal=True)

    def session_status(self):
        self.live = False
        row = self.get_last_row()
        try:
            if row[0][2] == 1 : self.live = True
            return self.live
        except:
            return self.live

    def create_session(self,instanceID):
        query = 'INSERT INTO gui_sessions VALUES (?,?,?)'
        arg = (None,instanceID,1)
        sql_query(database=self.database, query=query, arg=arg, sqlite=True)
        return None

    def delete_session(self):
        try:
            row = self.get_last_row()
            query_update = 'UPDATE gui_sessions SET status = 0 WHERE id = '+str(row[0][0])
            sql_query(database=self.database, query=query_update, sqlite=True)
        except:
            pass
        return None

    def destroy_all_sessions(self):
        query = 'DELETE FROM gui_sessions'
        sql_query(database=self.database, query=query, sqlite=True)
        return None



    
class InstanceManager():

    def __init__(self, address, database):
        self.address = address
        self.database = database

    def duplicate_row(self,id, auv_id=False):
        if auv_id:
            query = 'SELECT * FROM auvinstances WHERE AUV_Key = ' + str(id)
        else:   
            query = 'SELECT * FROM auvinstances WHERE ID = ' + str(id)
        try:
            row = sql_query(address=self.address, database=self.database, query=query, returnVal=True)
            if len(row) > 0:
                return True
        except:
            return False
        return False

    def generate_instance(self, name, key):
        if self.duplicate_row(key, auv_id=True):
            return False
        query = 'INSERT INTO auvinstances VALUES (%s,%s,%s)'
        arg = [None,name,key]
        sql_query(address=self.address, database=self.database, query=query, arg=arg)
        return True

    def delete_instance(self,id):
        if self.duplicate_row(id):
            query = 'DELETE FROM auvinstances WHERE ID=%s'
            sql_query(address=self.address, database=self.database, query=query, arg=(id,))
            return True
        return False

    def get_instance(self,ID):
        query = "SELECT * FROM auvinstances WHERE ID=" + str(ID)
        return sql_query(address=self.address, database=self.database, query=query, returnVal=True)

    def get_all_instances(self):
        query = "SELECT * FROM auvinstances"
        return sql_query(address=self.address, database=self.database, query=query, returnVal=True)


    def destroy_all_instances(self):
        query = 'DELETE FROM auvinstances'
        sql_query(address=self.address, database=self.database, query=query)
        return None




class MissionUpload():

    def __init__(self, sessionID, instance):
        self.sessionID = sessionID
        self.database = instance.database
        self.address = instance.address
        self.missionID = None

    def get_missions(self):
        query = 'SELECT * FROM missionfile WHERE Instance_missionFile_ID=' + str(self.sessionID)
        return sql_query(address=self.address, database=self.database, query=query, returnVal=True)


    def get_status(self,status=None):
        if status is None:
            return '_None_'
        elif status == 'run':
            return '▶️ _RUNNING_'
        elif status == 'abort':
            return '🆎 _ABORTED_'
        elif status == 'upload':
            return '🌐 _UPLOADED_'
        elif status == 'remove':
            return '🔴 _REMOVED_'


    def compile(self,file):
        data = file.read()
        with open('Mission.txt','w+') as f:
            f.write(data.decode('utf-8'))
        compiledMission = json.dumps(readMission(filename='Mission.txt'))
        os.remove('Mission.txt')
        return compiledMission

    def mission_present(self,ID):
        try:
            query = 'SELECT * FROM missionFile WHERE Instance_missionFile_ID = %s AND ID = %s'
            args = [self.missionID, ID]
            rows = sql_query(address=self.address, database=self.database, query=query, arg=args, returnVal=True)
            return True
        except:
            return False


    def upload(self,file):
        query = 'INSERT INTO missionfile VALUES (%s, %s, %s, %s, %s)'
        args = [None, file, str(datetime.datetime.now()), 'UPLOADED', self.sessionID]
        sql_query(address=self.address, database=self.database, query=query, arg=args)


    def abort(self, missionID):
        if self.mission_present(missionID):
            query = 'UPDATE missionfile SET Mission_Status = %s WHERE Instance_missionFile_ID = %s AND ID = %s'
            arg = ['ABORTED', self.sessionID, missionID]
            sql_query(address=self.address, database=self.database, query=query, arg=arg)
            return True
        return False


    def run(self, missionID):
        if self.mission_present(missionID):
            query = 'UPDATE missionfile SET Mission_Status = %s WHERE Instance_missionFile_ID = %s AND ID = %s'
            arg = ['RUNNING', self.sessionID, missionID]
            sql_query(address=self.address, database=self.database, query=query, arg=arg)
            return True
        return False


    def remove(self, missionID):
        if self.mission_present(missionID):
            query = 'DELETE FROM missionfile WHERE Instance_missionFile_ID = %s AND ID = %s'
            arg = [self.sessionID, missionID]
            sql_query(address=self.address, database=self.database, query=query, arg=arg)
            return True
        return False