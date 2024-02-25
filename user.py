class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def check_credentials(self, entered_first_name, entered_last_name):
        if self.first_name == entered_first_name and self.last_name == entered_last_name:
            return True
        else:
            return False

# Create a user object
user = User("Abdulaziz", "112233")

# Check the user's credentials
if user.check_credentials("Abdulaziz", "112233"):
    print("Credentials are correct")
else:
    print("Credentials are incorrect")