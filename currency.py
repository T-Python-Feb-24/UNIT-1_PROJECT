import requests
from api_keys import currency_api_key
from check import checkValidResponse
from check import checkValidCurr
from check import checkValidInt
from termcolor import colored

def currencyExchange():
    while True:
        user_input = input(colored("Enter the amount you want to exchange with its currency (e.g., 20 USD), separated by a space.: " ,'red'))
        input_values = user_input.split()
        if len(input_values) != 2:
            print(colored("Invalid input. Please provide the amount and currency, separated by a space.",'red'))
            continue
        
        amount, base_curr = input_values
        if not amount.isnumeric():
            print("Enter Valid Number!")
            continue
        if not checkValidCurr(base_curr):
            continue
        
        while True:
            target_curr = input("Enter Tagret Currency : ")
            if not checkValidCurr(target_curr):
                continue
            break

        url = "https://v6.exchangerate-api.com/v6/{0}/pair/{1}/{2}/{3}".format(currency_api_key, base_curr, target_curr, amount)
        if not checkValidResponse(url):
            print(colored("Something went wrong please try again later",'red'))
            continue

        response = checkValidResponse(url)
        jsn_response = response.json()
        result = jsn_response["conversion_result"]
        print(f"{user_input} = {result} {target_curr}")
       
        while True:
            end_input = input("\nTo Exchange Currency For Another Amount, press 1\nTo Exit The Currency Exchange Service, press 2:" )
            print("")
            option = checkValidInt(end_input, 2)
            if type(option) == int:
                break
        if option == 1:
            currencyExchange()
        elif option == 2:
            print("Thank You For using Our Currency Exchange Service 💵\n")
            return
        return