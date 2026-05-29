class Employee:
    def __init__(self, name, age, salary):
        self.name = name          # Public Variable
        self._age = age           # Protected Variable
        self.__salary = salary    # Private Variable

    # Public Method
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Salary:", self.__salary)

class Manager(Employee):
    def show_manager_info(self):
        print("Manager Name:", self.name)   # Public Access
        print("Manager Age:", self._age)    # Protected Access
        # Private Variable Is Not Accessible Here

# Testing the Class
manager = Manager("Ali", 30, 50000)

manager.display_details()
manager.show_manager_info()