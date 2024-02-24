from colorama import Fore, Style, init
from art import *
from pyfiglet import figlet_format
from University import University
from HighSchoolStudent import UniversityAdmissionSystem


init(autoreset=True)


def welcome():
    print(Fore.GREEN + figlet_format("WELCOME TO KING KHALID UNIVERSITY", font="small"))
    print(Style.RESET_ALL)
    print(Fore.BLACK + "______________________________________________________________________________")
    print(Style.RESET_ALL)

def determine_accepted_specialization(weighted_average):
    if weighted_average >= 90:
        return Fore.GREEN + "Medicine" + Style.RESET_ALL
    elif 80 <= weighted_average < 90:
        return Fore.BLUE + "Engineering" + Style.RESET_ALL
    elif 70 <= weighted_average < 80:
        return Fore.YELLOW + "Business Administration" + Style.RESET_ALL
    elif 60 <= weighted_average < 70:
        return Fore.MAGENTA + "Computer Science" + Style.RESET_ALL
    elif 50 <= weighted_average < 60:
        return Fore.CYAN + "Arts" + Style.RESET_ALL
    else:
        return None

def main():
    kku = University(
        name=Fore.GREEN + "King Khalid University" + Style.RESET_ALL,
        location=Fore.BLACK + "Abha, Saudi Arabia" + Style.RESET_ALL,
        specialties=[
            Fore.BLUE + "Engineering" + Style.RESET_ALL,
            Fore.BLUE + "Arts" + Style.RESET_ALL,
            Fore.BLUE + "Medicine" + Style.RESET_ALL,
            Fore.BLUE + "Computer Science" + Style.RESET_ALL,
            Fore.BLUE + "Business Administration" + Style.RESET_ALL
        ],
        registration_system=Fore.GREEN + "https://www.kku.edu.sa/registration" + Style.RESET_ALL
    )
    system = UniversityAdmissionSystem()

    while True:
        print(Fore.WHITE + "\n1. Display University Info" + Style.RESET_ALL)
        print(Fore.WHITE + "2. Register Student" + Style.RESET_ALL)
        print(Fore.WHITE + "3. Select Preferences" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Check Acceptance" + Style.RESET_ALL)
        print(Fore.RED + "5. Exit" + Style.RESET_ALL)
        
        choice = input(Fore.CYAN + "Enter your choice: " + Style.RESET_ALL)

        if choice == '2':
            name = input(Fore.BLACK + "Enter student name: " + Style.RESET_ALL)
            gpa = float(input(Fore.YELLOW + "Enter high school GPA: " + Style.RESET_ALL))
            qiyas = float(input(Fore.YELLOW + "Enter Qiyas score: " + Style.RESET_ALL))
            tahsili = float(input(Fore.YELLOW + "Enter Tahsili score: " + Style.RESET_ALL))
            student = system.HighSchoolStudent(name, gpa, qiyas, tahsili)
            system.register_student(student)
            print(Fore.CYAN + "______________________________________________________________________________" + Style.RESET_ALL)
        elif choice == '3':
            name = input(Fore.MAGENTA + "Enter student name to select preferences: " + Style.RESET_ALL)
            student = next((s for s in system.students_list if s['name'] == name), None)
            if student:
                preferences = input(Fore.MAGENTA + "Enter three preferences separated by commas: " + Style.RESET_ALL).split(',')
                if len(preferences) != 3:
                    print(Fore.RED + "Please enter exactly three preferences separated by commas.")
                    print(Style.RESET_ALL)
                    print(Fore.CYAN + "______________________________________________________________________________" + Style.RESET_ALL)
                    continue

                weighted_average = (student['gpa'] + student['qiyas'] + student['tahsili']) / 3

                
                accepted_specialization = determine_accepted_specialization(weighted_average)

                if accepted_specialization:
                    print(Fore.GREEN + f"Congratulations! {student['name']}, you are accepted in the {accepted_specialization} major." )


                    
                    system.select_preferences(student, preferences, accepted_specialization)
                else:
                    print(Fore.RED + f"Sorry, {student['name']}, you are not accepted in any of your preferred majors.")
                print(Style.RESET_ALL)
                print(Fore.CYAN + "______________________________________________________________________________" + Style.RESET_ALL)
        elif choice == '4':
            name = input(Fore.GREEN + "Enter student name to check acceptance: " + Style.RESET_ALL)
            student = next((s for s in system.students_list if s['name'] == name), None)
            if student:
                system.suggest_specialization(student)
                
                print(Fore.CYAN + "______________________________________________________________________________" + Style.RESET_ALL)
        elif choice == '1':
            kku.display_info()
            print(Fore.CYAN + "______________________________________________________________________________" + Style.RESET_ALL)  # Assuming you have a display_info method in your University class
        elif choice == '5':
            print(Fore.RED + "Exiting the program." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invaild choice.Please enter a valid option." + Style.RESET_ALL)
           

if __name__ == "__main__":
    welcome()
    main()