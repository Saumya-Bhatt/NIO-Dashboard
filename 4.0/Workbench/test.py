import streamlit as st
import os
import utm
import csv

import matplotlib.pyplot as plt
from image_cv import image_browser

def cleanFile(file):
    data = file.readlines()
    reader = csv.reader(data)
    temp = []
    for row in reader:
        temp.append(row)
    return temp

a = st.text_input('Enter input:')
u = 'https://'+a
st.text(u)


st.markdown('__1__. Choose an image file from below')
st.markdown('__2__. Select two points from the image, one should be the top left corner and another the bottom right corner of the map that you want.')
st.markdown('__3__. Enter the coordinates of those two points')
st.markdown('__4__. The map is now initialized.')
st.markdown('__5__. Delete the image after use.')

REFLOC = st.file_uploader('Enter a reference location file',type='txt',key='456')
if REFLOC is not None:
    data = cleanFile(REFLOC)

UPLOADED_FILE = st.file_uploader("Choose an image file", type="png", key='123')
image_holder = st.empty()
pixel_holder1 = st.empty()
pixel_holder2 = st.empty()


if UPLOADED_FILE is not None:
    #os.system('cmd /c "python image_cv.py"')


    BASEWIDTH = 1500
    IMG_BUFFER = Image.open(UPLOADED_FILE)
    WPERCENT = (BASEWIDTH/float(IMG_BUFFER.size[0]))
    H_SIZE = int((float(IMG_BUFFER.size[1])*float(WPERCENT)))
    IMG_BUFFER = IMG_BUFFER.resize((BASEWIDTH,H_SIZE), Image.ANTIALIAS)
    IMG_BUFFER = IMG_BUFFER.convert('L')
    
    IMG_BUFFER.save('buffer.png')
    FILE_PATH = 'buffer.png'

    GRID_MAP = image_browser(FILE_PATH)
    image = Image.open('crop.png')
    image_holder.image(image)

    pixel_holder1.markdown('The image size is %d x %d'%(GRID_MAP[1][0]-GRID_MAP[0][0], GRID_MAP[1][1]-GRID_MAP[0][1]))

    loc1 = utm.from_latlon(float(data[0][0]),float(data[0][1]))
    loc2 = utm.from_latlon(float(data[1][0]),float(data[1][1]))

    map_plot = plt.imread('crop.png')
    bounding_box = (loc1[0]%10000,loc2[0]%10000,loc1[1]%10000,loc2[1]%10000)

    loc3 = utm.from_latlon(15.456319, 73.801897)

    latitude = [loc3[0]%10000]
    longitude = [(loc2[1]-loc3[1])%10000-40]

    fig, ax = plt.subplots(figsize=(20,20))
    ax.scatter(latitude,longitude,color='red',s=200)

    ax.imshow(map_plot,extent=bounding_box)

    st.pyplot()


if st.button('Delete recent image'):

    os.system('del crop.png')
    os.system('del buffer.png')
    uploaded_file = None

    image_holder.markdown('No image selected')
    pixel_holder1.markdown("[-,-]")