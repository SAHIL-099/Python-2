# Use the California_Houses.csv file to create a map with the first 200 rows using the latitudes and longitudes given in the file with the 
# following customizations:
#  1. Colour of circle markers should be green with red fill and the type of map should be stamen terrain
#  2. Add pop up labels using the population from the file.
# Take the dataset fom below:
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/California_Houses.csv

import folium as f
import pandas as pd
# Load the data from the CSV file into a pandas DataFrame
df= pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/California_Houses.csv")
df = df.head(200)
m = f.Map(location=[df.latitude.mean(),df.longitude.mean()],zoom_start = 13)
f.TileLayer('stamenterrain').add_to(m)
grp = f.map.FeatureGroup()
for lat,long,population in zip(df.latitude,df.longitude,df.population):
    f.CircleMarker(location=[lat,long],color="green",fill=True,fill_color="red",tooltip=f"Population: {population}").add_to(grp)
grp.add_to(m)
m