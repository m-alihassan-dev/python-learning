class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My Name is {self.name} and I am {self.age} Years Old.")

class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def play(self):
        print(f"I Play {self.sport}.")

class StudentAthlete(Person, Athlete):
    def __init__(self, name, age, sport, student_id):
        super().__init__(name, age) 
        self.sport = sport
        self.student_id = student_id

    def show_details(self):
        print(
            f"Student ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Sport: {self.sport}"
        )

student_athlete = StudentAthlete("Ali", 20, "Basketball", 101)

student_athlete.introduce()
student_athlete.play()
student_athlete.show_details()