# Using the Open Weather Map API, generate a 3 hourly 5 days weather forecast for Ahmedabad with details like minimum temperature, 
# maximum temperature, wind speed, humidity, and weather description. Display this data in the form of a Pandas data frame with the column 
# names being date_time, min_temp, max_temp, wind_speed, humidity, and weather_description.
import pandas as  pd
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
five_days=new_data.json()

D={"Date_Time":[],"min_temp":[],"max_temp":[],"wind_speed":[],"humidity":[],"weather_description":[]}
for i in five_days['list']:
    D["Date_Time"].append(i['dt_txt'])
    D["min_temp"].append(i['main']['temp_min'])
    D["max_temp"].append(i['main']['temp_max'])
    D["wind_speed"].append(i['wind']['speed'])
    D["humidity"].append(i['main']['humidity'])
    D["weather_description"].append(i['weather'][0]['description'])
    
    
df=pd.DataFrame(D)
print(df)