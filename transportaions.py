import pandas as pd
from check import checkValidInt
from check import checkValidStr
airports_file = "sa-airports.csv"
airports_df = pd.read_csv(airports_file)
stations_file = 'sa_stations.csv'
stations_df = pd.read_csv(stations_file)


def availabiltyTrans():
    ''' function return the available transportaions(airports/ train stations) in the area based on the reagion + the city '''
    while True:
        c_r_input:int = input("\nTo explore transportation options in a specific city, press 1.\nTo explore transportation availability in a particular region, press 2. :")
        choise = checkValidInt(c_r_input,2)
        if type(choise) == int:
            break
    if choise == 1 :
        while True:
            city:str = input("\nEnter City Name : ")
            if checkValidStr(city) is not None :
                break
        if city in airports_df["city_name"].values :
            print(f"Available Airports In {city}✈️ :")
            print(f"{airports_df.loc[airports_df["city_name"] == city, ["airport_name"]].to_string(index=False,header=False)}")
            print()
        else :
            print(f"No Airports In {city}!")

        if city in stations_df["city_name"].values:
            print(f"Available Train Stations In {city} 🚂:")
            print(f"{stations_df.loc[stations_df["city_name"] == city, ['train_stations']].to_string(index=False,header=False)}")
        
        else:
            print(f"No Train Stations in {city}!")

    elif choise == 2 :
        while True:
            region:str = input("\nEnter Region Name :")
            if checkValidStr(region) is not None:
                break
        if region in airports_df["region_name"].values:
             print(f"\nAvailable Airports In {region} ✈️ :")
             print(f"{airports_df.loc[airports_df["region_name"] == region, ["airport_name","city_name"]].to_string(index=False)}")

        else :
            print(f"Sorry,No Airports In {region}!")

        if region in stations_df["region_name"].values:
             print(f"\nAvailable Train Stations In {region} 🚂:")
             print(f"{stations_df.loc[stations_df["region_name"] == region, ["train_stations","city_name"]].to_string(index=False)}")

        else:
            print(f"Sorry,No Train Stations In {region}!")

    while True:
        end_input = input("\nTo search for transportation in another city or region, press 1.\nTo exit the transportation availability service, press 2.")
        option = checkValidInt(end_input,2)
        if type(option) == int:
            break
    if option == 1:
        availabiltyTrans()

    elif option == 2:
        print("\nThank You For Using Our Transportation Availability Service!🚈\n")