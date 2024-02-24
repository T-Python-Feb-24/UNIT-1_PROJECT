from datetime import date
import json

class Vehicle:
    
    def __init__(self, brand:str, model:str, year:int, color:str, carOwner:str, plateNumber:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.carOwner = carOwner
        self.plateNumber = plateNumber
