class reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]

user_word = input("Enter a word: ")
obj = reverse(user_word)
print("Reversed string:", obj.reverse_string())