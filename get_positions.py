import pandas as pd
import requests
import folium
from folium import IFrame
import backend



#All Available fields that get returned from the API call                           
columns = ['callsign', 'course',  'dest',
                                'draft', 'eta', 'imo', 'lat', 'length',
                                'lon', 'mmsi', 'name', 'speed',
                                'status', 'time', 'truehead', 'type',
                                'width']



mmsi_list = backend.get_mmsi()



url = "http://www.findship.co/v2_web/ship/ship.php?mmsi="
df = pd.DataFrame({},columns=columns)

for i in mmsi_list:
    r = requests.get(url+i)
    positions = r.json()['shore']
    #print (positions)
    df = df.append(positions,ignore_index=True)
#print (df.loc[:, ['name', 'lat', 'lon', 'dest','eta','speed','time']])

lat = list(df["lat"])
lon = list(df["lon"])
vsl= list(df['name'])
des= list(df['dest'])
eta = list(df['eta'])
spd = list(df['speed'])



fgv = folium.FeatureGroup(name="Port Positions")
map = folium.Map(location=[15.01, -23.953439], zoom_start=2, tiles = "Mapbox Bright")
for lt, ln, vl, dt, et, sp in zip(lat,lon,vsl, des, eta, spd):
    html="""
    <h2> {}</h2>
    Destination: {}<br>
    ETA: {}<br>
    Speed: {}
    """
    html = html.format(str(vl),\
               str(dt),\
               str(et),
               str(sp))
    iframe = IFrame(html=html, width=250, height=125)
    popup = folium.Popup(iframe, max_width=2650)
    folium.Marker(location=[lt,ln],popup=popup).add_to(map)

map.save("fleet_list.html")