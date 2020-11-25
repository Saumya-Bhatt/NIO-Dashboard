from frame import sql_query


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
        query = "SELECT * from auvinstances"
        return sql_query(address=self.address, database=self.database, query=query, returnVal=True)


    def destroy_all_instances(self):
        query = 'DELETE FROM auvinstances'
        sql_query(address=self.address, database=self.database, query=query)
        return None