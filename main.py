from parking import register_car, leave_parking, check_car
from colorama import Fore, Back ,Style

def main():
    while True:
        print("\n")
        print(Fore.WHITE + Style.BRIGHT +
"""Welcome to the Parking lot
How can i help today\n
              """)
        
        print(Fore.BLUE+"1. Register Car")
        print(Fore.YELLOW +"2. Leave Parking")
        print(Fore.GREEN+"3. Check Car")
        print(Fore.RED + "4. Exit \n")
        choice = input(Fore.WHITE + "Enter your choice -> ")
        print("\n")

        if choice == "1":
            register_car()
        elif choice == "2":
            leave_parking()
        elif choice == "3":
            check_car()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()