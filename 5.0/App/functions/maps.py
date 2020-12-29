import pandas as pd
import numpy as np
import pydeck as pdk

from PIL import Image
import utm


def online_map(COORDINATES):
    
    home = pd.DataFrame(data=[COORDINATES['HOME'][0], COORDINATES['HOME'][1]])
    boat = pd.DataFrame(data=[COORDINATES['BOAT'][0], COORDINATES['BOAT'][1]])
    cbot = pd.DataFrame(data=[COORDINATES['C-BOT'][0], COORDINATES['C-BOT'][1]])

    midlat = float((COORDINATES['HOME'][0] + COORDINATES['BOAT'][0] + COORDINATES['C-BOT'][0])/3)
    midlong = float((COORDINATES['HOME'][1] + COORDINATES['BOAT'][1] + COORDINATES['C-BOT'][1])/3)


    map_info = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=midlat,
            longitude=midlong,
            zoom=15,
            pitch=50,
        ),
        layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=home,
                    get_position='[lon, lat]',
                    radius=20,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    get_color='[0, 255, 0, 160]',
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=boat,
                    get_position='[lon, lat]',
                    get_color='[0, 0, 255, 160]',
                    get_radius=20,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=cbot,
                    get_position='[lon, lat]',
                    get_color='[200, 0, 0, 160]',
                    get_radius=20,
                ),
            ],
    )

    return map_info



def save_image(IMAGE_FILE):

    BASEWIDTH = 1500
    FILE_PATH = 'buffer.png'

    img_buffer = Image.open(IMAGE_FILE)
    w_percent = (BASEWIDTH/float(img_buffer.size[0]))
    h_size = int((float(img_buffer.size[1])*float(w_percent)))
    IMG_FILE = img_buffer.resize((BASEWIDTH,h_size), Image.ANTIALIAS)
    IMG_FILE.save(FILE_PATH)

    image = Image.open(FILE_PATH)
    width,height = image.size
    map_plot = Image.open(FILE_PATH).convert("L")
    return (width,0,height,0), np.asarray(map_plot)



def clean_file(FILE):
    temp = FILE.read().decode('utf-8').splitlines()
    temp1 = [i.replace(' ','').split(',') for i in temp]
    temp3 = [[float(j) for j in i] for i in temp1]
    loc1 = utm.from_latlon(temp3[0][0],temp3[0][1])
    loc2 = utm.from_latlon(temp3[1][0],temp3[1][1])
    return loc1, loc2



def setup_offline_map(REFLOC_FILE, IMAGE_FILE):

        refloc1, refloc2 = clean_file(REFLOC_FILE)
        bounding_box, map_array = save_image(IMAGE_FILE)
        scale_x = bounding_box[0]/abs(refloc1[0] - refloc2[0])
        scale_y = bounding_box[2]/abs(refloc1[1] - refloc2[1])
        meta_data = [refloc1, refloc2, scale_x, scale_y, bounding_box[0], bounding_box[2]]

        return meta_data, map_array, bounding_box




def generate_coordinates(data, meta_data):
    
    home = utm.from_latlon(data['HOME'][0], data['HOME'][1])
    boat = utm.from_latlon(data['BOAT'][0], data['BOAT'][1])
    cbot = utm.from_latlon(data['C-BOT'][0], data['C-BOT'][1])

    loc1, loc2, scale_x, scale_y, width, height = meta_data

    latitude = [
        (loc1[0]-home[0])*scale_x+width,
        (loc1[0]-boat[0])*scale_x+width,
        (loc1[0]-cbot[0])*scale_x+width
    ]
    longitude = [
        (loc2[1]-home[1])*scale_y+height,
        (loc2[1]-boat[1])*scale_y+height,
        (loc2[1]-cbot[1])*scale_y+height
    ]

    return latitude, longitude