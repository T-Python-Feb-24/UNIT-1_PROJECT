from enum import Enum

# car.py
class Car:
    def __init__(self, year, make, model, price, is_rented=False):
        self.year = year
        self.make = make
        self.model = model
        self.price = price
        self.is_rented = is_rented

    def rent(self):
        self.is_rented = True

    def return_rent(self):
        self.is_rented = False

    def get_details(self):
        return (
            f"Year: {self.year}, Make: {self.make}, Model: {self.model}, "
            f"Price: ${self.price}, Is Rented: {self.is_rented}"
        )
