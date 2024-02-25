from distance import getDistance
from weather import getWeather
from currency import currencyExchange
from transportaions import availabiltyTrans
from histo import historicalPlaces
from check import checkValidStr
from check import checkValidInt
from websites import websites


print("**************************************************")
print(" Welcome to Your Ultimate Guide in Saudi Arabia!🐪")
print("**************************************************\n")
while True : 
    print("Our Services:")
    print('''
1. Distance Calculation Between Two Cities 
2. Get current Weather information for a specific city 
3. Currency Exchange 
4. Transportations Availability 
5. Explore Historical places in Saudi Arabia 
6. Websites And Applications To Enhance Your Journey!
7. To Exit the Program!''')
    
    while True:
            userinput = input("Access any Service By Entering The Corresponding Number Next To It! :")
            choice = checkValidInt(userinput,7)
            if type(choice) == int:
                break
    print("\n")
    if choice == 1 : 
            print("*****************************************************")
            print("    Welcome to our Distance Calculation Service! 🗺️   ")
            print("*****************************************************\n")
            print("Let's plan your journey!")
            getDistance()

    elif choice == 2:
        print("*****************************************************")
        print("          Welcome To Our Weather Service! 🌦️         ")
        print("*****************************************************\n")
        getWeather()
        
    elif choice == 3:
        print("*****************************************************")
        print("    Welcome to our Currency Exchange Service!💵     ")
        print("*****************************************************\n")
        currencyExchange() 

    elif choice == 4:
        print("*****************************************************")
        print("Welcome To Our Transportaions Availability Service!🚈")
        print("*****************************************************\n")
        availabiltyTrans()

    elif choice == 5:
        print("*****************************************************")
        print("      Welcome To Our Historical Places Service! 📜   ")
        print("*****************************************************\n")
        historicalPlaces()
        
    elif choice == 6:
        websites()
    
    elif choice == 7:
        break  





