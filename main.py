from datetime import date
import json
from Citizen import Citizen
from Vehicle import Vehicle
from Ticket import Ticket
from rich.console import Console
from rich.panel import Panel

console = Console()

citizen_info = []
vehicle_info = []
ticket_info = []

def citizen_load_data():
    try:
        with open("citizen_info.json", "r", encoding="utf-8") as file:
            citizen_content = file.read()
            citizen_info = json.loads(citizen_content, object_hook=lambda o: Citizen(o["name"], o["id"], o["birthDay"], o["placeOfBirth"]))
            console.print(Panel("[bold green]Citizen data loaded successfully![/]", title="Success"))
            return citizen_info
    except Exception as e:
        console.print(Panel(f"[bold red]Error loading citizen data: {e}[/]", title="Error"))
        return []

def vehicle_load_data():
    try:
        with open("vehicle_info.json", "r", encoding="utf-8") as file:
            vehicle_content = file.read()
            vehicle_info = json.loads(vehicle_content, object_hook=lambda o: Vehicle(o["brand"], o["model"], o["year"], o["color"], o["carOwner"], o["plateNumber"]))
            console.print(Panel("[bold green]Vehicle data loaded successfully![/]", title="Success"))
            return vehicle_info
    except Exception as e:
        console.print(Panel(f"[bold red]Error loading vehicle data: {e}[/]", title="Error"))
        return []

def ticket_load_data():
    try:
        with open("ticket_info.json", "r", encoding="utf-8") as file:
            ticket_content = file.read()
            ticket_info = json.loads(ticket_content, object_hook=lambda o: Ticket(o["brand"], o["model"], o["year"], o["plate_number"], o["owner_name"], o["Violation"], o["cost"]))
            console.print(Panel("[bold green]Ticket data loaded successfully![/]", title="Success"))
            return ticket_info
    except Exception as e:
        console.print(Panel(f"[bold red]Error loading ticket data: {e}[/]", title="Error"))
        return []

def ticket_save_data():
    with open("ticket_info.json", "w", encoding="utf-8") as file:
        content2 = json.dumps(ticket_info, default=lambda obj: {"brand": obj.brand, "model": obj.model, "year" : obj.year, "plate_number" : obj.plate_number, "owner_name" : obj.owner_name, "Violation" : obj.violation, "cost" : obj.cost}, indent=4)
        file.write(content2)
    console.print(Panel("[bold green]Ticket data saved successfully![/]", title="Success"))

main_menu = '''
Choose a number:
1) Check citizen information
2) Check vehicle information
3) Tickets
4) EXIT 
'''
citizen_info = citizen_load_data()
vehicle_info = vehicle_load_data()
ticket_info = ticket_load_data()

while True:
    main_choice = input(main_menu)
    if main_choice == "1":
        id_number_input = int(input("Enter the ID number: \n"))
        try:
            citizen:Citizen = list(filter(lambda person: person.id == id_number_input, citizen_info))[0]
            console.print(Panel(f"[cyan]{citizen.name}[/]\n[cyan]{citizen.id}[/]\n[cyan]{citizen.birthDay}[/]\n[cyan]{citizen.placeOfBirth}[/]", title="Citizen Information"))
        except Exception as e:
            console.print(Panel("[bold red]The ID number is not found.[/]", title="Error"))
        input("Press Enter to continue...")
    elif main_choice == "2":
        plate_number_input = input("Enter the plate number: \n")
        try:
            vehicle:Vehicle = list(filter(lambda car: car.plateNumber == plate_number_input, vehicle_info))[0]
            console.print(Panel(f"[cyan]{vehicle.brand}[/]\n[cyan]{vehicle.model}[/]\n[cyan]{vehicle.year}[/]\n[cyan]{vehicle.color}[/]\n[cyan]{vehicle.carOwner}[/]\n[cyan]{vehicle.plateNumber}[/]", title="Vehicle Information"))
        except Exception as e:
            console.print(Panel("[bold red]The plate number is not found.[/]", title="Error"))
        input("Press Enter to continue...")
    elif main_choice == "3":
        personal_menu = """
Choose a number:
1) Give a ticket
2) View old tickets
"""
        personal_choice = input(personal_menu)
        if personal_choice == "1":
            plate_number_input = input("Enter vehicle plate number: \n")
            try:
                vehicle:Vehicle = list(filter(lambda car: car.plateNumber == plate_number_input, vehicle_info))[0]
                console.print(Panel(f"[cyan]{vehicle.brand}[/]\n[cyan]{vehicle.model}[/]\n[cyan]{vehicle.year}[/]\n[cyan]{vehicle.color}[/]\n[cyan]{vehicle.carOwner}[/]\n[cyan]{vehicle.plateNumber}[/]", title="Vehicle Information"))
            except Exception as e:
                console.print(Panel("[bold red]The plate number is not found.[/]", title="Error"))
            violation_input = input("Violation description \n")
            cost_input = input("Violation fine amount: \n")           
            tickets = Ticket(vehicle.brand, vehicle.model, vehicle.year, vehicle.carOwner, vehicle.plateNumber, violation_input, cost_input)
            ticket_info.append(tickets)
            ticket_save_data()
        elif personal_choice == "2":
            for tickets in ticket_info:
                console.print(Panel(f"[cyan]{tickets.brand}[/]\n[cyan]{tickets.model}[/]\n[cyan]{tickets.year}[/]\n[cyan]{tickets.plate_number}[/]\n[cyan]{tickets.owner_name}[/]\n[cyan]{tickets.violation}[/]\n[cyan]{tickets.cost}[/]", title="Ticket Information"))
                input("Press Enter to continue...")

    elif main_choice == "4":
        console.print(Panel("[yellow]Goodbye!![/]", title="Exit"))
        break
