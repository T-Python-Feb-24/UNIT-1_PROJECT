import json
from user import User

def load_data(admin):
    try:
        with open("car_data.json", "r", encoding="utf-8") as file:
            cars = json.load(file)
            return cars
    except:
        return []

class Dealership:
    def __init__(self, name, admin_username, admin_password):
        self.name = name
        self.admin = Admin(admin_username, admin_password)
        self.inventory = load_data(self.admin)
        self.sold_cars = []
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_credentials(self, username, password):
        return self.username == username and self.password == password

    def sell_car(self, car, buyer, payment_method, installment_period=None):
        # Implement the selling logic here
        print(f"Sold {car} to {buyer} via {payment_method} payment method.")
        if payment_method == "installment":
            print(f"Installment period: {installment_period} months")

    def calculate_monthly_payment(self, loan_amount, annual_interest_rate, loan_term, monthly_interest_rate, monthly_payment ):
            loan_amount = float(input("Enter the loan amount: "))
            annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
            loan_term = int(input("Enter the loan term in months: "))
            monthly_interest_rate = annual_interest_rate / 12 / 100
            monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** - loan_term)
            print(f"Monthly payment: ${monthly_payment:.2f}")

    def load_cars(self, cars):
            self.inventory = cars

    def sell_car(self, car, buyer, payment_method, installment_period=None):
        # Implement the selling logic here
        print(f"Sold {car} to {buyer} via {payment_method} payment method.")
        if payment_method == "installment":
            print(f"Installment period: {installment_period} months")
        dealership = Dealership("ABC Motors")
                
    def save_sold_cars(self):
            with open(self.sold_cars_file, "w") as f:
                json.dump(self.sold_cars, f)