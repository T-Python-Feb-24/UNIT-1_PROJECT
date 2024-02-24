class UniversityAdmissionSystem:
    def __init__(self, students_list=None):
        self.students_list = students_list if students_list is not None else []

    def HighSchoolStudent(self, name, gpa, qiyas, tahsili):
        student = {
            'name': name,
            'gpa': gpa,
            'qiyas': qiyas,
            'tahsili': tahsili,
            'preferences': []
        }
        return student

    def register_student(self, student):
        self.students_list.append(student)
        print(f"The student {student['name']} is registered successfully.")

    def suggest_specialization(self, student):
        weighted_average = (student['gpa'] + student['qiyas'] + student['tahsili']) / 3

        print(f"\nPercentage of student {student['name']}: {weighted_average}")

        if weighted_average >= 90:
            print(f"Congratulations! You can join the Medicine major.")
            student['preferences'].append("Medicine")
        elif 80 <= weighted_average < 90:
            print(f"Congratulations! You can join the Engineering major.")
            student['preferences'].append("Engineering")
        elif 70 <= weighted_average < 80:
            print(f"Congratulations! You can join the Business Administration major.")
            student['preferences'].append("Business Administration")
        elif 60 <= weighted_average < 70:
            print(f"Congratulations! You can join the Computer Science major.")
            student['preferences'].append("Computer Science")
        elif 50 <= weighted_average < 60:
            print(f"Congratulations! You can join the Arts major.")
            student['preferences'].append("Arts")
        else:
            print("Sorry for not accepting you. Your weighted average is below the minimum requirement.")

    def select_preferences(self, student, preferences, closest_specialization):
        print(f"\nSelecting preferences for {student['name']}: {preferences}")
        student['preferences'] = preferences
        print(f"Closest specialization: {closest_specialization}")

    def admission_process(self):
        for student in self.students_list:
            if student['preferences']:
                accepted_specialization = self._find_accepted_specialization(student['preferences'])
                print(f"\nThe student {student['name']} has been accepted in the specialty {accepted_specialization}.")

    def _find_accepted_specialization(self, preferences):
        return preferences[0]

admission_system = UniversityAdmissionSystem()
