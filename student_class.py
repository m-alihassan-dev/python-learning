class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")


# Creating Student Objects
student1 = Student("Ali", 1, 99)
student2 = Student("Hassan", 2, 95)

# Displaying Student Information
student1.display_info()
student2.display_info()