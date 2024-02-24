from datetime import date

class Ticket:
    def __init__(self, brand:str, model:str, year:int, plate_number:str, owner_name:str, Violation:str, cost:int):
        self.brand = brand
        self.model = model
        self.year = year
        self.plate_number = plate_number
        self.owner_name = owner_name
        self.violation = Violation
        self.cost = cost

