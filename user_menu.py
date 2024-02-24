from mineral import zinc,iron,copper,potassium
from racipes import recipe_list
from yarl import URL 
from cfonts import render
from art import *
from colorama import *

#URLs for each recipe

one=URL("https://www.ambitiouskitchen.com/roasted-veggie-chickpea-pesto-quinoa-salad/").host
tow=URL("https://www.mccormick.com/grill-mates/recipes/main-dishes/grilled-salmon-and-asparagus-foil-packets").host
three=URL("https://www.bettycrocker.com/recipes/stuffed-peppers/63e29e18-903e-467c-aec5-fba4ce3a138f").host
four=URL("https://www.mccormick.com/recipes/salads-sides/stir-fry-vegetables").host
five=URL("https://foolproofliving.com/layered-yogurt-parfait/").host
six=URL("https://www.freshoffthegrid.com/grilled-chicken-veggie-skewers/").host
seven=URL("https://www.loveandlemons.com/quinoa-bowl/").host
eight=URL("https://www.simplyrecipes.com/recipes/sweet_potato_and_black_bean_tacos/").host
nine=URL("https://www.loveandlemons.com/vegetable-soup/").host
ten=URL("https://www.thekitchn.com/baked-cod-22925293").host

#list of some recipes
recipe=[
    ("Quinoa Salad with Roasted Vegetables" , [5,7,10,9,8], one),
    ("Grilled Salmon with Asparagus:" , [5,2,10,7,8],tow ),
    ("Stuffed Bell Peppers" , [4,4,3,9,8] ,three),
    ("Vegetable Stir-Fry" , [5,1,4,9,7],four ),
    ("Greek Yogurt Parfait" , [10,7,10,6,8] ,five),
    ("Chicken and Vegetable Skewers" , [5,7,10,9,8],six ),
    ("Mediterranean Quinoa Bowl" , [8,6,5,10,8],seven),
    ("Black Bean and Sweet Potato Tacos" , [2,7,1,9,10] ,eight),
    ("Vegetable Soup" , [5,7,6,9,4],nine ),
    ("Baked Cod with Lemon and Herbs" , [9,7,10,6,8],ten )
 ]



main=render("\nMain menu",colors=['green', 'white'], align='center',font='tiny')


x=text2art('Choose which Mineral would you check"\n',"fancy135").center(140)
a=text2art('1.Check your zinc levels\n',"fancy135").center(140)
z=text2art('2.Check your iron levels \n',"fancy135").center(140)
b=text2art('3.Check your copper levels\n',"fancy135").center(140)
c=text2art('4.Check your potassium levels\n',"fancy135").center(140)
d=text2art('5.Show Top 5 healthy recipes\n',"fancy135").center(140)
e=text2art('6.LogOut" \n',"fancy135").center(140)
f=text2art('> Enter your chois here :\n',"fancy135").center(140)
g=text2art('inter your amount of zinc :\n',"fancy135").center(140)
h=text2art('inter your amount iron :\n',"fancy135").center(140)
i=text2art('inter your amount copper :\n',"fancy135").center(140)
j=text2art('inter your amount potassium :\n',"fancy135").center(140)
l=text2art('Goodbey~ , let us see you soon\n',"fancy135").center(140)
p=text2art('Enter the password :\n',"fancy135").center(140)


top=render("\nTop five recipes ",colors=['green', 'white'], align='center',font='tiny')


k=text2art('> To back to the main menu press enter\n',"fancy135").center(140)
ii=text2art("invalid input\n","fancy135").center(140)




#User main menu 
def userchoises():
 
 while True:
  
  print(decor("fancy5",both=True)*9)
  print("\n\n\n")
  print(main)
  print(x)
  print("\n")
  print(Fore.LIGHTGREEN_EX+a)
  print(Fore.GREEN+z)
  print(Fore.LIGHTGREEN_EX+b)
  print(Fore.GREEN+c)
  print(Fore.LIGHTGREEN_EX+d)
  print("\n")
  print(e)
  choice = input(f)
  print("")
  match choice:
   case "1":
    try:
      amount:int= int(input(Fore.LIGHTGREEN_EX+g))
      zinc(amount)
      input(k)
    except :
     print(Fore.RED+ii)

   case "2":
    try:
        am= int(input(Fore.LIGHTGREEN_EX+h))
        iron(am)
        input(k)
    except :
     print(Fore.RED+ii)

   case "3":
    try:
        w= int(input(Fore.LIGHTGREEN_EX+i))
        copper(w)
        input(k)
    except :
     print(Fore.RED+ii)
    
   case "4":
    try:
        t= int(input(Fore.LIGHTGREEN_EX+j))
        potassium(t)
        input(k)
    except :
     print(Fore.RED+ii)

   case "5":
    try:
        print("\n")
        print(decor("fancy5",both=True)*4)
        print("\n")
        print(top)
        recipe_list(recipe)
        print("\n")
        print(decor("fancy5",both=True)*4)
        print("\n\n\n")
        input(k)
    except :
     print(Fore.RED+ii)

   case "6":
    print(l)
    break
   

