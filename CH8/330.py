# Using the Open Weather Map API, find the location of ahmedabad

import requests

api=input("enter api key:")
city="ahmedabad"

req_url="http://api.openweathermap.org/geo/1.0/direct?q="+city+"&appid="+api

response=requests.get(req_url)
data=response.json()
lat=data[0]['lat']
lon=data[0]['lon']

print("ahemedabad location is  lat :"+str(lat)+"\nlon:"+str(lon))