import json
import pandas as pd
import pydeck as pdk

def getOnlineMap(hpos,bpos,cpos):

    #location_file = json.loads(open('location.json').read())
    h_data = {'latitude':[hpos[0]], 'longitude':[hpos[1]]}
    b_data = {'latitude':[bpos[0]], 'longitude':[bpos[1]]}
    c_data = {'latitude':[cpos[0]], 'longitude':[cpos[1]]}

    location_file = {'home':hpos, 'boat':bpos, 'c-bot':cpos}


    home = pd.DataFrame.from_dict(h_data)
    boat = pd.DataFrame.from_dict(b_data)
    c_bot = pd.DataFrame.from_dict(c_data)

    lat_sum = 0
    for i in ['home','boat','c-bot']:
        lat_sum += location_file[i][0]
    midlat = float(lat_sum/3)
    long_sum = 0
    for i in ['home','boat','c-bot']:
        long_sum += location_file[i][1]
    midlong = float(long_sum/3)


    online_map = pdk.Deck(
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
                        get_position='[longitude, latitude]',
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
                        get_position='[longitude, latitude]',
                        get_color='[0, 0, 255, 160]',
                        get_radius=20,
                    ),
                    pdk.Layer(
                        'ScatterplotLayer',
                        data=c_bot,
                        get_position='[longitude, latitude]',
                        get_color='[200, 0, 0, 160]',
                        get_radius=20,
                    ),
                ],
            )
    return online_map