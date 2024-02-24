
import json

class Hotels:
    def __init__(self, hotels_data):
        try:
            with open(hotels_data, 'r', encoding="UTF-8") as file:
                self.hotels = json.load(file)
        except FileNotFoundError:
            print(f"The file {hotels_data} was not found.")
            self.hotels = []
    
    def search_hotels_by_city(self, city):
        return [hotel for hotel in self.hotels if hotel["city"] == city]

    def book_room(self, hotel, room_number):
        with open("hotels.json", 'r', encoding="UTF-8") as file:
            self.hotels = json.load(file)
        for index, h in enumerate(self.hotels):
            if h["name"] == hotel:
                for index2, room in enumerate(h["rooms"]):
                    if index2 == room_number:
                        if not self.hotels[index]["rooms"][index2]["booked"]:
                            self.hotels[index]["rooms"][index2]["booked"] = True
                            with open("hotels.json", 'w', encoding="UTF-8") as file:
                                json.dump(self.hotels, file, indent=2)
                            return True
                        else:
                            return False
                        
                        
                    with open("hotels.json", 'w', encoding="UTF-8") as file:
                        json.dump(self.hotels, file, indent=2)

    def total_cost(self, hotel, room_number, nights):
        return hotel["rooms"][room_number-1]["price"] * nights