from geopy.geocoders import OpenCage
from geopy.distance import geodesic
from datetime import timedelta
from api_keys import distance_api_key
from check import checkValidResponse
from check import checkValidStr
from check import checkValidInt

import pandas as pd

airports_file = "sa-airports.csv"
airports_df = pd.read_csv(airports_file)
stations_file = "sa_stations.csv"
stations_df = pd.read_csv(stations_file)

geolocator = OpenCage(user_agent="SaudiArabiaGuide", api_key=distance_api_key)


def distanceKm(from_city: str, to_city: str):
    global distance
    # geocode is a method inside the OpenCage class , Return a location point by address.
    from_geocode = geolocator.geocode(from_city)
    to_geocode = geolocator.geocode(to_city)
    if (from_geocode is None) or (to_geocode is None):
        print("unable to get locate city")

    # هنا سوي تراي واكسبت اذا ما نجحت عملية الاتصال
    # coordinates so that I can use them as an arguments in geodesic method , first latitude then longtitued
    from_coordinates = from_geocode.latitude, from_geocode.longitude
    to_coordinates = to_geocode.latitude, to_geocode.longitude

    # distance between the two cities in km  :
    distance = geodesic(from_coordinates, to_coordinates).kilometers
    print(
        f"\nDistance Between {from_city} To {to_city} is {round(distance,2)} km"
    )
    return distance


def format_time(time_in_hours):
    hours, remainder = divmod(time_in_hours * 60, 60)
    minutes, seconds = divmod(remainder * 60, 60)
    return f"{int(hours)} hours, {int(minutes)} minutes"

def transportationsTime(from_city: str, to_city: str):
    car_time = round(distance / 100, 2)
    print(f"Time by Car 🚗 : {format_time(car_time)}")

    if from_city in airports_df["city_name"].values and to_city in airports_df["city_name"].values:
        airplane_time = round(distance / 800, 2)
        print(f"Time by Airplane ✈️  : {format_time(airplane_time)}")

    if from_city in stations_df["city_name"].values and to_city in stations_df["city_name"].values:
        train_time = round(distance / 300, 2)
        print(f"Time by Train 🚂 : {format_time(train_time)}")


def getDistance():
    print("From:")
    while True:
        from_city: str = input("Enter The Starting Point City: ")
        if not checkValidStr(from_city):
            continue
        print("To:")
        while True:
            to_city: str = input("Enter The Destination Point City: ")
            if not checkValidStr(to_city):
                continue
            break

        distanceKm(from_city, to_city)
        transportationsTime(from_city, to_city)
        while True:
            end_input = input("\nTo Claculate Other Distance , press 1\nTo Exit Distance Calculation Service, press 2 :")
            option = checkValidInt(end_input, 2)
            if type(option) ==int:
                break
        if option == 1:
            getDistance()

        elif option == 2:
            print("Thank You For Using Our Distance Calculation Service!🌐\n")
            return
        return
