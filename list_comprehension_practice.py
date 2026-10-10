user_input = int(input("enter a number: "))
odd_numbers = [num for num in range(user_input) if num % 2 != 0]

print("Odd numbers:", odd_numbers)

fruits = ["apple", "banana", "cherry", "mango"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Updated fruits:", updated_fruits)