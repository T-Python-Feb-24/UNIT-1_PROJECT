import colorama
from registeration import Register , Login
from art import *
from colorama import *
from cfonts import render




colorama.init(autoreset=True)

output = render('Welcom', colors=['green', 'white'], align='center')
to = render('To', colors=['white', 'white'], align='center')
kih = render('Keep  It  Healthy \n\n\n\n', colors=['green', 'white'], align='center')
about_us=text2art('About us \n\n',"fancy135").center(140)
about=text2art('We aim  to improve your health through healthy nutrition diet\n\n',"fancy135").center(140)
about_=text2art('By adjusting your minerals in your diet \n\n\n',"fancy135").center(140)

join=render("Join us now\n\n\n",colors=['white', 'green'], align='center',font='tiny')
x=text2art('> 1.To register with us \n',"fancy135").center(140)
a=text2art('> 2.To login\n',"fancy135").center(140)
ex=text2art('> 3.Exit\n',"fancy135").center(140)
z=text2art('> Please choose : \n',"fancy135").center(140)
b=text2art('Enter your username: (Note.Enter Letters only )\n\n',"fancy135").center(140)
c=text2art('Enter the password: (Note.Enter Numbers only)\n\n',"fancy135").center(140)
d=text2art('Please confirm the password :\n',"fancy135").center(140)
e=text2art('Enter your username : \n\n',"fancy135").center(140)
f=text2art('Enter the password :\n\n',"fancy135").center(140)
g=text2art('Error, wrong input!\n',"fancy135").center(140)
invinput=text2art('Invalid username or password input\n',"fancy135").center(140)
bye=text2art('"Goodbye~"\n',"fancy135").center(140)




#Login menu
print(decor("fancy5",both=True)*9)
print("\n\n\n")
print(output)
print(to)
print(kih)
print("\n\n\n")
print(decor("fancy5",both=True)*9)
print("\n\n\n\n\n")
print(Fore.LIGHTGREEN_EX +about_us)
print("\n\n")
print(about)
print(about_)
print(join)
print("\n\n\n")
print(decor("fancy5",both=True)*9)
print("\n\n\n")


while True:
    try:
        print(Fore.LIGHTGREEN_EX +x)
        print(Fore.LIGHTGREEN_EX +a)
        print(Fore.LIGHTGREEN_EX +ex)

        reg_or_login = input(z)

        if reg_or_login == '1':
            try:
                username=str(input(Fore.LIGHTGREEN_EX +b))
                password=int(input(Fore.LIGHTGREEN_EX +c))
                conpass=int(input(Fore.LIGHTGREEN_EX +d))
                Register(username ,password,conpass)
            except ValueError:
                print(Fore.LIGHTRED_EX +invinput)

        elif reg_or_login == '2':
            try:
                username=str(input(Fore.LIGHTGREEN_EX +e))
                password=int(input(Fore.LIGHTGREEN_EX +f))
                Login(username ,password)

            except ValueError:
             print(Fore.LIGHTRED_EX +invinput)

        elif reg_or_login == '3':
            try:
                print(bye)
                break

            except ValueError:
             print(Fore.LIGHTRED_EX +invinput)

        else:
            print(g)
    except Exception as e :
        print(e)


