class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My Name is {self.name}.")


class Student(Person):
    def study(self):
        print(f"{self.name} is Studying.")


class Athlete(Person):
    def play(self):
        print(f"{self.name} is Playing a Sport.")


class StudentAthlete(Student, Athlete):
    def show_details(self):
        print(f"{self.name} is Both a Student and an Athlete.")


# Testing the Class
hybrid_student = StudentAthlete("Ali")

hybrid_student.introduce()
hybrid_student.study()
hybrid_student.play()
hybrid_student.show_details()