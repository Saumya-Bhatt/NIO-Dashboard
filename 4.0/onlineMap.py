import json
import pandas as pd
import pydeck as pdk


location_file = json.loads(open('Extra\location.json').read())

home = pd.DataFrame.from_dict(location_file['home'])
boat = pd.DataFrame.from_dict(location_file['boat'])
c_bot = pd.DataFrame.from_dict(location_file['c-bot'])

lat_sum = 0
for i in ['home','boat','c-bot']:
    lat_sum += location_file[i]['latitude'][0]
midlat = float(lat_sum/3)
long_sum = 0
for i in ['home','boat','c-bot']:
    long_sum += location_file[i]['longitude'][0]
midlong = float(long_sum/3)


online_map = pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=midlat,
                longitude=midlong,
                zoom=16,
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