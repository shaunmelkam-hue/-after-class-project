def calculate_change(paid, bill):
    change = paid - bill
    return change

money_returned = calculate_change(4.00, 2.50)
print(f"The shopkeeper should return: {money_returned}$")