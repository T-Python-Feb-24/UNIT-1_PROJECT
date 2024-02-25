from gift_card_system import GiftCardSystem
gift_card_system = GiftCardSystem()
def buy_a_gift_card():
    inventory = [
    {"id": 1, "name": "Google Play $10", "platform": "Google Play", "value": 10, "points": 5},
    {"id": 2, "name": "Google Play $25", "platform": "Google Play", "value": 25, "points": 10},
    {"id": 3, "name": "Apple $15", "platform": "Apple", "value": 15, "points": 7},
    {"id": 4, "name": "Apple $50", "platform": "Apple", "value": 50, "points": 20},
    {"id": 5, "name": "Amazon $20", "platform": "Amazon", "value": 20, "points": 8},
    {"id": 6, "name": "Amazon $100", "platform": "Amazon", "value": 100, "points": 40}
    ]

    while True:
        print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Name", "Platform", "Value", "Points"))
        print("----------------------------------------------------------")
        for item in inventory:
            print("{:<5} {:<20} {:<15} ${:<10} {:<10}".format(item["id"], item["name"], item["platform"], item["value"], item["points"]))

        choice = input("Enter the ID of the gift card you want to select (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        else:
            try:
                choice_id = int(choice)
                selected_item = next((item for item in inventory if item["id"] == choice_id), None)
                if selected_item:
                    gift_card_id = gift_card_system.generate_gift_card(selected_item["value"], selected_item["points"])
                    print("\n----------------------------------------------------------")
                    print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Name", "Platform", "Value", "Points"))
                    print("----------------------------------------------------------")
                    print("{:<5} {:<20} {:<15} ${:<10} {:<10}".format(selected_item["id"], selected_item["name"], selected_item["platform"], selected_item["value"], selected_item["points"]))
                    print("---------------------------------------------------------------")
                    print("Code: ", gift_card_id) 
                    print("---------------------------------------------------------------")
                    customer_menu()  
                else:
                    print("--------------------------------------------------")
                    print("Invalid ID. Please try again.")
                    print("--------------------------------------------------")
            except ValueError:
                print("--------------------------------------------------")
                print("Invalid input. Please enter a valid ID.")
                print("--------------------------------------------------")

def customer_menu():
    while True:
        print("1. Buy a Gift Card")
        print("2. Check Gift Card Balance")
        print("3. Show Purchase History")
        print("4. Show Total Points")
        print("5. Redeem Points")
        print("Enter the ID of the gift card you want to select (or 'q' to quit)")

        choice = input("Enter your choice: ")

        if choice == '1':
            buy_a_gift_card()  
        elif choice == '2':
            gift_card_id = input("Enter the gift card ID: ")
            try:
                balance = gift_card_system.check_balance(gift_card_id)
                if balance is not None:
                    print("--------------------------------------------------")
                    print("\nGift card balance:")
                    print("--------------------------------------------------")
                    print("{:<40} {:<10}".format("Gift Card ID", "Balance"))
                    print("--------------------------------------------------")
                    print("{:<40} {:<10}".format(gift_card_id, balance["value"]))
                    print("--------------------------------------------------")
                else:
                    print("--------------------------------------------------")
                    print("Gift card not found.")
                    print("--------------------------------------------------")
            except KeyError:
                print("--------------------------------------------------")
                print("Invalid gift card ID.")
                print("--------------------------------------------------")
        elif choice == '3':
            purchase_history = gift_card_system.get_purchase_history()
            print_purchase_history(purchase_history)
        elif choice == '4':
            print("--------------------------------------------------")
            print(f"Total Points | {gift_card_system.total_points}")
            print("--------------------------------------------------")
        elif choice == '5':
            print("--------------------------------------------------")
            print(f"Your Have Total Points | {gift_card_system.total_points}")
            print("--------------------------------------------------")
            
            gift_card_system.redeem_points()

                
        elif choice == 'q':
            break
        else:
            print("--------------------------------------------------")
            print("Invalid choice. Please try again.")
            print("--------------------------------------------------")

def print_purchase_history(purchase_history):
    if not purchase_history:
        print("--------------------------------------------------")
        print("No purchase history available.")
        print("--------------------------------------------------")
    else:
        print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Name", "Platform", "Value", "Code"))
        print("------------------------------------------------------------------------------------")
        for entry in purchase_history.values():
            print("{:<5} {:<20} {:<15} ${:<10} {:<10}".format(entry["ID"], entry["Name"], entry["Platform"], entry["Value"], entry["code"]))
        print("------------------------------------------------------------------------------------")
            
def main():
    print("\nWelcome to the Gift Card Management System!")
    print("--------------------------------------------------")
    username = input("username: ")
    password = input("password: ")
    customer_menu()
if __name__ == "__main__":
    main()
