from colorama import Fore, Style

def user_menu(self):
        while True:
            print("\n" + Fore.BLUE + Style.BRIGHT + "User Menu")
            print(Fore.GREEN + "1. View Available Cars")
            print(Fore.GREEN + "2. Rent a Car")
            print(Fore.GREEN + "3. Return a Car")
            print(Fore.GREEN + "4. View Rental History")
            print(Fore.RED + "5. Logout")

            choice = input(Fore.YELLOW + "Enter your choice: ")

            if choice == '1':
                self.view_all_cars()
            elif choice == '2':
                self.rent_car_to_user()
            elif choice == '3':
                self.return_car()
            elif choice == '4':
                customer_name = input("Enter your name: ")
                self.view_rental_history(customer_name)
            elif choice == '5':
                print(Fore.BLUE + "Logging out...")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")