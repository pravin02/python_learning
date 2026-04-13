class Vehicle:
    wheels = 4
    name = ""
    model = ""
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def description(self):
        if not self.name:
            print(f"Name of the vehicle is not defined")
            return
        print(f"Vehicle {self.name} is {self.model}")


vehicle = Vehicle("", "")
print(f"{vehicle.wheels} this vehicle has.")
vehicle.description()

vehicle2 = Vehicle("Audi", "365")
print(f"{vehicle2.wheels} this vehicle has.")
vehicle2.description()


class Animal:
    # parameterized constructor
    def __init__(self, name, legs = 2, barks = True):
        self.name= name
        self.legs = legs
        self.barks = barks
    
    def info(self):
        print(f"This is the animal named {self.name} has {self.legs} legs.")
        if self.barks:
            print("This Animal barks")
        else:
            print("This Animal does not barks")


dog = Animal("Puppy", 4, True);
dog.info()


class Budget:

    def __init__(self, budget):
        self.budget = budget
    
    def expense(self, amount):
        self.budget -= amount
        self.report()
    
    def report(self, currency="R"):
        print(f"Budget left {currency} {self.budget}")


budget = Budget(100)
budget.expense(2)
budget.expense(50)
