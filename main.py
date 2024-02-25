import json
from dealership import Dealership
from user import User
from admin import Admin

def load_data(admin):
    try:
        with open("car_data.json", "r", encoding="utf-8") as file:
            cars = json.load(file)
            return cars
    except:
        return []

def save_data(admin, cars):
    with open("car_data.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(cars))
    print("Data saved successfully.")

def add_car(admin, dealership, car):
    if not admin.check_credentials(admin.username, admin.password):
        raise Exception("Unauthorized access")
    dealership.inventory.append(car)
    save_data(admin, dealership.inventory)

def remove_car(admin, dealership, car):
    if not admin.check_credentials(admin.username, admin.password):
        raise Exception("Unauthorized access")
    dealership.inventory.remove(car)
    save_data(admin, dealership.inventory)

def get_installment_period():
    while True:
        try:
            installment_period = int(input("Enter the installment period (in months): "))
            if installment_period > 0:
                return installment_period
            else:
                print("Installment period must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def load_sold_cars(admin):
    try:
        with open("sold_cars.json", "r", encoding="utf-8") as file:
            sold_cars = json.load(file)
            return sold_cars
    except:
        return []

def save_sold_cars(admin, sold_cars):
    with open("sold_cars.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(sold_cars))
def cars(dealership):
    return dealership.inventory

def display_inventory_value(dealership):
    total_value = sum(car["price"] for car in dealership.inventory)
    print(f"Total inventory value: ${total_value:.2f}")

class Dealership:
    def __init__(self, name, admin_username, admin_password):
        self.name = name
        self.admin = Admin(admin_username, admin_password)
        self.inventory = load_data(self.admin)
        self.sold_cars = load_sold_cars(self.admin)

    def sell_car(self, car):
        buyer = User(
            first_name=input("Enter the buyer's first name: "),
            last_name=input("Enter the buyer's last name: "),
            email=input("Enter the buyer's email: "),
            phone=input("Enter the buyer's phone: "),
            id_number=input("Enter the buyer's ID number: "),
            bank_account=input("Enter the buyer's bank account: ")
        )
        self.inventory.remove(car)
        self.sold_cars.append(car)
        save_data(self.admin, self.inventory)
        save_sold_cars(self.admin, self.sold_cars)

admin = Admin("admin", "password")
dealership = Dealership("ABC Motors", admin.username, admin.password)

if __name__ == '__main__':
    while True:
        print("\nWelcome to the Car Dealership!")
        print("1. Add a car")
        print("2. Remove a car")
        print("3. Search for a car")
        print("4. Display all cars")
        print("5. Display inventory value")
        print("6. Sell a car")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            make = input("Enter the car make: ")
            model = input("Enter the car model: ")
            year = int(input("Enter the car year: "))
            price = float(input("Enter the car price: "))

            new_car = {
                "make": make,
                "model": model,
                "year": year,
                "price": price
            }

            cars.append(new_car)
            save_data(cars)

        elif choice == 2:
            remove_make = input("Enter the car make to remove: ")
            remove_model = input("Enter the car model to remove: ")

            for car in cars:
                if car["model"] == remove_model and car["make"] == remove_make:
                    cars.remove(car)
                    save_data(cars)
                    print("Car removed successfully.")
                    break
            else:
                print("Car not found.")

        elif choice == 3:
            search_year = int(input("Enter the car year to search: "))

            search_results = [car for car in cars if car["year"] == search_year]

            if not search_results:
                print("Car not found.")
            else:
                for car in search_results:
                    print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, Price: ${car['price']}")

        elif choice == 4:
            for idx, car in enumerate(cars, start=1):
                print(f"{idx}. {car['make']}, {car['model']}, {car['year']}, ${car['price']}")

        elif choice == 5:
            display_inventory_value(dealership)

        elif choice == 6:
            sell_car(dealership)

        elif choice == 7:
            break
        else:
            print("Invalid option, please select a valid option.")