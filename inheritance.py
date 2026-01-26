class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} Is Eating.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} Is Barking.")


# Creating Object Of Child Class
dog = Dog("Buddy")

dog.eat()
dog.bark()