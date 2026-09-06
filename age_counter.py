try:
    user_input = input("please enter your age: ")
    age = int(user_input)
    if age % 2 == 0:
        print("your age is an even number.")
    else:
        print("your age is an odd number.")

except ValueError:
    print("please enter a valid whole number. letters, decimals, and special characters are not allowed.")