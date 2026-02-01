class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Dunder Method For String Representation
    def __str__(self):
        return f"Name Is {self.name} And Marks Are {self.marks}"

    # Dunder Method For Addition Operator
    def __add__(self, other):
        return self.marks + other.marks

# Creating Objects
s1 = Student("Ali", 80)
s2 = Student("Ahmed", 90)

print(s1)
print(s2)
print(s1 + s2)