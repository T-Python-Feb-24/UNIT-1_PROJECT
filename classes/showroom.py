import json


# showroom.py
class CarShowroom:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        self.cars.remove(car)

    def display_cars(self):
        for car in self.cars:
            print(car.get_details())


