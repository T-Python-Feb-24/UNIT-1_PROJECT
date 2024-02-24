from colorama import Style,Fore
from tabulate import tabulate
from progress.bar import ChargingBar
import time

class Employee:
    def __init__(self, id, name, tasks):
        self.id = id
        self.name = name
        self.tasks = tasks
    def show_tasks(self):
        '''
        function for show employee tasks
        '''
        bar = ChargingBar(Fore.CYAN+'loading...', max=20)
        
        for i in range(20):
            time.sleep(0.03)
            bar.next()
        bar.finish()        
        print(f"\n {Fore.CYAN}Tasks for employee {self.name} (ID: {self.id}):{Style.RESET_ALL}")
        if self.tasks:
            table = [["Task number", "Description", "State"]]
            for index, task in enumerate(self.tasks, start=1):
                state_color = Fore.GREEN if task['state'] == 'done' else Fore.RED
                table.append([index, task['description'], f"{state_color}{task['state']}{Fore.CYAN}"])
            print(Fore.CYAN+tabulate(table, headers="firstrow", tablefmt="pretty")+Style.RESET_ALL)
        else:
            print(Fore.RED + "No tasks assigned." + Style.RESET_ALL)
                
    def complete_task(self, task_index):
        '''
        function for change the state of task to done
        '''
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["state"] = "done"
            print(Fore.GREEN+"Task marked as done.")
            
        else:
            print(Fore.RED+"Invalid task number.")
