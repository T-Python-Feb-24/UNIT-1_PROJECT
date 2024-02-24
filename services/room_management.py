from datetime import time, date
import json
import random
from colorama import Fore, Back, Style

class RoomManagement:
    def __init__(self) -> None:
        self.__list_of_rooms = self.read_rooms_file()

    def get_list_of_rooms(self):
            return self.__list_of_rooms
        
    def read_rooms_file(self):
            try:
                with open('rooms.json', mode='r', encoding='utf-8') as file:
                    list_of_rooms = json.loads(file.read())
                    return list_of_rooms
            except FileNotFoundError:
                return []

    def save_rooms_file(self, list_of_rooms):
            with open('rooms.json', mode='w', encoding='utf-8') as file:
                rooms_file_contents = json.dumps(list_of_rooms)
                file.write(rooms_file_contents)

    def add_room(self, list_of_rooms):
            print('Here you can add your new room!')
            room_number:int = int(input('Enter room number here: '))
            room_capacity:int = int(input('Enter room capacity here: '))
            room_PIN:int = random.randint(1000, 9999)
            print('is the room rented. Y/N ?')
            user_choice:str = input('enter your answer here: ')
            while True:
                if user_choice.upper() == 'Y':
                    is_rented:bool = True
                    break
                elif user_choice.upper() == 'N':
                    is_rented:bool = False
                    break
                else:
                    print('You Entered Wrong Data!!!')
                
            enter_time:time = input('Provide the enterance date(HH:MM): ')
            enter_date:date = input('Provide the enterance date here(YYYY-MM-DD): ')
            new_room:dict = {
                "room_number":room_number,
                "room_capacity":room_capacity,
                "room_PIN":room_PIN,
                "is_rented":is_rented,
                "enter_time":enter_time,
                "enter_date":enter_date
            }
            self.__list_of_rooms.append(new_room)
            self.save_rooms_file(self.__list_of_rooms)
            print(Fore.GREEN+'Room Added Successfully')
            print(Style.RESET_ALL)