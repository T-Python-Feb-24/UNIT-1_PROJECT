import requests
from requests.exceptions import ConnectionError
from termcolor import colored


def checkValidInt(int_number: int, max_number: int):
    try:
        int_number = int(int_number)
    except:
        print(colored("invalid input, please make sure to enter an integer number!",'red'))
        return None

    if int_number <= 0 or int_number > max_number:
        print(colored(f"Invalid Number, Please Enter Any number from 1 to {max_number}",'red'))
        return None
    else:
        return int_number


def checkValidStr(str_value):
    if not str_value.isalpha():
        print(colored("invalid input, plase make sure to enter a string value!",'red'))
        return False
    else:
        return str_value


def checkValidCurr(curr: str):
    if not curr.isalpha():
        print(colored("Please Enter Vlid currency value",'red'))
        return None

    elif len(curr) != 3:
        print(colored("Please Enter Vlid currency value",'red'))
        return None
    else:
        return curr


def checkValidResponse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        return
    except ConnectionError:
        print(colored("check your internet connection",'red'))
