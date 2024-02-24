from colorama import Fore, Style
from car import Car    
def employee_menu(system):
    while True:
        print("\n" + Fore.BLUE + Style.BRIGHT +"Employee Menu")
        print(Fore.GREEN +"1. Add New Car")
        print(Fore.GREEN +"2. Update Car Information")
        print(Fore.GREEN +"3. Remove Car from System")
        print(Fore.GREEN +"4. View All Cars")
        print(Fore.GREEN +"5. Rent Car to User")
        print(Fore.GREEN +"6. View Rental Records")
        print(Fore.RED +"7. Logout")

        choice = input(Fore.YELLOW +"Enter your choice: ")
        if choice == '1':
            add_new_car(system)
        elif choice == '2':
            update_car_information(system)
        elif choice == '3':
            system.remove_car_from_system()
        elif choice == '4':
            system.view_all_cars()
        elif choice == '5':
            system.rent_car_to_user()
        elif choice == '6':
            system.view_rental_records()
        elif choice == '7':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_car(rental_system):
    id = int(input("Enter car ID: "))
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    size = input("Enter car size: ")
    price_per_day = float(input("Enter price per day: "))
    registration_number = input("Enter registration number: ")
    is_rented = input("Is car rented? (True/False): ").lower() == 'true'
    new_car = Car(id, make, model, size, price_per_day, registration_number, is_rented)
    rental_system.add_car(new_car)
    print("New car added successfully.")

def update_car_information(rental_system):
    car_id = int(input("Enter the ID of the car to update: "))
    car = rental_system.find_car_by_id(car_id)
    if car:
        print(f"Updating car: {car.make} {car.model} (ID: {car.id})")
        print("Leave input blank to keep current value.")

        new_make = input(f"New Make (current: '{car.make}'): ").strip() or car.make
        new_model = input(f"New Model (current: '{car.model}'): ").strip() or car.model
        new_size = input(f"New Size (current: '{car.size}'): ").strip() or car.size
        new_price_per_day = input(f"New Price Per Day (current: '{car.price_per_day}'): ").strip() or car.price_per_day
        new_registration_number = input(f"New Registration Number (current: '{car.registration_number}'): ").strip() or car.registration_number
        new_is_rented = input(f"Is Rented? (True/False, current: '{car.is_rented}'): ").strip().lower() == 'true'

        updates = {
            'make': new_make,
            'model': new_model,
            'size': new_size,
            'price_per_day': float(new_price_per_day),
            'registration_number': new_registration_number,
            'is_rented': new_is_rented
        }

        rental_system.update_car(car_id, updates)
        print("Car updated successfully.")
    else:
        print(f"Car with ID '{car_id}' not found.")

def remove_car_from_system(system):
    car_id = int(input("Enter the ID of the car to remove: "))
    system.remove_car_from_system(car_id)
    print("Car removed from the system.")
