# %%
import hashlib
import json
import os


class Login:
    def get_user_by_user_name(self, user_name:str):
        if os.path.exists("users.json"):
            with open('users.json', 'r') as f:
                users = json.load(f)
            for user in users:
                if user['user_name'] == user_name.lower():
                    return user
        return None

    def create_user(self, user_name:str, password:str):
        hashed_password: str = hashlib.sha256(password.encode()).hexdigest()
        user: dict[str] = {'user_name': user_name, 'password': hashed_password}
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []
        users.append(user)
        with open('users.json', 'w') as f:
            json.dump(users, f)

    def login(self, user_name, password) -> bool:
        user = self.get_user_by_user_name(user_name)
        if user:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == user['password']:
                print(f"Login as {user_name} successful.")
                return True
        print("Invalid user_name or password.")
        return False


def main():
    user_name = input("Enter your user_name: ")
    password = input("Enter your password: ")

    user = Login().login(user_name, password)

    if user:
        print("Login successful.")
        # Keep the user's credentials until the app exits
        while True:
            # Use the user object to authenticate subsequent requests
            # ...
            pass
    else:
        print("Invalid user_name or password.")


if __name__ == "__main__":
    main()
