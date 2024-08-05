# Using Open Weather Map API, generate current air pollution data for Delhi and extract detail of “nh3” 
# lat=23.05
# lon=14.05 
# API call request: http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}
# Example of the API response: 
# {
#  "coord":[
#  50,
#  50
#  ],
#  "list":[
#  {
#  "dt":1605182400,
#  "main":{
#  "aqi":500
#  },
#  "components":{
#  "co":201.94053649902344,
#  "no":0.01877197064459324,
#  "no2":0.7711350917816162,
#  "o3":68.66455078125,
#  "so2":0.6407499313354492,
#  "pm2_5":0.5,
#  "pm10":0.540438711643219,
#  "nh3":0.12369127571582794
#  }
#  }
# }