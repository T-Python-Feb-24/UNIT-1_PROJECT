from art import *
import os
import time

class colors:
    
    BWHITE = '\033[7m'
    BGREEN = '\x1b[3;30;42m'
    BRED = '\x1b[3;31;41m'
    GREY = '\033[30m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
    GBU = '\33[92m\33[1m\33[4m' #GREEN + BOLD + UNDERLINE
    BBU = '\33[94m\33[1m\33[4m' #BLUE  + BOLD + UNDERLINE
    YBU = '\33[93m\33[1m\33[4m' #YELLOW + BOLD + UNDERLINE   
    YBI = '\33[93m\33[1m\33[3m' #YELLOW + BOLD + ITALIC
    RBI = '\33[91m\33[1m\33[3m' #RED + BOLD + ITALIC
    BREDB = '\x1b[3;31;41m\33[1m' #RED Background + BOLD
    YB = '\33[93m\33[1m'

    #TEST = '\x1b[0;30;40m'
#print(colors.TEST+" WELCOME TO World "+colors.RESET)


    def animate_text(text):
        number_of_characters=1
        while True:
            print("\n")
            print(text[0:number_of_characters])
            number_of_characters += 1
            if number_of_characters > len(text):
                number_of_characters = 0
            time.sleep(0.1)
            os.system('clear')
    
    def intro():
        print(colors.RBI)
        tprint('''HOTEL BOOKING
            PROJECT''', font="varsity")
        print(colors.RESET)

        input()

        print(f"{colors.BBU}OVERVIEW{colors.RESET}")
        print(colors.GREY + '''This is a simple hotel booking system that allows users to make reservations for rooms in the hotel.
    The user will be able to:
        \4 Choose an option from main menu .
        \4 Search for hotel by city name and get list of hotels with their details .
        \4 Make reservations for one or more nights in a room .
        \4 View the total cost of reserved room .''' + colors.RESET)