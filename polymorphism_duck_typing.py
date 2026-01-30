class Fan:
    def start(self):
        print("Fan is Running")

class Bike:
    def start(self):
        print("Bike is Starting")

class Computer:
    def start(self):
        print("Computer is Booting")

def power_on(machine):
    machine.start()

# Testing Polymorphism
machines = [Fan(), Bike(), Computer()]

for machine in machines:
    power_on(machine)