from services.user_management import UserManagement
from services.book_management import Library
from services.room_management import RoomManagement
import json
from datetime import datetime, timedelta, date, time
from colorama import Fore, Back, Style
#object Book
book = Library()
#This list have (books.json)
list_of_books:list = book.get_list_of_book()

#object Room
room = RoomManagement()
#This list have (rooms.json)
list_of_rooms:list = room.get_list_of_rooms()

#object User
user = UserManagement()
#this list have (users.json)
list_of_users:list = user.get_list_of_users()


def search_for_book():
    print('What is the book title you are looking for?')
    user_search_input = input('Type here: ')

    book_found = False  

    for item in list_of_books:
        if item['title'] == user_search_input:
            print()
            print(Fore.GREEN+ 'Yes, it\'s available!')
            print(Style.RESET_ALL)
            print(f'-your book title is: {item["title"]}')
            print(f'-the author is: {item["author"]}')
            print(f'-its published in: {item["published"]}')
            print(f'-its have {item["pages"]} pages')
            print(f'-here the description of a book: \n{item["description"]}')
            print(f'-we have {item["availability"]} quantity')
            book_found = True
            print()
            print(Fore.YELLOW+'Press Enter To Get Back Home Page')
            print(Style.RESET_ALL)
            input()
            break 
    if not book_found:
        print(Fore.RED+'Sorry, it\'s not available.')
        print(Style.RESET_ALL)

def view_the_books():
    print('Our Books: ')
    for item in list_of_books:
        print()
        print('-',item['title'])
    print()

def rent_book():
    print('What is the book title you are looking for?')
    user_search_input = input('Type here: ')
    book_found = False  

    for item in list_of_books:
        if item['title'] == user_search_input:
            while True:
                print()
                print(Fore.GREEN+'The book are found')
                print(Style.RESET_ALL)
                print('Do you want to rent that book. Y/N ?')
                user_answer:str = input('Type here: ')
                if user_answer.upper()=='Y':
                    rental_duration:int = int(input('Enter rental duration (in days): '))
                    item['availability']-=1
                    #item['rental_duration'] = rental_duration
                    current_date = datetime.now()
                    end_date:datetime = current_date + timedelta(days=rental_duration)
                    end_date_formatted = end_date.strftime('%Y-%m-%d')
                    print(f'Book rented successfully! Due date: {end_date_formatted}')
                    print()
                    book.save_books_file(list_of_books)
                    for index in list_of_users:
                        if index['email']==user_email:
                            if "rented_books" in index:
                                index['rented_books']['title']=user_search_input
                                index['rented_books']['due']=end_date_formatted
                    user.save_users_file(list_of_users)
                    break
                elif user_answer.upper()=='N':
                    print(Fore.YELLOW+'Alright, moving to home page...')
                    print(Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED+'You entered a wrong letter.')
                    print(Style.RESET_ALL)
            book_found = True
            break 
    if not book_found:
        print(Fore.RED+'Sorry, it\'s not available.')
        print(Style.RESET_ALL)

def check_room_availability(room_number:int, list_of_rooms:list)->bool:
    """
    Checks if a room is rented or available based on its room number.
    
    Args:
        room_number (int): The room number to check.
        rooms_data (list[dict]): A list of dictionaries containing room information.
        
    Returns:
        bool: True if the room is rented, False if it's available.
    """

    for study_room in list_of_rooms:
        if study_room["room_number"] == room_number:
            return study_room['is_rented']

def view_the_rooms():
    for study_room in list_of_rooms:
        print()
        print(f'- The room with number: {study_room['room_number']}, and its enough for: {study_room['room_capacity']} people')
    print()
    print('the rooms that are available: ')
    for study_room in list_of_rooms:
        is_rented:bool = check_room_availability(study_room['room_number'], list_of_rooms)
        if is_rented == False:
            print(f'- room with number: {study_room['room_number']}')

def booking_study_room(list_of_rooms:list):
    print('Our study rooms: ')
    view_the_rooms()
    print()

    while True:
        user_answer:int = int(input('Enter here the number of the room you want: '))
        is_room_rented:bool = check_room_availability(user_answer,list_of_rooms)
        if is_room_rented == True:
            print(Fore.RED+f"Room {user_answer} is currently rented.")
            print(Style.RESET_ALL)
            break
        else:
            print(Fore.GREEN+f"Room {user_answer} is available for booking.")
            print(Style.RESET_ALL)
            print('Do you want to confirm your booking? Y/N')
            user_confirmation:str = input('Enter here: ')
            if user_confirmation.upper() == 'Y':
                enter_date:date = input('Enter date (YYYY-MM-DD): ')
                enter_time:time = input('Enter time (HH:MM): ')
                for study_room in list_of_rooms:
                    if study_room['room_number'] == user_answer:
                        study_room['enter_time'] = enter_time
                        study_room['enter_date'] = enter_date
                        study_room['is_rented'] = True
                    room.save_rooms_file(list_of_rooms)
                for study_room in list_of_rooms:
                    if study_room['room_number']==user_answer:
                        print(f'the PIN for room door is: {study_room['room_PIN']}')
                
                for index in list_of_users:
                    if index['email']==user_email:
                        index['study_room_bookings']['room_number']=user_answer
                        index['study_room_bookings']['enter_date']=enter_date
                        index['study_room_bookings']['enter_time']=enter_time
                user.save_users_file(list_of_users)
                
                print(Fore.GREEN+'Study room booked successfully!')
                print(Style.RESET_ALL)
                break
            elif user_confirmation.upper()=='N':
                print(Fore.YELLOW+'getting back to the rooms booking menue...')
                print(Style.RESET_ALL)
                break
            else:
                print(Fore.RED+'Please Enter a valid inputs')
                print(Style.RESET_ALL)

def check_user_login(user_email:str, user_password:int)->bool:
    for user_login in list_of_users:
        if user_login['email']==user_email and user_login['password']==user_password:
            return True
    else:
        return False

def pre_main()->str:
    while True:
        print('WELCOME TO OUR LIBRARY')
        print('Enter Your Email and Password')
        user_email = input("Your Email: ").lower()
        user_password = int(input("Your Password: "))
        is_user_have_account:bool = check_user_login(user_email, user_password)

        if is_user_have_account == True:
            return user_email
        else:
            print(Fore.YELLOW+"This Email and Password Incorrect.You want to Make An Account?")
            print(Style.RESET_ALL)
            user_sign_up:str = input('Enter Y/N: ')
            print()
            if user_sign_up.upper()=='Y':
                user_name:str = input('Please Enter Your Name: ')
                user_email = input('Please Enter Your Email(user@gmail.com): ').lower()
                user_password = int(input('Please Enter Your Password In PIN Format (4-digits)'))
                new_user:dict = {
                    "user_name":user_name,
                    "email":user_email,
                    "password":user_password,
                    "rented_books":{
                        "title":"",
                        "due":""
                    },
                    "study_room_bookings":{
                        "room_number":0,
                        "enter_date":"",
                        "enter_time":""
                    }
                }
                list_of_users.append(new_user)
                user.save_users_file(list_of_users)
                return user_email
            elif user_sign_up.upper()=='N':
                pass
            else:
                print(Fore.RED+'You Entered Wrong Inputs!')
                print(Style.RESET_ALL)

user_email = pre_main()
for i in list_of_users:
    if i['email']==user_email:
        user_name=i['user_name']

def view_profile():
    print()
    print('User Profile:')
    print(f'Name: {user_name}')
    print(f'Email: {user_email}')

    print('Rented Books:')
    for i in list_of_users:
        if i['email']==user_email:
            if "rented_books" in i:
                print(f"- {i['rented_books']['title']} (Due: {i['rented_books']['due']})")
        print()

    print('Study Room Bookings:')
    for i in list_of_users:
        if i['email']==user_email:
            if 'study_room_bookings' in i:
                print(f"- Room {i['study_room_bookings']['room_number']} on {i['study_room_bookings']['enter_date']} at {i['study_room_bookings']['enter_time']}")
        print()

    print(Fore.BLUE+'Thank you for using BookBuddy Library!')
    print(Style.RESET_ALL)
    print()

def sign_out_from_room():
    for index in list_of_users:
        if index['email']==user_email:
            if "study_room_bookings" in index:
                index['study_room_bookings']['room_number']=0
                index['study_room_bookings']['enter_date']=''
                index['study_room_bookings']['enter_time']=''
    user.save_users_file(list_of_users)
    user_room: int = int(input('Enter the room number: '))
    for room_booked in list_of_rooms:
        if room_booked['room_number']==user_room:
            room_booked['is_rented']=False
            room_booked['enter_time']=''
            room_booked['enter_date']=''
    room.save_rooms_file(list_of_rooms)
    print(Fore.GREEN+'process done successfully')
    print(Style.RESET_ALL)
    print()

def returning_a_book():
    for index in list_of_users:
        if index['email']==user_email:
            if 'rented_books' in index:
                index['rented_books']['title'] = ''
                index['rented_books']['due'] = ''
    user.save_users_file(list_of_users)
    user_book:str = input('Enter the book title you want to return: ')
    for return_book in list_of_books:
        if return_book['title']==user_book:
            return_book['availability']+=1
    book.save_books_file(list_of_books)
    print(Fore.GREEN+'process done successfully')
    print(Style.RESET_ALL)
    print()

print()
while True:
    try:
        print(f"Welcome Again {user_name}")
        print('Please Choose A Number From This Options:')
        print('1. Search/view books')
        print('2. Rent a book')
        print('3. Book a study room')
        print('4. View profile')
        print('5. To sign out from a room')
        print('6. To returning a book')
        print('7. Admin')
        print('8. Exit')
        user_choice:int = int(input('Enter Here Your Choice: '))
        if user_choice == 1:
            while True:
                try:
                    print('You want to "view" or "search" or "exit" ?')
                    user_choice2:str = input('Type here: ')
                    if user_choice2.lower() == 'search':
                        search_for_book()
                        break
                    elif user_choice2.lower() == 'view':
                        view_the_books()
                        break
                    elif user_choice2.lower() == 'exit':
                        print(Fore.YELLOW+'now you will go back to home page...')
                        print(Style.RESET_ALL)
                        break
                    else:
                        print('You Typed wrong option!')
                except Exception as e:
                    print(e)
        elif user_choice == 2:
            rent_book()
        elif user_choice == 3:
            booking_study_room(list_of_rooms)
        elif user_choice == 4:
            view_profile()
        elif user_choice == 5:
            sign_out_from_room()
        elif user_choice == 6:
            returning_a_book()
        elif user_choice == 7:
            if user_email == 'admin@admin.com':
                print()
                while True:
                    print('For adding a room press 1')
                    print('For adding a book press 2')
                    print('For editing a room press 3')
                    print('For editing a book press 4')
                    print('For exiting press 5')
                    admin_input:int = int(input('Type here: '))
                    if admin_input == 1:
                        room.add_room(list_of_rooms)
                        break
                    elif admin_input == 2:
                        book.add_book(list_of_books)
                        break
                    elif admin_input == 3:
                        admin_editing_room:int = int(input('Enter the room number: '))
                        for index in list_of_rooms:
                            if index['room_number']==admin_editing_room:
                                index['is_rented']=False
                        room.save_rooms_file(list_of_rooms)
                        print(Fore.GREEN+'Room Edited Successfully')
                        print(Style.RESET_ALL)
                        break
                    elif admin_input == 4:
                        admin_editing_book:str = input('Enter the book id: ')
                        for index in list_of_books:
                            if index['id']==admin_editing_book:
                                index['availability']+=1
                        book.save_books_file(list_of_books)
                        print(Fore.GREEN+'Book Edited Successfully')
                        print(Style.RESET_ALL)
                        break
                    elif admin_input == 5:
                        print('Exiting to Home Page...')
                        break
                    else:
                        print('You entered a wrong data.')
            else:
                print(Fore.YELLOW+'This Page For Admin Only!')
                print(Style.RESET_ALL)
        elif user_choice == 8:
            print(Fore.BLUE+'Thank you for using our program...')
            break
        else:
            print(Fore.RED+'Wrong Number, Please Enter Number between 1-4')
    except Exception as e:
        print(Fore.RED + e)