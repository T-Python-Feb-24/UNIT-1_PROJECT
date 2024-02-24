class University:
    def __init__(self, name, location, colleges=None, registration_system=None):
        self.name = name
        self.location = location
        self.colleges = colleges if colleges is not None else []
        self.registration_system = registration_system

    def add_college(self, college):
        self.colleges.append(college)

    def display_info(self):
        print(f"University Name: {self.name}")
        print(f"Location: {self.location}")
        print("Colleges:")
        for college in self.colleges:
            print(f" - {college}")
        print(f"Registration System: {self.registration_system}")