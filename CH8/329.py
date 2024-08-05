# Using the Open Weather Map API, generate a 3 Hourly 5 Days weather forecast for Ahmedabad with all details in JSON format.
# Note: Request for all the data via API in metric units
import requests,json

api=input("enter api key:")
city="ahmedabad"

req_url="http://api.openweathermap.org/geo/1.0/direct?q="+city+"&appid="+api

response=requests.get(req_url)
data=response.json()
lat=data[0]['lat']
lon=data[0]['lon']

req="http://api.openweathermap.org/data/2.5/forecast?lat="+str(lat)+"&lon="+str(lon)+"&appid="+api+"&units=metric"

new_data=requests.get(req)
three_five=new_data.json()
print(json.dumps(three_five,indent=5))