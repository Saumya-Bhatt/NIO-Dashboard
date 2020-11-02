import mysql.connector
import datetime
import time
import csv
import os

from PIL import Image


def cleanFile(file):
    data = file.readlines()
    reader = csv.reader(data)
    temp = [row for row in reader]
    return temp

def data_frame(data):
    frame = {
    'HOME' : [float(data[0][0]),float(data[0][1]),'🟢'],
    'BOAT' : [float(data[1][0]),float(data[1][1]),'🔵'],
    'C-BOT' : [float(data[2][0]),float(data[2][1]),'🔴']
    }
    return frame

def create_file(file_data):
    fname = 'MISSION_FILE__' + str(datetime.datetime.now())+'.txt'
    upload_dir = os.getcwd() + '\\UPLOAD'
    os.chdir(upload_dir)
    with open(fname,'w+') as f:
        f.write(file_data.getvalue())
    os.chdir('..')
    return None

def saveImage(UPLOADED_FILE):
    BASEWIDTH = 1500
    IMG_BUFFER = Image.open(UPLOADED_FILE)
    WPERCENT = (BASEWIDTH/float(IMG_BUFFER.size[0]))
    H_SIZE = int((float(IMG_BUFFER.size[1])*float(WPERCENT)))
    IMG_BUFFER = IMG_BUFFER.resize((BASEWIDTH,H_SIZE), Image.ANTIALIAS)
    FILE_PATH = 'UPLOAD/buffer.png'
    IMG_BUFFER.save(FILE_PATH)

    image = Image.open(FILE_PATH)
    width,height = image.size
    map_plot = Image.open(FILE_PATH).convert("L")
    return width,height,map_plot

def positionFrame(getHome,getBoat,getCbot,reverse=False):
    if not reverse:
        homePos = [float(getHome[1]),float(getHome[2])]
        boatPos = [float(getBoat[1]),float(getBoat[2])]
        cbotPos = [float(getCbot[1]),float(getCbot[2])]
        return [homePos,boatPos,cbotPos]
    else:
        homePos = [float(getHome[2]),float(getHome[1])]
        boatPos = [float(getBoat[2]),float(getBoat[1])]
        cbotPos = [float(getCbot[2]),float(getCbot[1])]
        return [homePos,boatPos,cbotPos]

def sql_queries_static(query,param1=None,param2=None):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='nio_python'
    )
    mycursor = mydb.cursor()
    if param1 is None and param2 is None:
        mycursor.execute(query)
    else:
        mycursor.execute(query%(param1,param2))
    mydb.commit()
    mydb.close()
    mycursor.close()

def sql_queries_dynamic(query,param1=None,param2=None):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='nio_python'
    )
    mycursor = mydb.cursor()
    if param1 is None and param2 is None:
        mycursor.execute(query)
    else:
        mycursor.execute(query%(param1,param2))
    req_data = mycursor.fetchall()
    mydb.close()
    mycursor.close()
    return req_data