import json
from car import Car
from datetime import datetime
from colorama import Fore, Back, Style

HOURLY_RATE = 3.0

DATA_FILE = "parked_cars.json"

def load_parked_cars():
    try:
        with open(DATA_FILE, 'r') as file:
            data = file.read()
            if data:
                parked_cars = []
                try:
                    json_data = json.loads(data)
                    for car_data in json_data:
                        car = Car(
                            car_data['license_plate'],
                            car_data['start_date'],
                            car_data['end_date']
                        )
                        parked_cars.append(car)
                except json.JSONDecodeError:
                    parked_cars = []
            else:
                parked_cars = []
    except FileNotFoundError:
        parked_cars = []
    
    return parked_cars

'''def check_car():
    license_plate = input("Enter the license plate of the car: ")
    parked_cars = load_parked_cars()
    found = False
    for car in parked_cars:
        if car.license_plate == license_plate:
            found = True
            print(f"Car with license plate {license_plate} is parked.")
            break
    if not found:
        print(Fore.BLUE + f"Car with license plate {license_plate}is parked.") #f"Car with license plate {license_plate} is not parked.")'''

def leave_parking():
    license_plate = input("Enter the license plate of the car to leave -> ")
    parked_cars = load_parked_cars()
    found = False
    for car in parked_cars:
        if car.license_plate == license_plate:
            found = True
            parked_cars.remove(car)
            end_date_str = input("Enter the end date (YYYY-MM-DD HH:MM) -> ")
            try:
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M")
                if end_date < car.start_date:
                    print(Fore.RED + "Invalid date. The leaving date cannot be before the registration date.")
                    return
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM.")
                return
            print("\n")
            car.end_date = end_date
            save_parked_cars(parked_cars)
            duration = car.end_date - car.start_date
            hours = duration.total_seconds() / 3600
            days = hours // 24
            extra_hours = hours % 24

            if extra_hours < 12:
                price = (days * 30) + (extra_hours * 3)
            else:
                price = (days + 1) * 30

            print(Fore.GREEN + f"Car with license plate {license_plate} has left the parking. ")
            print(Fore.GREEN + f"Total parking duration: {hours:.2f} hours ")
            print(Fore.GREEN + f"Price: {price:.2f} $ \n")
            break
    if not found:
        print(Fore.BLUE + f"Car with license plate {license_plate} is not parked.")

def save_parked_cars(parked_cars):
    data = []
    for car in parked_cars:
        car_data = {
            'license_plate': car.license_plate,
            'start_date': car.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            'end_date': car.end_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        data.append(car_data)
    
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

def is_parking_full():
    parked_cars = load_parked_cars()
    return len(parked_cars) >= 10


def register_car():
    if is_parking_full():
        print(Fore.RED + "Parking is full. Cannot register the car.")
        print("_________________________")
        return

    try:
        license_plate = input(Fore.GREEN + "Enter car license plate -> ")
        if len(license_plate) > 7:
            raise ValueError("Invalid license plate. License plate should not exceed 7 characters.")

        parked_cars = load_parked_cars()
        for car in parked_cars:
            if car.license_plate == license_plate:
                print(Fore.RED + f"Car with license plate {license_plate} is already registered.")
                return

        print(Fore.GREEN + f"Your license plate is -> {license_plate}\n")

        start_date_str = input(Fore.GREEN + "Enter parking start date and time (YYYY-MM-DD HH:MM) -> ")
        print(Fore.GREEN + f"The start date is -> {start_date_str}\n")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M")
    except ValueError as e:
        print(Fore.RED + str(e))
        return

    car = Car(license_plate, start_date, None)
    parked_cars.append(car)
    save_parked_cars(parked_cars)
    print(Fore.GREEN + f"Car with license plate {license_plate} registered successfully.\n")

def load_parked_cars():
    try:
        with open("parked_cars.json", "r") as file:
            parked_cars_data = json.load(file)
            parked_cars = []
            for car_data in parked_cars_data:
                license_plate = car_data['license_plate']
                start_date = datetime.strptime(car_data['start_date'], "%Y-%m-%d %H:%M:%S")
                end_date = datetime.strptime(car_data['end_date'], "%Y-%m-%d %H:%M:%S") if car_data['end_date'] else None
                car = Car(license_plate, start_date, end_date)
                parked_cars.append(car)
    except FileNotFoundError:
        parked_cars = []
    return parked_cars

def save_parked_cars(parked_cars):
    parked_cars_data = []
    for car in parked_cars:
        car_data = {
            'license_plate': car.license_plate,
            'start_date': car.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            'end_date': car.end_date.strftime("%Y-%m-%d %H:%M:%S") if car.end_date else None
        }
        parked_cars_data.append(car_data)
    with open("parked_cars.json", "w") as file:
        json.dump(parked_cars_data, file, indent=4)

def check_car():
    try:
        license_plate = input("Enter car license plate: ")
        if len(license_plate) > 7:
            raise ValueError("Invalid license plate. License plate should not exceed 7 characters.")
        parked_cars = load_parked_cars()
        for car in parked_cars:
            if car.license_plate == license_plate:
                print(Fore.GREEN + f"Car with license plate {license_plate} is parked.")
                print("___________________________")
                return
        print(Fore.RED + f"Car with license plate {license_plate} is not found in the parking.")
        print("_________________________________________________________")
    except ValueError as e:
        print(Fore.RED + str(e))