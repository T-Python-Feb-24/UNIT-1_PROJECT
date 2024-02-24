from rich.console import Console
from rich.table import Table
import json
from colorama import Fore
from gtts import gTTS
import os


data={"courses": {},
        "add_student": {}}
def load_data():
    try:
      with open("data.json","r",encoding="utf-8")as file:
        data=json.load(file)
        return data
    except :
        data={"courses": {},
        "add_student": {}}
    
def save_data():
    with open("data.json", "w", encoding="utf-8") as file:
          json.dump(data,file)
data=load_data()

class CourseManager:
    def add_courses():
       course_name = input("Enter the course name: ")
       course_time = input("Enter the course time: ")
       if course_name not in data["courses"]:
         try:
           if not (course_name.isalpha()):
            raise ValueError("Sorry the course name must contain letters only")
           data["courses"][course_name] = course_time
           data["add_student"][course_name] = []  # Initialize list for students
           print(Fore.LIGHTMAGENTA_EX )
           print(f"The course: {course_name} in Time: {course_time} has been added successfully!\n")
           text1="the courses  has been added successfully,Good luck"# مكتبه الصوت
           tts=gTTS(text1,lang="en")
           tts.save("output.mp3")
           os.system("start output.mp3")
           save_data()
         except ValueError as e:
           print(e)
       else:
        print("This course has been added before!\n")

       

    def delete_course():
        course_name = input("Enter the course name you want to delete it: ")
        if course_name in data['courses']:
            del data['courses'][course_name]
            del data['add_student'][course_name]  # Remove student list
            print(f"The course {course_name} has been deleted successfully!\n")
            save_data()
        else:
            print(f"The course: {course_name} is not found\n")
    
    def show_courses():
        console=Console()
        table=Table(title="These are the available courses and their durations:")
        table.add_column("Courses",justify="center",style="cyan",no_wrap=True)
        table.add_column("Duration",style="magenta")
        for course, durations in data['courses'].items():
            table.add_row(course,(f"{durations} hours"))
            table.add_row("","")
        console.print(table)
        save_data()


class StudentManagement:
    
    def add_students():
        course_name = input("Enter the course name: ")
        student_name = input("Enter the student's name: ")
        student_last_name = input("Enter the student's last name:")
        if course_name in data['courses']:
          try:  
            if not (student_name.isalpha()and student_last_name.isalpha()):
               raise ValueError("Sorry the student name must contain letters only")
            if len(data['add_student'][course_name]) < 10:
              data['add_student'][course_name].append((student_name , student_last_name))
              print(Fore.CYAN )
              print(f"The student: {student_name}  {student_last_name} has joined to the course: {course_name} successfully!\n")
              save_data()
            else:
              print(f"Sorry, we can't add more students. The course: {course_name} has reached its maximum capacity\n")
          except ValueError as e:
            print(e)
        else:
           print(f"We couldn't find the course: {course_name}. Please try again.\n")
           
           
    def cancel_registration_student():
        course_name = input("Enter the course name: ")
        student_name = input("Enter the student's name you want to cancel registration for: ")
        student_last_name = input("Enter the student's last name:")
        if course_name in data['add_student'] and (student_name,student_last_name) in data['add_student'][course_name]:
            data['add_student'][course_name].remove((student_name, student_last_name)) 
            print(Fore.LIGHTRED_EX )
            print(f"The student {student_name} {student_last_name} has been removed from the course: {course_name}.\n")
            save_data()
        else:
            print(f"The student {student_name} {student_last_name} is not found in course: {course_name}.\n")
            
            
    def change_course():
       student_name = input("Enter the student's name: ")
       student_last_name = input("Enter the student's last name: ")
       old_course = input("Enter the old course name: ")
       new_course = input("Enter the new course name: ")
    
       if old_course in data['add_student'] and (student_name, student_last_name) in data['add_student'][old_course]:
        
         if new_course in data['courses']:
            if len(data['add_student'][new_course]) < 10:
                data['add_student'][new_course].append((student_name, student_last_name))
                data['add_student'][old_course].remove((student_name, student_last_name))
                print(Fore.YELLOW)
                print(f"The course for {student_name} {student_last_name} has been changed from {old_course} to {new_course}.\n")
                save_data()
            else:
                print(f"Sorry, we can't add the new course: {new_course}. It has reached the maximum limit.\n")
         else:
            print(f"Sorry, the new course {new_course} doesn't exist.\n")
       else:
        print(f"Sorry, the student {student_name} {student_last_name} is not join to the course: {old_course}.\n")
   


    def show_students():
        console= Console()

        table =Table(title="view all students joining the coursees: ")
        table.add_column("Course",justify="center",style="cyan",no_wrap=True)
        table.add_column("Students",style="magenta")
        for course, students in data['add_student'].items():
          
          table.add_row(course,"\n".join([f"{student[0]} {student[1]}\n" 
                                       for student in students  ]))
          table.add_row("","")
            
        console.print(table)
        save_data()
            