import folium
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#load data
def read_data(x):
    data = pd.read_csv(x)
    data['LONGITUDE'] = -1 * data['LONGITUDE']
    data.Long = data['LONGITUDE']
    data.Lat = data['LATITUDE']
    return data

#color the points
def coloring(speed):
    #55+ baby blue
    if speed > 55:
        return '#42f5f5'
    #41-55 light blue
    elif speed > 40:
      return '#4edded'
    #21-40 blue
    elif speed > 20:
      return '#428df5'
    #0-20 dark blue
    elif speed > 0:
      return 'blue'

#create a popup
def popup(i):
  for i in range(0,len(data)):
    date = data.iloc[i]["LOCAL DATE"]
    time = data.iloc[i]["LOCAL TIME"]
    return date, time