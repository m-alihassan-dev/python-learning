class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Vehicle Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def car_details(self):
        print(f"Car Model: {self.model}, Brand: {self.brand}")


class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

    def bike_details(self):
        print(f"Bike Type: {self.bike_type}, Brand: {self.brand}")


# Creating Objects
my_car = Car("Toyota", "Corolla")
my_bike = Bike("Yamaha", "Sport")

my_car.show_brand()
my_car.car_details()

my_bike.show_brand()
my_bike.bike_details()