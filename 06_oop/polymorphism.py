class Shape:
    def draw(self):
        print("Drawing a Shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

# Testing Polymorphism
shapes = [Circle(), Rectangle(), Shape()]

for shape in shapes:
    shape.draw()