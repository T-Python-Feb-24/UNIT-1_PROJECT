from check import checkValidInt

def websites():
    print(''' Discover Local Services:
             
-✈️ Airplane Booking - Explore and book flights with Saudia and Flynas
-🚆 Train Tickets Booking - Plan and book train journeys with Saudi Railways (SAR)

Ride-Hailing Apps:
-🚖 Uber - Reliable ride-hailing service
-🚗 Careem - Ride-hailing and delivery services

Food Delivery:
-🍔 HungerStation - Order your favorite meals from local restaurants
-🍣 The Chefz - Explore a variety of culinary delights

Booking Accommodations:
- 🏨 Booking.com - Find and book hotels, apartments, and more.''')

    while True:
        end_input = input("\nTo Exit The Service, press 1")
        option = checkValidInt(end_input, 1)
        if type(option) == int:
            break

    if option == 1:
        print("\nThank You For Using Our Service📱")
