class Dog:
    animal ="dog"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

print(f"Dog 1 is a {dog1.color} {dog1.breed}.")
print(f"Dog 2 is a {dog2.color} {dog2.breed}.")