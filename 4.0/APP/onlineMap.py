import pandas as pd
import pydeck as pdk

def getOnlineMap(HOME_POSITION,BOAT_POSITION,CBOT_POSITION):
    
    home = pd.DataFrame(data=[HOME_POSITION],columns=['lat','lon'])
    boat = pd.DataFrame(data=[BOAT_POSITION],columns=['lat','lon'])
    cbot = pd.DataFrame(data=[CBOT_POSITION],columns=['lat','lon'])

    midlat = float((HOME_POSITION[0]+BOAT_POSITION[0]+CBOT_POSITION[0])/3)
    midlong = float((HOME_POSITION[1]+BOAT_POSITION[1]+CBOT_POSITION[1])/3)


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
