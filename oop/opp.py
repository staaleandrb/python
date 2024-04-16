class Vehicle:
    def __init__(self,name, max_speed, mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        capacity = 50
        super().__init__(name, max_speed, mileage,capacity)
        


class Car(Vehicle):
    def __init__(self, name, max_speed, mileage):
        capacity = 5
        super().__init__(name, max_speed, mileage,capacity)

    

School_bus = Bus("School Volvo", 180, 12)
bil = Car("bil", 200, 15)

print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

print(School_bus.seating_capacity())