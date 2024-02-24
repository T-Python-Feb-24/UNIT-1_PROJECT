from Classes.Hotel import Hotels
from Classes.colors import colors

hotels = Hotels("hotels.json")

def main():
    colors.intro()
    input()
    
    print(colors.YBI + "\nWelcome to our hotel booking program!" + colors.RESET)
    
    while True:
        print("------ Choose an option ------")
        print("1. Search hotels by city.")
        print("2. Book a room.")
        print("3. Exit.")

        option = input("Choose option: ")
        match option:
            case "1":

                # List all cities in the database and ask user for a city name
                '''Add List_City function'''
                
                print("  \4 Riyadh. \n  \4 Jeddah.")
                city = input("Choose the city: ")
                hotels_in_city = hotels.search_hotels_by_city(city)
                
                if hotels_in_city:
                    print(colors.BBU + f"Hotels in {city}:" + colors.RESET)
                    for hotel in hotels_in_city:
                        print("  \4", hotel["name"], ", Available Rooms: ", len(hotel['rooms']))
                    print("")
                else:
                    print(colors.RED + f"{city} not found." + colors.RESET)
            
            case "2":
                city = input("Enter the city: ")
                hotels_in_city = hotels.search_hotels_by_city(city)

                # Check for hotels in the choosen city
                if hotels_in_city:
                    print(colors.BBU +f"Hotels in {city}:" + colors.RESET)
                    for hotel in hotels_in_city:
                        print("   \4", hotel["name"])
                    print("")
                    hotel_name = input("Enter the hotel name: ")
                    hotel = next((hotel for hotel in hotels_in_city if hotel["name"] == hotel_name), None)

                    # Check for available rooms in the choosen hotel
                    if hotel:
                        print(colors.GBU + "Rooms available:" + colors.RESET)
                        for i, rooms in enumerate(hotel["rooms"]):
                            print(f"   {i+1}. Room number: {rooms['number']}, Type: {rooms['type']}, Price: ${rooms['price']}")
                        print("")
                        
                        room_number = int(input("Choose a room: "))
                        booked = hotels.book_room(hotel_name, room_number-1)
                        
                        # Check if the room is booked or not
                        if booked:
                            nights = int(input("Enter the number of nights: "))
                            print(colors.BGREEN + "Room Booked Successfully!!" + colors.RESET)
                            total_cost = hotels.total_cost(hotel, room_number, nights)
                            print(colors.GREEN + f"The total cost is {total_cost}.\n" + colors.RESET)
                        else:
                            print(colors.BREDB + "This Room is already Booked.\n" + colors.RESET)

                    else: print(colors.RED + f"{hotel_name} not found." + colors.RESET)
                else: print(colors.RED + f"{city} not found." + colors.RESET)
            
            case "3":
                print("---------------------------------")
                print(colors.YBI)
                colors.animate_text("Thank you for using our service!!")
                print(colors.RESET)
                break
            
            case _:
                print(colors.RED + "Invalid option. Please try again." + colors.RESET)

main()