class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        final_fare = base_fare + (base_fare * 0.10)
        return final_fare

School_bus = Bus("School Volbo", 180, 12, 50)

print("Total Bus fare is:", School_bus.fare())