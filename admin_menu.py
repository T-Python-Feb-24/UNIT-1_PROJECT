from add_search import *
from cfonts import render
from art import *
from colorama import *
import colorama

colorama.init(autoreset=True)

main=render("Main menu\n\n\n",colors=['white', 'white'], align='center',font='tiny')
wba=render("Welcom back admin\n\n",colors=['green', 'white'], align='center',font='tiny')
addm=render("Add menu\n",colors=['green', 'white'], align='center',font='tiny')
sm=render("Search menu \n",colors=['green', 'white'], align='center',font='tiny')
sz=render("Search in zinc\n",colors=['green', 'white'], align='center',font='tiny')
si=render("Search in iron\n",colors=['green', 'white'], align='center',font='tiny')
sc=render("Search in copper\n",colors=['green', 'white'], align='center',font='tiny')
sp=render("Search in potassium\n",colors=['green', 'white'], align='center',font='tiny')
dlm=render("Delete menu \n",colors=['green', 'white'], align='center',font='tiny')
dlz=render("Delete from zinc list \n",colors=['green', 'white'], align='center',font='tiny')
dli=render("Delete from iron list\n",colors=['green', 'white'], align='center',font='tiny')
dlc=render("Delete from copper list\n",colors=['green', 'white'], align='center',font='tiny')
dlp=render("Delete from potassium list \n",colors=['green', 'white'], align='center',font='tiny')

x=text2art('Choose which chois would you do :\n\n',"fancy135").center(140)
a=text2art('1.To add new food list:\n\n',"fancy135").center(140)
z=text2art('2.To search in food list:\n \n',"fancy135").center(140)
dell=text2art('3.To delete from food list: \n\n\n',"fancy135").center(140)
b=text2art('4.LogOut:\n',"fancy135").center(140)

cc=text2art('> Enter your chois here :\n',"fancy135").center(140)

d=text2art('Choose which list would you add new elemnts in :\n',"fancy135").center(140)
e=text2art('1.Add to zinc list \n',"fancy135").center(140)
f=text2art('2.Add to iron list\n',"fancy135").center(140)
g=text2art('3.Add to copper list\n',"fancy135").center(140)
h=text2art('4.Add to potassium list\n',"fancy135").center(140)
i=text2art('5.Exit\n',"fancy135").center(140)

j=text2art('Enter food name : \n',"fancy135").center(140)
l=text2art('Enter grams per meal :\n',"fancy135").center(140)
p=text2art('Enter calories per grams :\n',"fancy135").center(140)
v=text2art('which level .ex: high or low :\n',"fancy135").center(140)

kk=text2art('> To back to the main menu press enter \n',"fancy135").center(140)

sl=text2art('Choose which list would you search in :\n',"fancy135").center(140)
zl=text2art('1.Zinc list \n',"fancy135").center(140)
il=text2art('2.Iron list  \n',"fancy135").center(140)
cl=text2art('3.Copper list \n',"fancy135").center(140)
pl=text2art('4.Potassium list  \n',"fancy135").center(140)

dl=text2art('Choose which list would you delete from :\n',"fancy135").center(140)

lev=text2art('Enter the level :\n',"fancy135").center(140)
bac=text2art('You back to main menu\n',"fancy135").center(140)
gby=text2art('Goodbey~ . See you soon\n',"fancy135").center(140)
line=text2art("--------------------------------------------- \n","fancy135").center(140)
ii=text2art("invalid input\n","fancy135").center(140)




#Admin main menu 

def admin_add_search_list():

 while True:
   print(decor("fancy5",both=True)*9)
   print("\n\n\n")
   
   print(wba)
   print(main)
   print("\n\n")
   print(x)
   print(Fore.LIGHTGREEN_EX+a)
   print(Fore.LIGHTGREEN_EX+z)
   print(Fore.LIGHTGREEN_EX+dell)
   print(b)
   print()
   Choice = input(cc)
   print("")
   match Choice :
     #case to add food list 
     case "1":
       while True:
        print(decor("fancy5",both=True)*9)
        print("\n\n\n")
        print(addm)
        print("\n\n")
        print(d)
        print("\n")
        print(Fore.LIGHTGREEN_EX+e)
        print(Fore.LIGHTGREEN_EX+f)
        print(Fore.LIGHTGREEN_EX+g)
        print(Fore.LIGHTGREEN_EX+h)
        print("\n\n")
        print(i)
        c=input(cc)
        print("")
        match c :
          case "1":
            try:
              print(decor("fancy5",both=True)*9)
              print("\n\n\n")
              name=str(input(j))
              grams=int(input(l))
              calories=int(input(p))
              level=str(input(v))
              add_to_zinc(name,grams,calories,level)
            except ValueError:
              print(ii)
            
            input(kk)
          case "2":
            try:
              print(decor("fancy5",both=True)*9)
              print("\n\n\n")
              name=str(input(j))
              grams=int(input(l))
              calories=int(input(p))
              level=str(input(v))
              add_to_iron(name,grams,calories,level)
            except ValueError:
              print(ii)
          
            input(kk)
          case "3":
            try:
              print(decor("fancy5",both=True)*9)
              print("\n\n\n")
              name=str(input(j))
              grams=int(input(l))
              calories=int(input(p))
              level=str(input(v))
              add_to_copper(name,grams,calories,level)
            except ValueError:
              print(ii)
            input(kk)
        
          case "4":
            try:
              print(decor("fancy5",both=True)*9)
              print("\n\n\n")
              name=str(input(j))
              grams=int(input(l))
              calories=int(input(p))
              level=str(input(v))
              add_to_potassium(name,grams,calories,level)
            except ValueError:
              print(ii)
            input(kk)
          
          case "5":
            print(bac)
            break
          
     case "2":
      while True:
        print(decor("fancy5",both=True)*9)
        print("\n\n\n")
        print(sm)
        print("\n\n\n")
        print(sl)
        print("\n")
        print(Fore.LIGHTGREEN_EX+zl)
        print(Fore.LIGHTGREEN_EX+il)
        print(Fore.LIGHTGREEN_EX+cl)
        print(Fore.LIGHTGREEN_EX+pl)
        print("\n\n")
        print(i)
        w=input(cc)
        match w :
          case "1":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(sz)
           level=input(lev)
           name=input(j)
           print(search_in_zinc(level,name))
           input(kk)
          case "2":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(si)
           level=input(lev)
           name=input(j)
           print(search_in_iron(level,name))
           input(kk)
          case "3":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(sc)
           level=input(lev)
           name=input(j)
           print(search_in_copper(level,name))
           input(kk)
          case "4":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(sp)
           level=input(lev)
           name=input(j)
           print(search_in_potassium(level,name))
           input(kk)

          case "5":
           print(bac)
           break
      
     case "3":
       print("\n")
       print(decor("fancy5",both=True)*9)
       print("\n\n\n")
       print(dlm)
       print("\n\n\n")
       print(dl)
       print("\n")
       print(Fore.LIGHTGREEN_EX+zl)
       print(Fore.LIGHTGREEN_EX+il)
       print(Fore.LIGHTGREEN_EX+cl)
       print(Fore.LIGHTGREEN_EX+pl)
       print("\n\n")
       print(i)
       dchois=input(cc)
       match dchois:
         case"1":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(dlz)
           name=input(j)
           level=input(lev)
           delete_from_zinc(name,level)
           input(kk)
         case"2":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(dli)
           name=input(j)
           level=input(lev)
           delete_from_iron(name,level)
           input(kk)
         case"3":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(dlc)
           name=input(j)
           level=input(lev)
           delete_from_copper(name,level)
           input(kk)
         case"4":
           print("\n")
           print(decor("fancy5",both=True)*9)
           print("\n\n\n")
           print(dlp)
           name=input(j)
           level=input(lev)
           delete_from_potassium(name,level)
           input(kk)
         case"5":
           print(bac)
           


     case "4":
      print(gby)
      break
     


