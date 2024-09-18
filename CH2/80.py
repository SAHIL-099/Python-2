# You are given a dataset that contains the unemployment rate of different US states for the year 2021. You have to create a 
# choropleth map of the US using the unemployment rate data.
# csv file: https://raw.githubusercontent.com/Jovita7/Data-Analysis-and-Visualization/main/US_Unemployment_

import folium
import pandas as pd
usa_state = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(
geo_data = 'us-states.json', #json
name ='choropleth',
data = pd.read_csv("US_Unemployment_Oct2012.csv"),
columns = ['State', 'Unemployment'], #columns to work on
key_on ='feature.id',
fill_color ='YlGnBu', #I passed colors Yellow,Green,Blue
fill_opacity = 0.7,
line_opacity = 0.2,
legend_name = "Unemployment scale"
).add_to(usa_state)
usa_state