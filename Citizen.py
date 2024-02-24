from datetime import date

class Citizen:

    def __init__(self, name:str, id:int, birthDay:date, placeOfBirth:str):
        self.name = name
        self.id = id
        self.birthDay = birthDay
        self.placeOfBirth = placeOfBirth