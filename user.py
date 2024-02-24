import json
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from art import*
from colorama import*

class User:

    def __init__(self, username=None,password = None ,email=None,name=None, age=None,bmr_calories = None, weight=None, height=None, gender=None,calories = None,fat=None, protein=None , carbs=None):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.calories = calories
        self.weight = weight
        self.height = height
        self.gender = gender
        self.protein =protein
        self.fat =fat
        self.carbs = carbs
        self.bmr_calories =bmr_calories
        
       

    def sign_up(self):
        username = input(Fore.BLUE+"Enter username: ")
        password = input(Fore.BLUE+"Enter password: ")
        name = input(Fore.BLUE+"Enter your name: ")
        age = int(input(Fore.BLUE+"Enter your age: "))
        weight = float(input(Fore.BLUE+"Enter your weight (in kg): "))
        height = float(input(Fore.BLUE+"Enter your height (in cm): "))
        option_gender = int(input(Fore.BLUE+"Enter your gender: \n1)women \n2)men\n"))
        if option_gender ==1:
            gender ="women"
        elif option_gender ==2:
            gender="men"
        else:
            print("Wrong choose , please enter 1 or 2 just")

        self.name = name
        self.username = username
        self.password = password
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.cal_calr = 0

        user_info = {
            "username": username,
            "password": password, 
            "name": name,
            "age": age, 
            "weight": weight, 
            "height": height, 
            "gender": gender
        }
      # Load existing data or create an empty dict
        try:
            with open("user_data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        # Ensure there's a "users" list, even if initially empty
        if "users" not in data:
            data["users"] = []

        # Add user data to the "users" list
        data["users"].append(user_info)

        # Save data to the JSON file
        with open("user_data.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Account created successfully!")

    def log_in(self):
        
        username = input(Fore.BLUE+"Enter username: ")
        password = input(Fore.BLUE+"Enter password: ")

    
        with open("user_data.json", "r") as f:
            data = json.load(f)
        user_found = False
        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                self.name = user["name"]
                self.age = user["age"]
                self.weight = user["weight"]
                self.height = user["height"]
                self.gender = user["gender"]
                user_found = True
                break
        if user_found:
            print("Login successful!")
        else:
            print("Invalid username or password.")



    
    def calculate_bmr_calories(self):
            self.bmr_calories = (10 * self.weight) + (6.25 * self.height ) - (5 * self.age) + 5
            return self.bmr_calories

    def calculate_bmi(self):
            self.bmi = self.weight / (self.height/100) ** 2
            if self.bmi > 50:
                category = "Overweight"
            elif self.bmi <= 45:
                category = "Normal weight"
            elif self.bmi < 40:
                category = "Underweight"
            else:
                category = "Obese"
            return category,round(self.bmi)


    def calculate_calories(self):
        goal =0
        option= int(input(Fore.LIGHTBLUE_EX+"choose your goal \n 1)lifestyle \n 2)lose weight \n 3)gain weight.\n"))
        if option == 1:
            goal='lifestyle'
        elif option == 2:
            goal='lose weight'
        elif option == 3:
            goal='gain weight'
        else:
            print("Invalid input. Please enter either '1' or '2' or '3'.\n")
            self.calculate_calories()

        
        try:
            self.bmr_calories= self.calculate_bmr_calories()
            if goal == "lifestyle":
                self.calories = self.bmr_calories
            elif goal == "lose weight":
                self.calories = self.bmr_calories - 500
            elif goal == "gain weight":
                self.calories = self.bmr_calories + 500
            else:
                print("Invalid goal specified.")
                return None
            return self.calories  
        except TypeError:
            print("Invalid input type.")
            return None 

    def check_diet(self):  
        answer = input(Fore.YELLOW+" Do you want dietary plan ? (yes/no): ")
        if answer == "yes":
            self.choose_diet_option()  # Call choose_diet_option directly
        elif answer == "no":
            print(exit)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.check_diet()  # Call check_diet recursively


    def choose_diet_option(self):  
        data =None
        with open("diet_plan.json", "r") as f:
            data = json.load(f)
        if(self.gender =="men"):
            men_calories = self.calories 
            print(men_calories)
            men_data = None
            for range_key, range_data in data['men'].items():
                min_calories, max_calories = map(int, range_key.split('-'))
                if min_calories <= men_calories <= max_calories:
                    men_data = range_data
                    break
            men_data_string = '\n'.join([f"{meal_type}: {', '.join(meals)}" for meal_type, meals in men_data.items()]) if men_data is not None else "No data available for men."
            print("Men's Data:")
            print(men_data_string)
        else:
            women_calories = self.calories 
            print(women_calories)
            women_data = None
            for range_key, range_data in data['women'].items():
                min_calories, max_calories = map(int, range_key.split('-'))
                if min_calories <= women_calories <= max_calories:
                    women_data = range_data
                    break
            women_data_string = '\n'.join([f"{meal_type}: {', '.join(meals)}" for meal_type, meals in women_data.items()]) if women_data is not None else "No data available for women."
            print("Women's Data:")
            print(women_data_string)

    def calculate_proten(self):
        self.protein = self.calories * 0.4
        return self.protein
    def calculate_carb(self):
        self.carbs = self.calories * 0.3
        return self.carbs
    def calculate_fat(self):
        self.fat = self.calories * 0.3
        return self.fat
        
    def showfig(self):
        calories_goal = 3000
        protein_goal = 180
        fat_goal = 80
        carbs_goal = 300
        protein_sum=self.calculate_proten()
        carbs_sum=self.calculate_carb()
        fat_sum=self.calculate_fat()
        fig, axs = plt.subplots(1, 2)  # Create a figure with 1 row and 2 columns

        axs[0].pie([protein_sum, fat_sum, carbs_sum], labels=["Protein", "Fat", "Carbs"], autopct="%1.1f%%")
        axs[0].set_title("Macronutrients Distribution")

        axs[1].bar([0, 1, 2], [protein_sum, fat_sum, carbs_sum], width=0.4)
        axs[1].bar([0.5, 1.5, 2.5], [protein_goal, fat_goal, carbs_goal], width=0.4)
        axs[1].set_title("Macronutrients Progress")

        fig.tight_layout()  # Adjust spacing between figures
        plt.show()





