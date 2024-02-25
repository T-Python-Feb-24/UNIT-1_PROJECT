import json
from msilib.schema import AdminUISequence

class Admin:
    
    class Admin:
        def __init__(self, username, password):
            self.username = username
            self.password = password

    def save_admins_to_json(self, filename):
        admins = [{"username": self.username, "password": self.password}]
        with open(filename, "w") as f:
            json.dump(admins, f)
    def admin (request):
        

        AdminUISequence.save_admins_to_json("admins_data.json")



def load_admins_from_json(filename):
        try:
            with open(filename, 'r') as f:
                Admin.admins = json.load(f)
        except FileNotFoundError:
            Admin.admins = []

# Save admins to JSON file
Admin.save_admins_to_json("admins_data.json")

# Load admins from JSON file
Admin.load_admins_from_json("admins_data.json")