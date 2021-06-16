import requests
import json

api = {OpenWeatherMap Token}

city = input("Enter your city: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

# accessing data using requests get() method
ans = requests.get(url)
json_data = json.loads(ans.text)

# whole data returned from the api
# print(json_data)

# checking whether the request is success or not
if json_data['cod'] != 200:
    print(json_data['message'])

else:
    # getting weather data
    w = json_data["weather"][0]["description"]

    # getting temperature
    temp = json_data['main']['temp']

    # Humidity
    hum = json_data['main']['humidity']

    # speed of wind
    swind = json_data['wind']['speed']

    print(f"Weather : {w}",f"Temperature: {temp}", f"Humidity: {hum}", f"Wind speed: {swind}", sep="\n")

