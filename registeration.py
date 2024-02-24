
import json
from admin_menu import admin_add_search_list
from user_menu import userchoises

a=("> Account created!\n").center(140)
b=("> Invalid username or password. Try again!\n").center(140)
c=("> Error, passwords dose not match\n").center(140)

def Register(username ,password,confirm_password ):
    
    while True:
        admin=False
        ulist={"name":username , "pass":confirm_password , "admin":admin}
        if password == confirm_password:
         try:
            with open("usernames.json", "a") as file:
                  file.seek(0)
                  json.dump(ulist, file)
                  file.write("\n")
                  print(a)
                  break

         except json.JSONDecodeError as e :
            print(e)
        elif password != confirm_password:
            print(c)
            continue
    

def Login(username ,password1):
    global ulist
    while True:
        with open("usernames.json", "r") as file:
            ulist = [json.loads(line) for line in file]

        if any(user["name"] == username and user["pass"] == password1 and user["admin"] == False for user in ulist):
            print("")
            userchoises()
            break
        elif any(user["name"] == username and user["pass"] == password1 and user["admin"] == True for user in ulist):
            print(" ")
            admin_add_search_list()
            break
        else:
            print(b)
            break


