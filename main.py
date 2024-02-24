from courses import CourseManager,StudentManagement
from colorama  import Fore 
from art import *
from gtts import gTTS
import os
 
 
text="Welcome to the courses platform"
tts=gTTS(text,lang="en")
tts.save("output.mp3")
os.system("start output.mp3")

print(Fore.LIGHTMAGENTA_EX)
print(text2art('''Welcome
to the courses
platform''',font="cybermedum" ))
print('''My project is about a platform to add, delete, and display courses and their times, 
with the ability for students to join courses, change the course when needed, 
or cancel participation in the course''')

print(Fore.LIGHTRED_EX)
print('''Note: There is a maximum limit for students to join each course,
The limit for each course is only 10 students ''')


print(Fore.BLUE)
usage = '''
To use class course and class student, choose a number:
1) Add new course
2) Delete the course
3) Display all courses
4) Add a new student
5) Cancel student registration
6) Change course
7) Show all students
8) Exit
'''
while True:
    user_choice = input(usage)
    if user_choice == "1":
        CourseManager.add_courses()
    elif user_choice == "2":
        CourseManager.delete_course()
    elif user_choice == "3":
        CourseManager.show_courses()
    elif user_choice == "4":
            StudentManagement.add_students()
    elif user_choice == "5":
        StudentManagement.cancel_registration_student()
    elif user_choice == "6":
        StudentManagement.change_course()
    elif user_choice == "7":
        StudentManagement.show_students()
    elif user_choice == "8":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 8.\n")