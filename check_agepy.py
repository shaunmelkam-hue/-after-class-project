age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("Enrollment successful!")
    else:
        print("Enrollment failed you are older than 20.")
else:
    print("Enrollment failed you are younger than 10.")