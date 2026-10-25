class BMW:
    def fuel_type(self):
        print("BMW fuel type: Diesel")

    def max_speed(self):
        print("BMW max speed: 250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type: Petrol")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")

car_bmw = BMW()
car_ferrari = Ferrari()

for car in (car_bmw, car_ferrari):
    car.fuel_type()
    car.max_speed()
    print("-" * 25)