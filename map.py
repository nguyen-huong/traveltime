from folium import plugins
import folium
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from tasks.py import *

#change data path here
data = read_data('data/data.csv')

Lat = list(data["LATITUDE"])
Long = list(data["LONGITUDE"])
speed = list(data["SPEED"])

fg = folium.FeatureGroup(name="Travel Time Map")

#change map center with the avg of the data
map = folium.Map([data.Lat.mean(), data.Long.mean()], zoom_start=12)

#add a marker for each point
for lati, longi, spe in zip(Lat, Long, speed):
    fg.add_child(folium.CircleMarker(location=[lati, longi], radius = 4, popup=str(popup(spe)),
    fill_color=coloring(spe), color = coloring(spe), fill_opacity=0.7))

#display data points on the map and export
map.add_child(fg)
folium.LayerControl().add_to(map)
map.save("map.html")