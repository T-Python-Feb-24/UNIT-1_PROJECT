# Importing necessary modules and classes
from dataclasses import dataclass, field, asdict
from classes.book import Book, Stock
from typing import Optional  # A module that provides runtime type checking
# A function that gets password input, hiding the input on the screen
from getpass import getpass
import sys  # A module that provides access to some variables used or maintained by the Python interpreter
import hashlib  # This library is used for hashing passwords
import json  # This library is for working with JSON data
# This library is for interacting with the operating system
from os import path as opath
from colorama import Fore, init
init(autoreset=True)


@dataclass
class User:
    user_name: str  # A string attribute to store the user name
    # A string attribute to store the user's password
    password: Optional[str] = field(init=True, repr=False)
    # An optional string attribute to store the user's phone number
    phone_number: Optional[str] = field(default=None)


def __get_user_by_user_name(user_name: str) -> dict | None:  # -> dict | None:
    """
    This method retrieves a user from the users.json file based on their user_name.
    It returns the user as a dictionary if found, otherwise it returns None.
    """
    if opath.exists("users.json"):  # Check if the users.json file exists
        with open('users.json', 'r') as f:  # Open the users.json file in read mode
            # Load the JSON data from the file into a Python list
            users: list[dict] = json.load(f)
        for user in users:  # Iterate through the list of users
            # Check if the user_name matches the input
            if user['user_name'] == user_name.lower():
                return user  # Return the user if found
    return None  # Return None if the user is not found


def login() -> bool:
    """
    This method logs in a user with the given user_name and password.
    It returns True if the login is successful, otherwise it returns False.
    """
    print(f"{" Sign In ":*^35}")
    caller: str = sys._getframe().f_back.f_code.co_name
    if caller != "admin":
        user_name: str = input("Enter your username: ")
    else:
        user_name = "admin"
    # Get the user by their user_name
    user = __get_user_by_user_name(user_name)
    if user:  # If the user is found
        password: str = getpass("Enter your password:(curser is hidden) ")
        hashed_password = hashlib.sha256(
            password.encode()).hexdigest()  # Hash the password
        # Check if the hashed password matches the one in the user dictionary
        if hashed_password == user['password']:
            # Return True to indicate a successful login
            print()
            return customer(**user)
    # raise an error message
    raise ValueError(f"{Fore.RED}Invalid user_name or password.")


def get_all_users():
    """
    This method retrieves all users from the users.json file.
    It returns the users info as a dictionary if found exept password.
    """
    if opath.exists("users.json"):  # Check if the users.json file exists
        with open('users.json', 'r') as f:  # Open the users.json file in read mode
            # Load the JSON data from the file into a Python list
            users: list[dict] = json.load(f)
            print("="*40)
        for i, user in enumerate(users, 0):  # Iterate through the list of users
            if user["user_name"] == "admin":
                continue
            user_name: str = user["user_name"]
            phone_nember: str = user["phone_number"]
            cart: list[dict] = user["cart"]
            print(f'{i:>8}- Name{":":>9} {user_name}')
            print(f'{"Phone Number":>22}: {phone_nember}')
            print(f'\nbook in (his\\her) cart :')
            print("-"*40)
            cart = [f'{i}- {book['title']}' for i, book in enumerate(cart, 1)]
            print(f'{" "*12}{"\n".join(cart):}')
            print("="*40, end="\n\n")


@dataclass
class customer(User):
    cart: list[Book] = field(default_factory=list)
    __stock: Stock = field(default_factory=Stock)

    def __post_init__(self):
        super()
        self.cart: list[Book] = self.__get_cart()

    def print_list_cart(self):
        print("\nBooks in your cart:")
        print("-"*20)
        if len(self.cart) > 0:
            for i, book in enumerate(self.cart, 1):
                print(f"{i}- [{book.id}] {book.title}")
            print("-"*20)
            return
        print("Your cart is empty")

    def is_exist(self, book_id):
        for book in self.cart:
            if book.id == book_id:
                return True
        return False

    def __get_cart(self):
        try:
            with open("users.json", "r", encoding="utf-8") as file:
                users: list[dict] = json.load(file)
            for user in users:
                if user["user_name"] == self.user_name:
                    cart = [Book(**item) for item in user["cart"]]
            return cart
        except Exception as e:
            print(e)

    def add_to_cart(self):
        self.__stock.list_of_books()
        while (book_id := input("Put the book id to add it to your cart: ")) != "q":
            try:
                book_id = int(book_id)
                if book_id in range(1, len(self.__stock)+1):
                    book: Book = self.__stock.get_book(book_id)
                    if book.in_stock == 0:
                        print(f"😞sorry The book \
                              {book.title} is not in stock right now")
                        return
                    if not self.is_exist(book_id):
                        self.cart.append(book)
                        print(
                            f'\t{"-"*60}\n\t{Fore.GREEN}The book ({book.title}) added to your cart successfully\n\t{Fore.WHITE}{"-"*60}')
                        self.save_cart()
                        self.__stock.book_decreamnt_quantity(book)
                        break
                    else:
                        print(f"The book {book.title} already in your cart")

                else:
                    print(
                        Fore.RED+"Wrong input you should put the book id from your cart list")
            except ValueError:
                print(
                    Fore.RED+"Wrong input you should put the book id from the stock list")

    def remove_book(self):
        self.print_list_cart()
        if self.cart == []:
            return
        while True:
            try:
                book_id = int(
                    input("Put the book id to remove book from your cart: "))
                if book_id in range(1, len(self.__stock)+1):
                    book_title: str = self.cart.pop(book_id-1).title
                    print(
                        f'{"-"*60}\nThe book ({book_title}) removed from your cart successfully\n{"-"*60}')
                    self.save_cart()
                    break
                else:
                    print(
                        Fore.RED+"Wrong input you should put the book id from your cart list")
            except ValueError as e:
                print(e)

    def save_cart(self):
        users: list[dict] = [{}]
        try:
            with open('users.json', 'r') as f:  # Try to open the users.json file in read mode
                # Load the JSON data from the file into a Python list
                users: list[dict] = json.load(f)
        except FileNotFoundError:  # If the file is not found
            print(f"{Fore.RED}Sorry there a problem in the json file")
        for user in users:
            if user["user_name"] == self.user_name:
                cart_list_dict: list = []
                for book in self.cart:
                    cart_list_dict.append(asdict(book))
                user["cart"] = cart_list_dict
        with open('users.json', 'w') as f:  # Open the users.json file in write mode
            # Save the updated list as JSON data to the file
            json.dump(users, f)


def __valid_username(username: str):
    if not username.isalpha():
        return False
    return True


def create_user():
    """
    This method creates a new user with the given user_name and password, and saves it to the users.json file.
    """
    print(f"{" Sign UP ":*^35}")
    while True:
        user_name: str = input("Enter your username: ")
        if not __valid_username(user_name):
            continue
        break
    while True:
        phone_number: str = input("Enter your phone number: ")
        if (len(phone_number) != 10 or not phone_number.isdigit()):
            print(f"{Fore.RED}Invalid phone number should be 10 digits")
            continue
        break
    while True:
        password = getpass(
            "Enter your password:(curser is hidden) ")
        if len(password) != 6:
            continue
        break
    password = hashlib.sha256(
        password.encode()).hexdigest()  # Hash the password
    # Create a new user dictionary
    user = {
        'user_name': user_name,
        'password': password,
        'phone_number': phone_number,
        "cart": []
    }
    try:
        with open('users.json', 'r') as f:  # Try to open the users.json file in read mode
            # Load the JSON data from the file into a Python list
            users = json.load(f)
    except FileNotFoundError:  # If the file is not found
        users = []  # Create an empty list
    users.append(user)  # Add the new user to the list
    with open('users.json', 'w') as f:  # Open the users.json file in write mode
        # Save the updated list as JSON data to the file
        json.dump(users, f)
    print(f"{Fore.GREEN}You can now use your account to login")


# check module running
def main():
    print(sys.argv)
    u = User("wissam")
    if u.user_type:
        print(f"Login as {u.user_name} successful.")


if __name__ == '__main__':
    main()
