import json
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
from datetime import date
from tabulate import tabulate
from car import Car
from employee import employee_menu
from user import user_menu
import time

class RentalCarManagementSystem:
    def __init__(self):
        self.cars = []
        self.rental_records = []  

    def load_cars(self, filename="cars.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                cars_data = json.load(file)
                self.cars = [Car(**car) for car in cars_data]
        except FileNotFoundError:
            print(f"{Fore.RED}The file {filename} was not found.")

    def save_cars(self, filename="cars.json"):
        cars_data = [car.to_dict() for car in self.cars]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(cars_data, file, indent=4)
            
    def return_car(self):
        registration_number = input("Enter the registration number of the car you want to return: ")
        car = self.find_car_by_registration_number(registration_number)
        if car:
            if car.is_rented:
                print("Processing return...")
                time.sleep(1)
                car.is_rented = False
                self.save_cars()  
                print(f"{Fore.GREEN}Car {registration_number} has been successfully returned.")
            else:
                print(f"{Fore.YELLOW}This car is not currently rented.")
        else:
            print(f"{Fore.RED}Car not found.")

    def rent_car(self, registration_number, renter_name, rental_days):
        car = self.find_car_by_registration_number(registration_number)
        if car:
            if not car.is_rented:
                print("Processing rental...")
                time.sleep(1)
                car.is_rented = True
                self.save_cars()
                rental_cost = car.price_per_day * rental_days
                rental_record = {
                    "registration_number": registration_number,
                    "rent_date": date.today().strftime("%Y-%m-%d"),
                    "renter_name": renter_name,
                    "rental_days": rental_days,
                    "rental_cost": rental_cost
                }
                self.save_rental_record(rental_record)
                print(f"{Fore.GREEN}You have successfully rented the car: {car.make} {car.model} for {rental_days} days. Total cost: ${rental_cost:.2f}")
            else:
                print(f"{Fore.YELLOW}This car is already rented.")
        else:
            print(f"{Fore.RED}Car not found.")


    def view_rental_history(self, customer_name):
        customer_history = [record for record in self.rental_records if record['renter_name'] == customer_name]
        if customer_history:
            headers = customer_history[0].keys() if customer_history else []
            print(tabulate(customer_history, headers="keys", tablefmt="grid"))
        else:
            print(f"{Fore.YELLOW}No rental history found for {customer_name}.")


    def rent_car_to_user(self):
        registration_number = input("Enter the registration number of the car to rent: ")
        rental_days = int(input("Enter the number of days for rental: "))
        renter_name = input("Enter the renter's name: ")
        renter_id = input("Enter the renter's ID (10 digits): ")
        if len(renter_id) != 10 or not renter_id.isdigit():
            print(f"{Fore.RED}Invalid ID. Please enter a 10-digit numerical ID.")
            return
        self.rent_car(registration_number, renter_name, rental_days)
    def find_car_by_id(self, car_id):
        for car in self.cars:
            if car.id == car_id:
                return car
        return None
    def update_car(self, car_id, updates):
        car = self.find_car_by_id(car_id)
        if car is not None:
            if 'make' in updates:
                car.make = updates['make']
            if 'model' in updates:
                car.model = updates['model']
            if 'size' in updates:
                car.size = updates['size']
            if 'price_per_day' in updates:
                car.price_per_day = updates['price_per_day']
            if 'registration_number' in updates:
                car.registration_number = updates['registration_number']
            if 'is_rented' in updates:
                car.is_rented = updates['is_rented']
            print(f"Car ID {car_id} updated successfully.")
        else:
            print(f"No car found with ID {car_id}.")
    def remove_car_from_system(self):
        registration_number = input("Enter the registration number of the car to remove: ")
        car = self.find_car_by_registration_number(registration_number)
        if car:
            self.cars.remove(car)
            self.save_cars()  # Save the updated cars list to a file
            print(f"Car {registration_number} removed successfully.")
        else:
            print(f"Car with registration number {registration_number} not found.")
    def view_rental_records(self):
        try:
            with open('rentals.json', 'r', encoding="utf-8") as file:
                rental_records = json.load(file)
                if rental_records:
                    headers = rental_records[0].keys()  # Get the keys of the first record
                    records_data = [record.values() for record in rental_records]  # Extract values from each record
                    print(tabulate(records_data, headers=headers, tablefmt="grid"))
                else:
                    print(f"{Fore.YELLOW}No rental records found.")
        except FileNotFoundError:
            print(f"{Fore.RED}No rental records found.")



    def save_rental_record(self, record):
        self.rental_records.append(record)  
        with open('rentals.json', 'w', encoding="utf-8") as file:
            json.dump(self.rental_records, file, indent=4)  # Save to file

    def find_car_by_registration_number(self, registration_number):
        return next((car for car in self.cars if car.registration_number == registration_number), None)

    def view_all_cars(self):
        headers = ["ID", "Make", "Model", "Size", "Price/Day", "Reg Number", "Is Rented"]
        table_data = [[car.id, car.make, car.model, car.size, car.price_per_day, car.registration_number, 'Yes' if car.is_rented else 'No'] for car in self.cars]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def load_rental_records(self, filename="rentals.json"):  
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.rental_records = json.load(file)
        except FileNotFoundError:
            print(f"{Fore.RED}The file {filename} was not found.")
        except json.JSONDecodeError:
            self.rental_records = []
    
    def add_car(self, new_car):
        
        self.cars.append(new_car)
        self.save_cars() 
        print(f"Car {new_car.registration_number} added successfully.")

def main():
    rental_system = RentalCarManagementSystem()
    rental_system.load_cars()
    rental_system.load_rental_records()  

    while True:
        print("\n" + Fore.BLUE + Style.BRIGHT + "Welcome to the Car Rental System")
        print(Fore.GREEN + "1. Employee")
        print(Fore.GREEN + "2. User")
        print(Fore.RED + "3. Exit")

        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == '1':
            employee_menu(rental_system)
        elif choice == '2':
            user_menu(rental_system)
        elif choice == '3':
            print(Fore.BLUE + "Thank you for using the Car Rental System.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
