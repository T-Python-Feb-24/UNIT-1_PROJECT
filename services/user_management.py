import json
class UserManagement:
    def __init__(self) -> None:
        self.__list_of_users = self.read_users_file()

    def get_list_of_users(self):
            return self.__list_of_users
        
    def read_users_file(self):
            try:
                with open('users.json', mode='r', encoding='utf-8') as file:
                    list_of_users = json.loads(file.read())
                    return list_of_users
            except FileNotFoundError:
                return []

    def save_users_file(self, list_of_users):
            with open('users.json', mode='w', encoding='utf-8') as file:
                users_file_contents = json.dumps(list_of_users)
                file.write(users_file_contents)
    
    def add_user(self, list_of_users):
        new_user:dict = {
            }
        self.__list_of_users.append(new_user)
        self.save_users_file(self.__list_of_users)
    
    