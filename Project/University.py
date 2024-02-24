class University:
    def __init__(self, name, location, specialties=None, registration_system=None):
        self.name = name
        self.location = location
        self.specialties = specialties if specialties is not None else []
        self.registration_system = registration_system

    def add_specialty(self, specialty):
        self.specialties.append(specialty)

    def display_info(self):
        print(f"University Name: {self.name}")
        print(f"Location: {self.location}")
        print("specialties:")
        for specialty in self.specialties:
            print(f" - {specialty}")
        print(f"Registration System: {self.registration_system}")