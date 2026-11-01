class RomanConverter:
    def int_to_roman(self, num: int) -> str:
        
        val_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')

        ]
        
        roman_num = ""

        for value, numeral in val_map:
            while num >= value:
                roman_num += numeral
                num -= value

        return roman_num

if __name__ == "__main__":
    user_input = int(input("Enter an integer to convert: "))
    converter = RomanConverter()
    result = converter.int_to_roman(user_input)
    print(f"The Roman numeral eqivalent is: {result}")