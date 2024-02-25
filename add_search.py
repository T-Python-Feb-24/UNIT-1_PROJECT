import json


'''Here is an minerals function for Add , delete ,show and search in lists food through mineral level 
for every mineral level (zinc,iron,copper,potassium) with json file to each mineral '''

done=("> Done ").center(140)

#zinc add function , show , search functions 
zinc={
 "high_zinc":[] ,
 "low_zinc":[] }


def add_to_zinc (name ,grams,calories , zinc_level):
    data = {
        "name": name,
        "grams": grams,
        "calories": calories
    }
    try:
        with open("zincc.json" , "r") as zincfile:
         zinc=json.load(zincfile)
         zincfile.read()
         if zinc_level == "high":
             zinc["high_zinc"].append(data)
             print(done)
         elif zinc_level == "low":
             zinc["low_zinc"].append(data)
             print(done)
        with open("zincc.json" , "w") as zincfile :
            json.dump(zinc,zincfile,indent=4)
    except ValueError as e:
       print(e)


#delete mineral function

def delete_from_zinc(name, zinc_level):
    try:
        with open("zincc.json", "r") as dzfile:
            zinc = json.load(dzfile)

        if zinc_level == "high":
         items = zinc["high_zinc"]
        elif zinc_level == "low":
         items = zinc["low_zinc"]
        else:
         print("Invalid zinc level provided")
         return

        for item in items:
         if item["name"] == name:
             items.remove(item)
             print(f"\n{name} deleted from {zinc_level} zinc\n".center(140))
             break
        else:
            print(f"\n{name} not found in {zinc_level}zinc\n".center(140))

        with open("zincc.json", "w") as dzfile:
            json.dump(zinc, dzfile, indent=4)

    except FileNotFoundError:
        print("Zinc file not found")
    except Exception as e:
        print("An error occurred:", e)




#show the list of food 
def show_zinc (level):
    with open("zincc.json","r") as zfile:
        z=json.load(zfile)
        if level == "high":
         return z["high_zinc"]
        elif level == "low":
            return z["low_zinc"]
        
def zinc_list (level):
   res=show_zinc(level)
   if res:
    for item in res:
            print(f"\nName: {item['name']}".center(100), f"Grams: {item['grams']}".center(100),f"Calories: {item['calories']}".center(100))
        
#search in list
def search_in_zinc(level ,name):
  with open("zincc.json","r") as file :
   zinc=json.load(file)
   try:
    if level == "high":
        hzinc =zinc["high_zinc"]
        for data in hzinc:
          if data["name"] == name:
            for i in data:
               print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
               break
    elif level == "low":
            lzinc=zinc["low_zinc"]
            for data in lzinc:
              if data["name"] == name:
               for i in data:
                print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
                break
            
    else:
        raise ValueError("Invalid input: level must be either 'high' or 'low'")
   except ValueError as v :
      print(v)
   except Exception as e:
    print(e)


#iron add function , show , search functions 
iron={
 "high_iron":[] ,
 "low_iron":[] }

def add_to_iron (name ,grams,calories , iron_level):
    data = {
        "name": name,
        "grams": grams,
        "calories": calories
    }
    with open("iron.json" , "r") as ironfile:
       iron=json.load(ironfile)
       ironfile.read()
    if iron_level == "high":
        iron["high_iron"].append(data)
        print(done)
    elif iron_level == "low":
        iron["low_iron"].append(data)
        print(done)
    with open("iron.json" , "w") as ironfile :
        json.dump(iron,ironfile,indent=4)

#delete mineral function

def delete_from_iron(name, iron_level):
    try:
        with open("iron.json", "r") as difile:
            iron = json.load(difile)

        if iron_level == "high":
            items = iron["high_iron"]
        elif iron_level == "low":
            items = iron["low_iron"]
        else:
            print("Invalid iron level provided")
            return

        for item in items:
            if item["name"] == name:
             items.remove(item)
             print(f"\n{name} deleted from {iron_level} iron\n".center(140))
             break
        else:
            print(f"\n{name} not found in {iron_level} iron\n".center(140))

        with open("iron.json", "w") as difile:
            json.dump(iron, difile, indent=4)

    except FileNotFoundError:
        print("iron file not found")
    except Exception as e:
        print("An error occurred:", e)





#show the list of food 
def show_iron (level):
    with open("iron.json","r") as ifile:
        i=json.load(ifile)
        if level == "high":
         return i["high_iron"]
        elif level == "low":
            return i["low_iron"]
        
def iron_list (level):
   res=show_iron(level)
   if res:
    for item in res:
            print(f"\nName: {item['name']}".center(100), f"Grams: {item['grams']}".center(100),f"Calories: {item['calories']}".center(100))
     
#search in list
def search_in_iron(level ,name):
  with open("iron.json","r") as ifile :
   iron=json.load(ifile)
   try:
    if level == "high":
        hiron =iron["high_iron"]
        for data in hiron:
          if data["name"] == name:
           for i in data:
            print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
            break
        
    elif level == "low":
        liron=iron["low_iron"]
        for data in liron:
         if data["name"] == name:
          for i in data:
            print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
            break
    
    else:
      raise ValueError("Invalid input: level must be either 'high' or 'low'")
   except ValueError as v :
        print(v)
   except Exception as e:
        print(e)


#copper add function , show , search functions 
copper={
 "high_copper":[] ,
 "low_copper":[] }

def add_to_copper (name ,grams,calories , copper_level):
    data = {
        "name": name,
        "grams": grams,
        "calories": calories
    }
    with open("copper.json" , "r") as copperfile:
       copper=json.load(copperfile)
       copperfile.read()
    if copper_level == "high":
        copper["high_copper"].append(data)
        print(done)
    elif copper_level == "low":
        copper["low_copper"].append(data)
        print(done)
    with open("copper.json" , "w") as copperfile :
        json.dump(copper,copperfile,indent=4)

#delete mineral function

def delete_from_copper(name, copper_level):
    try:
        with open("copper.json", "r") as dcfile:
            copper = json.load(dcfile)

        if copper_level == "high":
            items = copper["high_copper"]
        elif copper_level == "low":
            items = copper["low_copper"]
        else:
            print("Invalid copper level provided")
            return

        for item in items:
            if item["name"] == name:
             items.remove(item)
             print(f"\n{name} deleted from {copper_level} copper\n".center(140))
             break
        else:
            print(f"\n{name} not found in {copper_level} copper\n".center(140))

        with open("copper.json", "w") as dcfile:
            json.dump(copper, dcfile, indent=4)

    except FileNotFoundError:
        print("copper file not found")
    except Exception as e:
        print("An error occurred:", e)




#show the list of food 
def show_copper (level):
    with open("copper.json","r") as cfile:
        c=json.load(cfile)
        if level == "high":
         return c["high_copper"]
        elif level == "low":
            return c["low_copper"]
        
def copper_list (level):
   res=show_copper(level)
   if res:
    for item in res:
        print(f"\nName: {item['name']}".center(100), f"Grams: {item['grams']}".center(100),f"Calories: {item['calories']}".center(100))
        
#search in list
def search_in_copper(level ,name):
  with open("copper.json","r") as ifile :
   copper=json.load(ifile)
   try:
    if level == "high":
        hcopper =copper["high_copper"]
        for data in hcopper:
          if data["name"] == name:
            for i in data:
             print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
             break
        
    elif level == "low":
            lcopper=copper["low_copper"]
            for data in lcopper:
              if data["name"] == name:
                for i in data:
                 print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
                 break
            
    else:
     raise ValueError("Invalid input: level must be either 'high' or 'low'")
   except ValueError as v :
    print(v)
   except Exception as e:
    print(e)


#potassium add function , show , search functions 
potassium={
 "high_potassium":[] ,
 "low_potassium":[] }

def add_to_potassium (name ,grams,calories , potassium_level):
    data = {
        "name": name,
        "grams": grams,
        "calories": calories
    }
    with open("potassium.json" , "r") as potassiumfile:
       potassium=json.load(potassiumfile)
       potassiumfile.read()
    if potassium_level == "high":
        potassium["high_potassium"].append(data)
        print(done)
    elif potassium_level == "low":
        potassium["low_potassium"].append(data)
        print(done)
    with open("potassium.json" , "w") as potassiumfile :
        json.dump(potassium,potassiumfile,indent=4)


#delete mineral function

def delete_from_potassium(name, potassium_level):
    try:
        with open("potassium.json", "r") as dpfile:
            potassium = json.load(dpfile)

        if potassium_level == "high":
            items = potassium["high_potassium"]
        elif potassium_level == "low":
            items = potassium["low_potassium"]
        else:
            print("Invalid potassium level provided")
            return

        for item in items:
            if item["name"] == name:
             items.remove(item)
             print(f"\n{name} deleted from {potassium_level} potassium\n".center(140))
             break
        else:
            print(f"\n{name} not found in {potassium_level} potassium\n".center(140))

        with open("potassium.json", "w") as dpfile:
            json.dump(potassium, dpfile, indent=4)

    except FileNotFoundError:
        print("potassium file not found")
    except Exception as e:
        print("An error occurred:", e)





#show the list of food 
def show_potassium (level):
    with open("potassium.json","r") as pfile:
        p=json.load(pfile)
        if level == "high":
         return p["high_potassium"]
        elif level == "low":
            return p["low_potassium"]
        
def potassium_list (level):
   res=show_potassium(level)
   if res:
    for item in res:
        print(f"\nName: {item['name']}".center(100), f"Grams: {item['grams']}".center(100),f"Calories: {item['calories']}".center(100))

#search in list
def search_in_potassium(level ,name):
    with open("potassium.json","r") as pfile :
       potassium=json.load(pfile)
       try:
        if level == "high":
            hpotassium =potassium["high_potassium"]
            for data in hpotassium:
                if data["name"] == name:
                 for i in data:
                  print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
                  break
              
        elif level == "low":
            lpotassium=potassium["low_potassium"]
            for data in lpotassium:
              if data["name"] == name:
                for i in data:
                 print(f"\nName:{data['name']}".center(90),f"Grams: {data['grams']}".center(90),f"Calories: {data['calories']}".center(90))
                 break
            
        else:
         raise ValueError("Invalid input: level must be either 'high' or 'low'")
       except ValueError as v :
         print(v)
       except Exception as e:
         print(e)





