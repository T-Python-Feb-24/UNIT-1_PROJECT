from check import checkValidInt
from termcolor import colored
historical_places_dic:dict = {

        'Riyadh Region' : [
        {"name" : "Masmak Fortress (Riyadh City)" , "description" : "The Masmak Fortress is a historic fortress located in the heart of Riyadh city. It played a significant role in the establishment of the first Saudi state. The fortress witnessed the daring raid by Abdulaziz Ibn Saud in 1902, marking the recapture of Riyadh. Today, it serves as a museum that showcases artifacts and exhibits related to the region's history."},
        {"name" : "Diriyah (Ad-Dir'iyah)" , "description" : "Diriyah is a historic town located on the outskirts of Riyadh and is the original home of the Saudi royal family. It is a UNESCO World Heritage Site known for its mud-brick architecture and historical significance. Diriyah played a crucial role in the early history of the Kingdom and is a key symbol of Saudi Arabia's cultural heritage."},
        {"name" : "Murabba Palace (Riyadh City)" , "description" : "The Murabba Palace, also known as Qasr Al-Murabba, is a historic palace in Riyadh that dates back to the time of King Abdulaziz Ibn Saud. Built in 1936, the palace served as the King's residence and a center for government affairs. It reflects traditional Najdi architecture and is now part of the King Abdulaziz Historical Center."}
],
        "East Region" : [
        {"name" : "Tarout Island Archaeological Site (Qatif)" , "description" : "Tarout Island, located near Qatif, has archaeological sites that date back to ancient civilizations, including the Dilmun and Hellenistic periods. The area has revealed artifacts such as pottery, tombs, and structures, providing insights into the region's long history."},
        {"name" : "Ibrahim Palace (Al Hofuf)" , "description" : "Ibrahim Palace, also known as Qasr Ibrahim, is a historical palace located in Al Hofuf. The palace dates back to the Ottoman era and is known for its unique architectural style. It has been restored and is now open to the public, offering a glimpse into the region's historical architecture."},
        {"name" : "Jubail Historical District (Jubail)" , "description" : "Jubail, a major industrial city, also has a historical district that preserves the traditional architecture of the region. The district showcases old buildings, mosques, and narrow streets, reflecting the historical and cultural heritage of Jubail."}
],
        "Westren Region" : [
        {"name" : "Historic Jeddah (Al-Balad)" , "description" : "Historic Jeddah, also known as Al-Balad, is a UNESCO World Heritage Site and one of the oldest parts of the city. It features traditional coral houses, historic mosques, and narrow alleyways. The area provides a glimpse into Jeddah's rich cultural and architectural heritage."},
        {"name" : "Al-Masjid an-Nabawi (Medina)" , "description" : "The second holiest mosque in Islam, Al-Masjid an-Nabawi, is located in Medina. It is the final resting place of Prophet Muhammad and is known for its significant religious and historical importance."},
        {"name" : " Abraj Al Bait Towers (Clock Tower) Jeddah" , "description" : "While modern, the Abraj Al Bait Towers, including the Clock Tower, are prominent landmarks near the Grand Mosque. They house hotels, shopping malls, and are known for their architectural significance."}
],
        "North Region" : [
        {"name" : "Hegra (AlUla)" , "description" : "Mada'in Saleh, also known as Al-Hijr or Hegra, is an archaeological site in northwestern Saudi Arabia, part of the Al-Ula governorate. It was once a significant city of the Nabataean Kingdom, contemporaneous with Petra in Jordan. Key features include well-preserved rock-cut tombs with intricate facades, such as the notable Qasr Al-Farid ('Lonely Castle'). Mada'in Saleh provides insights into Nabataean culture and architecture, earning it UNESCO World Heritage status in 2008. It is a major historical and cultural destination, showcasing the ancient history of the region."},
        {"name" : "Tabuk Castle (Tabuk)" , "description" : "Dating to 1559, Tabuk Castle is now a museum, with several rooms housing some interesting historical artefacts from the Ottoman period and lots of signage about the history of Tabuk, its connection to the Prophet Muhammad and several famous travellers, including Ibn Battuta and Evliya Celebi. The castle features a ground-floor mosque, an open courtyard and a stairway to the castle’s 2nd-floor mosque and watchtowers. Outside are cisterns that once captured water from a spring that the Prophet Muhammad reportedly drank from."},
        {"name" : "Al Ula Fort (AlUla Old Town)" , "description" : "to protect the ancient village, inhabitants in the 6th century used red-sandstone blocks to build this castle on a promontory that gives a 360-degree view of the surrounding valley. The 45m climb to the castle is of moderate difficulty but worth the effort once you see the red-tinged cliffs of the sweeping valley below."}
],
        "South Region" : [
        {"name" : "Rijal Almaa Museum (Asir Province)" , "description" : "Rijal Alma is a well-preserved heritage village known for its unique stone architecture.The village provides insights into the traditional lifestyle and architecture of the Asir region."},
        {"name" : "Habala Village (Asir Province)" , "description" : "Habala is an ancient mountain village famous for its hanging houses built into the cliffs. The village reflects the historical and cultural heritage of the local communities."},
]
}



def regionPlaces(region:str):
        print(colored(f"\nHistoricl places in {region}:",'green'))
        region = historical_places_dic[region]
        for place in region :
                print(f"- {place['name']}:\n {place['description']}")
                print()


def allPlaces():
        all = historical_places_dic
        for region,places in all.items() :
                print(f"- {region} :")
                for p in places :
                        print(f"{p['name']}")
                print()

def historicalPlaces():
        print("Explore the rich tapestry of Saudi Arabia's past as we")
        print("guide you through its mesmerizing Historical Places.\n")
        print("For Historical Places in:")
        print("1. Riyadh Region")
        print("2. East Region")
        print("3. Western Region")
        print("4. North Region")
        print("5. South Region")
        print("6. Uncover the entire tapestry of Saudi Arabia's history!\n")
        while True:
              userInput = input("Press the number corresponding to your desired adventure: ")
              choise = checkValidInt(userInput,6)
              if type(choise) == int:
                break
        if choise == 1:
                regionPlaces("Riyadh Region")
        elif choise == 2:
                regionPlaces("East Region")
        elif choise == 3:
                regionPlaces("Westren Region")
        elif choise == 4:
                regionPlaces("North Region")
        elif choise == 5:
                regionPlaces("South Region")
        elif choise == 6:
                allPlaces()
        
        while True:
                end_input = input("To Continue Exploring Historical Places Press 1,To Exit Historical Places Service, press 2:")
                option = checkValidInt(end_input,2)
                if type(option)==int:
                        break     
        if option == 1:
                historicalPlaces()
        elif option == 2:
                print("Thank You For using Our Historical Places Service!🌐\n")
                return
        return