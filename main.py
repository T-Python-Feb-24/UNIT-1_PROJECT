import atexit
from colorama import Fore, Style
from manager import Manager

def main():
    def exit_handler():
        Manager.save_data()

    atexit.register(exit_handler)
    Manager.employees = Manager.load_data()
    print(Fore.GREEN+"Welcome to our program")
    while True:

        print(f"{Fore.LIGHTWHITE_EX}Press {Fore.CYAN}1{Fore.LIGHTWHITE_EX} for control as a manager.")
        print(f"{Fore.LIGHTWHITE_EX}Press{Fore.CYAN} 2{Fore.LIGHTWHITE_EX} for control as an employee.")
        print(f"{Fore.LIGHTWHITE_EX}Press {Fore.CYAN}3{Fore.LIGHTWHITE_EX} for Exit.{Style.RESET_ALL}")

        user_input = input("Your choice: ")

        if user_input == "1":
            while True:
                print(Fore.BLUE+f"\n----------------{Fore.WHITE}Manager{Fore.BLUE}----------------------")
                print(f"Press {Fore.WHITE}1 {Fore.BLUE}for adding a new employee")
                print(f"Press {Fore.WHITE}2 {Fore.BLUE}for showing the list of employees")
                print(f"Press {Fore.WHITE}3{Fore.BLUE} to add a task to an employee")
                print(f"Press {Fore.WHITE}4 {Fore.BLUE}to show tasks of an employee")
                print(f"Press {Fore.WHITE}5 {Fore.BLUE}to remove an employee")
                print(f"Press {Fore.WHITE}6 {Fore.BLUE}to exit")
                print(f"---------------------------------------------{Style.RESET_ALL}")

                manager_input = input(Fore.BLUE+"Your choice: ")

                if manager_input == "1":
                    id_input = input(f"{Fore.LIGHTBLUE_EX}ID: {Style.RESET_ALL}")
                    name_input = input(f"{Fore.LIGHTBLUE_EX}Name:{Style.RESET_ALL} ")
                    department_input = input(f"{Fore.LIGHTBLUE_EX}Department:{Style.RESET_ALL} ")
                    Manager.add_employee(id_input, name_input, department_input)

                elif manager_input == "2":
                    Manager.show_employees()

                elif manager_input == "3":
                    print(f"{Fore.BLUE}-----------------------{Fore.WHITE}ADD TASK-{Fore.BLUE}-----------------------")
                    employee_id = input(f"Enter the ID of the employee:{Style.RESET_ALL} ")
                    task_number=input(F"{Fore.BLUE}Enter task number: ")
                    task_description = input(f"{Fore.BLUE}Enter the task description: ")
                    Manager.add_task_to_employee(employee_id,task_description,task_number)
                    print("---------------------------------------------------")

                elif manager_input == "4":
                    employee_id = input(f"{Fore.BLUE}Enter the ID of the employee: {Style.RESET_ALL}")
                    Manager.show_employee_tasks(employee_id)

                elif manager_input == "5":
                    employee_id = input(f"{Fore.BLUE}Enter the ID of the employee to remove:{Style.RESET_ALL} ")
                    Manager.remove_employee(employee_id)
                elif manager_input =="6":
                    break
                    

                else:
                    print(F"{Fore.RED}Invalid choice. Please choose a valid option.{Style.RESET_ALL}")

        elif user_input == "2":
            while True:
                print(Fore.LIGHTYELLOW_EX+"-----------------employee---------------")
                print(f"{Fore.LIGHTYELLOW_EX}Press {Fore.WHITE}1{Fore.LIGHTYELLOW_EX} to complete a task")
                print(f"Press {Fore.WHITE}2{Fore.LIGHTYELLOW_EX} to back")
                exit_input = input("Your choice:"+Style.RESET_ALL)
                if exit_input == "1":
                    employee_id = input(f"{Fore.LIGHTYELLOW_EX}Enter the ID of the employee: "+Style.RESET_ALL)
                    employee = Manager.get_employee(employee_id)
                    if employee:
                        employee_obj = Manager.create_employee_object(employee)
                        while True:
                            print(F"\n{Fore.LIGHTYELLOW_EX}Press {Fore.WHITE}1{Fore.LIGHTYELLOW_EX} to show tasks")
                            print(f"Press {Fore.WHITE}2{Fore.LIGHTYELLOW_EX} to complete a task")
                            print(f"Press {Fore.WHITE}3{Fore.LIGHTYELLOW_EX} to exit")
                            employee_choice = input("Your choice: "+Style.RESET_ALL)

                            if employee_choice == "1":
                                employee_obj.show_tasks()

                            elif employee_choice == "2":
                                try:
                                    task_index = int(input(Fore.LIGHTYELLOW_EX+"Enter the number of the task to complete: "+Style.RESET_ALL))
                                    employee_obj.complete_task(task_index)
                                except:
                                    raise Exception(Fore.RED+"please enter a valid number"+Style.RESET_ALL)
                            elif employee_choice == "3":
                                Manager.save_data()
                                break

                            else:
                                print(Fore.RED+"Invalid choice. Please choose a valid option."+Style.RESET_ALL)

                    else:
                        print(Fore.RED+"Employee not found."+Style.RESET_ALL)
                elif exit_input == "2":
                    break
                else:
                    raise Exception(Fore.RED+"Invalid choice. Please choose between '1' or '2'."+Style.RESET_ALL)
        elif user_input == "3":
            Manager.save_data()
            print(Fore.RED + "The program has been closed." + Style.RESET_ALL)
            break

        else:
            print(Fore.RED+"Invalid choice. Please choose '1', '2', or '3'."+Style.RESET_ALL)

if __name__ == "__main__":
    main()

