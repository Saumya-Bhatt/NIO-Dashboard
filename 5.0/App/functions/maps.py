import pandas as pd
import pydeck as pdk


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
