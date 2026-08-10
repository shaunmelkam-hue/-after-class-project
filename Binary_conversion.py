decimal_num = int(input("Enter a decimal number: "))
original_num = decimal_num
binary_str = ""

if decimal_num == 0:
    binary_str = "0"

while decimal_num > 0:
    remainder = decimal_num % 2
    binary_str = str(remainder) + binary_str
    decimal_num = decimal_num // 2

print(f"The binary representation of {original_num} is: {binary_str}")