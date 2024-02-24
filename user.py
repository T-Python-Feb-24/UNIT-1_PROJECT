import json

class User:
    def load_user_data(user_data):
        try:
            with open("user_data.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_user_data(user_data):
        with open("user_data.json", "w", encoding="utf-8") as file:
            json.dump(user_data, file, indent=2)
