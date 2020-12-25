import mysql.connector
import datetime


# NOTE: install python mysql module before running:   pip install mysql-connector

# NOTE: If want to insert into DB, input type:
# value = {
#     'battery'  : xyz,
#     'pitch'    : xyz,
#     'yaw'      : xyz,
#     'depth'    : xyz,
#     'boat_lat' : xyz,
#     'boat_long': xyz,
#     'cbot_lat' : xyz,
#     'cbot_long': xyz,
#     'home_lat' : xyz,
#     'home_long': xyz
# }
# If only want to add to certain tables, keep other entry as None in values.

# NOTE: If want to get all entries from the DB, just run: connect(fetch=True)
#       If want to get latest entries and not all, run: connect(fetch=True, latest=True)

# return type with latest=True:
# {
# 'battery': [(9, '44')],
# 'pitch'  : [(1, '73.8')],
# 'yaw'    : [(2, '56.17')],
# 'depth'  : [()]
# 'boat'   : [(4, '73.797539', '15.456058')],
# 'cbot'   : [(10, '73.801689', '15.458551')],
# 'home'   : [(1, '73.801925', '15.456380')]
# }

# First entry in the list is the ID number so can be ignored


def connect(values=None, fetch=False, latest=False):

    connection = mysql.connector.connect(
            user     = 'root',
            password = '',
            host     = '127.0.0.1',
            database = 'nio_python'
        )
    cursor = connection.cursor()

    if fetch == True:
        records = {}
        query = {
            'battery': 'SELECT * FROM battery_value',
            'pitch'  : 'SELECT * FROM pitch_value',
            'yaw'    : 'SELECT * FROM yaw_value',
            'depth'  : 'SELECT * FROM depth',
            'boat'   : 'SELECT * FROM boat_position',
            'cbot'   : 'SELECT * FROM cbot_position',
            'home'   : 'SELECT * FROM home_position'
        }
           
        for i in query:
            if latest == True:
                add = ' ORDER BY ID DESC LIMIT 1'
                new_query = query[i] + add
                cursor.execute(new_query)
            else:
                cursor.execute(query[i])
            records[i] = cursor.fetchall()
        connection.close()
        return records
    else:
        query = {
            'battery': {
                'q'  : 'INSERT INTO battery_value VALUES (%s,%s)',
                'arg': (None,values['battery'])
            },
            'pitch': {
                'q'  : 'INSERT INTO pitch_value VALUES (%s,%s)',
                'arg': (None,values['pitch'])
            },
            'yaw': {
                'q'  : 'INSERT INTO yaw_value VALUES (%s,%s)',
                'arg': (None,values['yaw'])
            },
            'depth': {
                'q'  : 'INSERT INTO depth VALUES (%s,%s,%s)',
                'arg': (None,values['depth'],str(datetime.datetime.now()))
            },
            'boat': {
                'q'  : 'INSERT INTO boat_position VALUES (%s,%s,%s)',
                'arg': (None, values['boat_lat'], values['boat_long'])
            },
            'cbot': {
                'q'  : 'INSERT INTO home_position VALUES (%s,%s,%s)',
                'arg': (None, values['home_lat'], values['home_long'])
            },
            'home': {
                'q'  : 'INSERT INTO cbot_position VALUES (%s,%s,%s)',
                'arg': (None, values['cbot_lat'], values['cbot_long'])
            }
        }
        for i in query:
            if query[i]['arg'] == (None,None) or query[i]['arg'] == (None,None,None):
                print(f'SKIPPING | NO VALUE GIVEN FOR ARG : {i}')
            else:
                cursor.execute(query[i]['q'],query[i]['arg'])
                connection.commit()
                print(f'COMMITED TO DB | {i} : {values[i]}')
        cursor.close()
        connection.close()
        print('CLOSING CONNECTION')
        return None