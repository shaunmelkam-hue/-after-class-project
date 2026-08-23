import math


def calculate_circumference(radius):

    circumference = 2 * math.pi * radius
    return circumference


test_radius = 5

result = calculate_circumference(test_radius)
print(f"The circumference of a circle with radius{test_radius} is: {result:.2f}")