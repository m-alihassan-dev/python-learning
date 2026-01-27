class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My Name Is {self.name} And I Am {self.age} Years Old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print("I Am A Student And I Am Studying.")


class CollegeStudent(Student):
    def __init__(self, name, age, student_id, college_name):
        super().__init__(name, age, student_id)
        self.college_name = college_name

    def attend_class(self):
        print(
            f"My Student ID Is {self.student_id} "
            f"And I Study At {self.college_name}."
        )


# Creating Object Of Multilevel Inheritance Class
student = CollegeStudent("Ali", 19, 123, "GCUF")

student.introduce()
student.study()
student.attend_class()