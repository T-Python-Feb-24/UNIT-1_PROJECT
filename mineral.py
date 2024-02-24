from add_search import zinc_list,iron_list,copper_list,potassium_list
from art import *
from cfonts import render
from colorama import *




mzinc=render("High zinc menu\n",colors=['green', 'white'], align='center',font='tiny')
lzinc=render("Low zinc menu\n",colors=['green', 'white'], align='center',font='tiny')
hiron=render("High iron menu \n",colors=['green', 'white'], align='center',font='tiny')
liron=render("Low iron menu\n ",colors=['green', 'white'], align='center',font='tiny')
hcopper=render("High copper menu \n",colors=['green', 'white'], align='center',font='tiny')
lcopper=render("low copper menu \n",colors=['green', 'white'], align='center',font='tiny')
hpotassium=render("High potassium menu\n ",colors=['green', 'white'], align='center',font='tiny')
lpotassium=render("low potassium menu \n",colors=['green', 'white'], align='center',font='tiny')

helthyzinc=text2art("\nYour zinc leve is on normall levels , Keep it healthy\n","fancy135").center(140)
helthyiron=text2art("\nYour iron leve is on normall levels , Keep it healthy\n","fancy135").center(140)
helthycopper=text2art("\nYour copper leve is on normall levels , Keep it healthy\n","fancy135").center(140)
helthypotassium=text2art("\nYour potassium leve is on normall levels , Keep it healthy\n","fancy135").center(140)

z=text2art('Do you want a list of food of this level :\n \n',"fancy135").center(140)
a=text2art("Your zinc level is high , please be aware\n","fancy135").center(140)
aa=text2art("Your zinc leve is low , please be carefull\n","fancy135").center(140)

b=text2art('Your iron level is high , please be aware\n',"fancy135").center(140)
c=text2art('Your iron level is low , please be carefull\n',"fancy135").center(140)

d=text2art('Your copper level is high , please be aware\n',"fancy135").center(140)
e=text2art('Your copper level is low , please be carefull \n',"fancy135").center(140)

f=text2art('Your potassium level is high , please be aware\n',"fancy135").center(140)
g=text2art('Your potassium level is low , please be carefull\n',"fancy135").center(140)

yorn=text2art("y/yes n/no : \n\n","fancy135").center(140)
inv=text2art("invalid input \n","fancy135").center(140)
line=text2art("--------------------------------------------- \n","fancy135").center(140)

#Functions to caculate the user minerals levels 

def zinc (amount:float ):
        while True :
                if amount > 22 :
                    print("\n")
                    print(Fore.LIGHTRED_EX+a)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                         print(decor("fancy5",both=True)*4)
                         print("\n\n\n")
                         print(mzinc)
                         zinc_list("high")
                         print(decor("fancy5",both=True)*4)
                         print("\n\n\n")
                    elif yes_no == "n":
                       print("")
                    else:
                     raise Exception(Fore.RED+inv)
                elif amount < 13 :
                    print("\n")
                    print(Fore.LIGHTBLUE_EX+aa)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     print(lzinc)
                     zinc_list("low")
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                    elif yes_no == "n":
                        print("")
                        
                    else:
                     raise Exception(Fore.RED+inv)

                elif amount <= 22 and amount >= 13 :
                    print("\n")
                    print(Fore.GREEN+ helthyzinc)
                    print("\n")
                    print(decor("fancy5",both=True)*4)
                    print("\n\n\n")
                    
                else:
                 raise Exception(Fore.RED+inv)
                break

    
        



def iron ( amount:float):
        while True :
                if amount > 16 :
                    print("\n")
                    print(Fore.LIGHTRED_EX+b)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     print(hiron)
                     iron_list("high")
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                    elif yes_no == "n":
                        print("")
                        
                    else:
                     raise Exception(Fore.RED+inv)

                elif amount < 13 :
                    print("\n")
                    print(Fore.LIGHTBLUE_EX+c)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     print(liron)
                     iron_list("low")
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                    elif yes_no == "n":
                        print("")
                    else:
                     raise Exception(Fore.RED+inv)

                elif amount <= 16 and amount >= 13 :
                    print("\n")
                    print(Fore.GREEN+helthyiron)
                    print("\n")
                    print(decor("fancy5",both=True)*4)
                    print("\n\n\n")
                    
                else:
                 raise Exception(Fore.RED+inv)
                break
    



def copper (amount:float):
        while True :
                if amount> 140 :
                    print("\n")
                    print(Fore.LIGHTRED_EX+d)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     print(hcopper)
                     copper_list("high")
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                    elif yes_no == "n":
                        print("")
                    else:
                     raise Exception(Fore.RED+inv)

                elif amount < 70 :
                    print("\n")
                    print(Fore.LIGHTBLUE_EX+e)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     print(lcopper)
                     copper_list("low")
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                    elif yes_no == "n":
                        print("")
                    else:
                     raise Exception(Fore.RED+inv)

                elif amount <= 140 and amount >= 70 :
                    print("\n")
                    print(Fore.GREEN+helthycopper)
                    print("\n")
                    print(decor("fancy5",both=True)*4)
                    print("\n\n\n")
                    
                    break
                else:
                 raise Exception(Fore.RED+inv)
                break
    

def potassium (amount:float):
        while True :
                if amount> 5.3 :
                    print("\n")
                    print(Fore.LIGHTRED_EX+f)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     print(hpotassium)
                     potassium_list("high")
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                    elif yes_no == "n":
                        print("")
                    else:
                     raise Exception(Fore.RED+inv)

                elif amount < 3.6 :
                    print("\n")
                    print(Fore.LIGHTBLUE_EX+g)
                    print(Fore.LIGHTGREEN_EX+z)
                    yes_no = input(yorn).lower()
                    if yes_no == "y":
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     print(lpotassium)
                     potassium_list("high")
                     print(decor("fancy5",both=True)*4)
                     print("\n\n\n")
                     
                    elif yes_no == "n":
                        print("")
                    else:
                     raise Exception(Fore.RED+inv)

                elif amount <= 5.3 and amount >= 3.6 :
                    print("\n")
                    print(Fore.GREEN+helthypotassium)
                    print("\n")
                    print(decor("fancy5",both=True)*4)
                    print("\n\n\n")
                    
                else:
                 raise Exception(Fore.RED+inv)
                break
        