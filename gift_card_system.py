import uuid

class GiftCardSystem:
    def __init__(self):
        self.gift_cards = {}
        self.purchase_history = {}  
        self.total_value = 0  
        self.total_points  = 0

    def generate_gift_card(self, value, points):
        gift_card_id = str(uuid.uuid4())
        self.gift_cards[gift_card_id] = {"value": value, "points": points}
        self._update_purchase_history(value, gift_card_id)
        return gift_card_id

    def view_gift_cards(self):
        return self.gift_cards

    def check_balance(self, gift_card_id):
        return self.gift_cards.get(gift_card_id)

    def _update_purchase_history(self, purchase_amount, code):
        self.total_value += purchase_amount  
        self.total_points += purchase_amount  
        card_id = len(self.purchase_history) + 1
        self.purchase_history[card_id] = {"ID": card_id,
                                          "Name": "Gift Card",
                                          "Platform": "Generic",
                                          "Value": purchase_amount,
                                          "code": code,
                                          "total_value": self.total_value}  


    def get_purchase_history(self):
        return self.purchase_history
    
    
    def redeem_points(self):
        if self.total_value > 200:
            print("--------------------------------------------------")
            points = int(input("Enter the number of points you want to redeem: "))
            if points <= self.total_points:
                gift_card_id = self.generate_gift_card(points, points)
                self.total_points -= points
                print("--------------------------------------------------")
                print(f"You have redeemed {points} points! Gift card ID: {gift_card_id}")
                print("--------------------------------------------------")
            else:
                print("--------------------------------------------------")
                print("Insufficient points. Please try again with fewer points.")
                print("--------------------------------------------------")
        else:
            print("--------------------------------------------------")
            print("You cannot redeem points at the moment. Total value must exceed 200.")
            print("--------------------------------------------------")
