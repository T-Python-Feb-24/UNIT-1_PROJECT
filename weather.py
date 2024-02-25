import requests
from api_keys import weather_api_key
from check import checkValidStr
from check import checkValidResponse
from check import checkValidInt
from termcolor import colored

def getWeather():
    while True:
        city_name: str = input("Enter city name :")
        if not checkValidStr(city_name):
            continue

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}"
        if not checkValidResponse(url):
            print("error getting weather data")
            continue

        if checkValidResponse(url):
            response = checkValidResponse(url)
            weather_data = response.json()
            # temperature here would be retrived in Kalvin
            temp = weather_data['main']['temp']
            desc = weather_data['weather'][0]['description']
            # converting the temperature to Celsius
            temp_c = temp - 273.15
            print(f"Today's weather in {city_name} is {desc} ,Temperature is: {round(temp_c)}C")
        
        while True: 
            end_input = input("\nTo Check Weather For Another City, Press 1 \nTo Exit Weather Service, Press 2 :\n")
            option = checkValidInt(end_input, 2)
            if type(option) == int:
                break
            
        if option == 1:
            getWeather()

        elif option == 2:
            print("Thank You For using Our Weather Service!🌦️\n")
            return
        return
