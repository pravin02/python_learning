class Vehicle:
    wheels = 4
    name = ""
    model = ""

    def description(self):
        if not self.name:
            print(f"Name of the vehicle is not defined")
            return
        print(f"Vehicle {self.name} is {self.model}")


vehicle = Vehicle()
print(f"{vehicle.wheels} this vehicle has.")
vehicle.name = "Audi"
vehicle.model = "Audi3"
vehicle.description()
