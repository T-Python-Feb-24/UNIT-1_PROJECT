from University import University
from HighSchoolStudent import UniversityAdmissionSystem

# Function to determine the accepted specialization based on the weighted average
def determine_accepted_specialization(weighted_average):
    if weighted_average >= 90:
        return "Medicine"
    elif 80 <= weighted_average < 90:
        return "Engineering"
    elif 70 <= weighted_average < 80:
        return "Arts"
    elif 60 <= weighted_average < 70:
        return "Computer Science"
    elif 50 <= weighted_average < 60:
        return "Business Administration"
    else:
        return None

def main():
    kku = University(
        name="King Khalid University",
        location="Abha, Saudi Arabia",
        colleges=["Engineering", "Arts", "Medicine ,"],
        registration_system="https://www.kku.edu.sa/registration"
    )

    # Add more colleges/specializations
    kku.add_college("Computer Science")
    kku.add_college("Business Administration")
    kku.add_college("Physics")
    kku.add_college("Law")
    kku.add_college("Psychology")

    system = UniversityAdmissionSystem()

    while True:
        print("\n1. Display University Info")
        print("2. Register Student")
        print("3. Select Preferences")
        print("4. Check Acceptance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '2':
            name = input("Enter student name: ")
            gpa = float(input("Enter high school GPA: "))
            qiyas = float(input("Enter Qiyas score: "))
            tahsili = float(input("Enter Tahsili score: "))
            student = system.HighSchoolStudent(name, gpa, qiyas, tahsili)
            system.register_student(student)
        elif choice == '3':
            name = input("Enter student name to select preferences: ")
            student = next((s for s in system.students_list if s['name'] == name), None)
            if student:
                preferences = input("Enter three preferences separated by commas: ").split(',')
                if len(preferences) != 3:
                    print("Please enter exactly three preferences separated by commas.")
                    continue

                weighted_average = (student['gpa'] + student['qiyas'] + student['tahsili']) / 3

                # Determine the accepted specialization based on the weighted average
                accepted_specialization = determine_accepted_specialization(weighted_average)

                if accepted_specialization:
                    print(f"Congratulations! {student['name']}, you are accepted in the {accepted_specialization} major.")
                    # Update the student's preferences
                    system.select_preferences(student, preferences, accepted_specialization)
                else:
                    print(f"Sorry, {student['name']}, you are not accepted in any of your preferred majors.")
        elif choice == '4':
            name = input("Enter student name to check acceptance: ")
            student = next((s for s in system.students_list if s['name'] == name), None)
            if student:
                system.suggest_specialization(student)
        elif choice == '1':
            kku.display_info()  # Assuming you have a display_info method in your University class
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()