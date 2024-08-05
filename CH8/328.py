# Using Open Weather Map API, generate current air pollution data for
# Ahmedabad and extract detail of aqi.


import requests,json

api=input("enter api key:")
city="ahmedabad"

req_url="http://api.openweathermap.org/geo/1.0/direct?q="+city+"&appid="+api

response=requests.get(req_url)
data=response.json()
lat=data[0]['lat']
lon=data[0]['lon']

req="http://api.openweathermap.org/data/2.5/air_pollution?lat="+str(lat)+"&lon="+str(lon)+"&appid="+api

test=requests.get(req)
air=test.json()
aqi=air['list'][0]['main']['aqi']
print(air)
print("air quality index is :"+aqi)
