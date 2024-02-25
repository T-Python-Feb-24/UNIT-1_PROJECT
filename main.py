import art
import sys
from classes.user import customer, User, login, create_user, get_all_users
from classes.book import Stock


def main():
    welcome()
    if len(sys.argv) == 2 and sys.argv[1] == "-a":
        admin()
    else:
        while True:
            choice: str = input("Do you have an account:(y/n)? ")
            if choice == ("n" or "N"):
                create_user()
            elif choice != ("y" or "Y"):
                print("Invalid choice")
                continue
            break

        try:
            user:  customer = login()
            print(f"welcome to our bookstore {user.user_name}")
            while True:
                customer_menu()
                choice = input("Enter your choice: ")
                stock = Stock()
                match choice:
                    case "1":
                        stock.list_of_books()
                    case "2":
                        user.add_to_cart()
                    case "3":
                        user.remove_book()
                    case "4":
                        user.print_list_cart()
                    case "q":
                        print("Goodbye :)  see you agine")
                        exit(0)
                    case _:
                        print("Invlid choice")

        except Exception as e:
            print(e)


def admin():
    try:
        user:  User = login()
        print(f"welcome {user.user_name}")
        while True:
            admin_menu()
            choice: str = input("Enter your choice: ")
            stock = Stock()
            match choice:
                case "1":
                    stock.list_of_books()
                case "2":
                    stock.add_book()
                case "3":
                    stock.remove_book()
                case "4":
                    get_all_users()
                case "q":
                    print("Goodbye :)  see you agine")
                    exit(0)
                case _:
                    print("Invlid choice")
    except Exception as e:
        print(e)


def welcome():
    greeting = "Welcome to Wissam BookStoor!"
    art.tprint("-"*30, "small")
    art.tprint(greeting, "small")
    art.tprint("-"*30, "small")


def customer_menu():
    print(f'''
    1- List the books in the stock
    2- Add a book to your cart by the book id
    3- Remove a book from your cart by the book id
    4- List of books in your cart
    q- exit
          ''')


def admin_menu():
    print(f'''
    1- List the books in the stock
    2- Add or update a book in stock
    3- Remove a book from
    4- List of all users with there books
    q- exit
          ''')


if __name__ == "__main__":
    main()
