import utm
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def getOfflineMap(UPLOADED_FILE, refloc, HOME_POSITION, BOAT_POSITION, CBOT_POSITION):

    BASEWIDTH = 1500
    IMG_BUFFER = Image.open(UPLOADED_FILE)
    WPERCENT = (BASEWIDTH/float(IMG_BUFFER.size[0]))
    H_SIZE = int((float(IMG_BUFFER.size[1])*float(WPERCENT)))
    IMG_BUFFER = IMG_BUFFER.resize((BASEWIDTH,H_SIZE), Image.ANTIALIAS)

    IMG_BUFFER.save('UPLOAD/buffer.png')
    FILE_PATH = 'UPLOAD/buffer.png'

    image = Image.open(FILE_PATH)
    width,height = image.size
#   st.markdown('The selected image size is %dp x %dp'%(width,height))

    loc1 = utm.from_latlon(float(refloc[0][0]),float(refloc[0][1]))
    loc2 = utm.from_latlon(float(refloc[1][0]),float(refloc[1][1]))


    home = utm.from_latlon(HOME_POSITION[1],HOME_POSITION[0])
    boat = utm.from_latlon(BOAT_POSITION[1],BOAT_POSITION[0])
    cbot = utm.from_latlon(CBOT_POSITION[1],CBOT_POSITION[0])

    width,height = image.size
    scale_x = width/abs(loc1[0]-loc2[0])
    scale_y = height/abs(loc1[1]-loc2[1])

    map_plot = Image.open(FILE_PATH).convert("L")
    arr = np.asarray(map_plot)
    bounding_box = (width,0,height,0)

    latitude = [(loc1[0]-home[0])*scale_x+width,(loc1[0]-boat[0])*scale_x+width,(loc1[0]-cbot[0])*scale_x+width]
    longitude = [(loc2[1]-home[1])*scale_y+height,(loc2[1]-boat[1])*scale_y+height,(loc2[1]-cbot[1])*scale_y+height]

    fig, ax = plt.subplots()
    ax.scatter(latitude[0],longitude[0],color='green',s=20)
    ax.scatter(latitude[1],longitude[1],color='blue',s=20)
    ax.scatter(latitude[2],longitude[2],color='red',s=20)
    ax.imshow(arr,extent=bounding_box,cmap='gray')

    return fig, scale_x, scale_y