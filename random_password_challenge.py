import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
length = 12
password_list = [random.choice(characters) for i in range(length)]
random.shuffle(password_list)
password = "".join(password_list)
print("Generated password:", password)