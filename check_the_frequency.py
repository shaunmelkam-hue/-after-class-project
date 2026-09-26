test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:", test_dict)
user_value = int(input("Enter the frequency value to check:"))
count = 0
for key in test_dict:
    if test_dict[key] == user_value:
        count += 1

print(f"The frequency of value {user_value} is {count}")