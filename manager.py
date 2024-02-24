import json
from datetime import date
from employee import Employee
from colorama import Fore,Style
from progress.bar import ChargingBar
from tabulate import tabulate
import time
class Manager:
    employees = []

    def load_data():
        '''
        function to read the data from json
        '''
        try:
            with open("employee.json", "r", encoding="utf-8") as file:
                return json.loads(file.read())
        except FileNotFoundError:
            return []

    def save_data():
        '''
        function for save the data
        '''
        with open("employee.json", "w", encoding="utf-8") as file:
            json.dump(Manager.employees, file, indent=4)

    def is_id_unique(new_id):
        '''
        function for check if the id is uniqe or no
        '''
        for employee in Manager.employees:
            if employee["ID"] == new_id:
                return False
        return True

    def add_employee(id_input, name_input, department_input):
        '''
        function to add a new employee
        '''
        Manager.employees = Manager.load_data()
        if not Manager.is_id_unique(id_input):
            raise Exception(Fore.RED+"The ID is already in use. Please choose a unique ID.")

        new_employee = {
            "ID": id_input,
            "Name": name_input,
            "Department": department_input,
            "Date": str(date.today()),
            "Tasks": []
        }
        Manager.employees.append(new_employee)
        Manager.save_data()
        print(Fore.GREEN+"Employee added successfully.")

    def show_employees():
        '''
        function to display employee list
        '''
        Manager.employees = Manager.load_data()
        
        bar = ChargingBar(Fore.BLUE+'loading...', max=20)
        
        for i in range(20):
            time.sleep(0.03)
            bar.next()
        bar.finish()
        
        sorted_employees = sorted(Manager.employees, key=lambda x: int(x["ID"]))
        
        table = [["ID", "Name", "Department", "Date"]]
        for employee in sorted_employees:
            table.append([employee["ID"], employee["Name"], employee["Department"], employee["Date"]])
        
        print("\n"+Fore.LIGHTGREEN_EX,tabulate(table, headers="firstrow", floatfmt="simple"))
                

    def show_employee_tasks(employee_id):
        '''
        function to show employee tasks
        '''
        Manager.employees = Manager.load_data()
        bar = ChargingBar(Fore.CYAN+'loading...', max=20)
        
        for i in range(20):
            time.sleep(0.03)
            bar.next()
        bar.finish()  
        for employee in Manager.employees:
            if employee["ID"] == employee_id:
                print(f"Tasks for employee {employee['Name']} (ID: {employee_id}):")
                if employee["Tasks"]:
                    table = [["Task number", "Description", "State"]]
                    for task in employee["Tasks"]:
                        state_color = Fore.GREEN if task['state'] == 'done' else Fore.RED
                        table.append([task["task_number"], task['description'], f"{state_color}{task['state']}{Fore.CYAN}"])
                    print("\n" + Fore.CYAN + tabulate(table, headers="firstrow", tablefmt="pretty"))
                else:
                    print(Fore.RED + "No tasks assigned.")
                return
        print(f"No employee with ID {employee_id} found.")

    def add_task_to_employee(employee_id, task_description,task_number):
        '''
        function to add a new task 
        '''
        Manager.employees = Manager.load_data()

        for employee in Manager.employees:
            if employee["ID"] == employee_id:
                employee["Tasks"].append({"task_number":task_number,"description": task_description, "state": "not ready"})
                Manager.save_data()
                print(f"Task added successfully for employee ID: {employee_id}")
                return
        print(f"{Fore.RED}No employee with ID {Fore.WHITE}{employee_id} {Fore.RED}found.{Fore.BLUE}")



    def remove_employee(employee_id):
        '''
        function for remove employee
        '''
        Manager.employees = Manager.load_data()

        for index, employee in enumerate(Manager.employees):
            if employee["ID"] == employee_id:
                del Manager.employees[index]
                Manager.save_data()
                print(f"Employee with ID {employee_id} removed successfully.")
                return
        print(f"{Fore.RED}No employee with ID {employee_id} found.{Style.RESET_ALL}")

    def get_employee(employee_id):
        
        Manager.employees = Manager.load_data()

        for employee in Manager.employees:
            if employee["ID"] == employee_id:
                return employee
        return None

    def create_employee_object(employee):
        return Employee(employee["ID"], employee["Name"], employee["Tasks"])
