# Using the Open Weather Map API, find the wind_speed of ahmedabad 

import requests,json

api=input("enter api key:")
city="ahmedabad"

req_url="http://api.openweathermap.org/geo/1.0/direct?q="+city+"&appid="+api

response=requests.get(req_url)
data=response.json()
lat=data[0]['lat']
lon=data[0]['lon']

req="https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid="+api+"&units=metric"

new_data=requests.get(req)
data=new_data.json()
print(json.dumps(data,indent=5))
wind_speed=data['wind']['speed']
print("wind speed:",wind_speed)
