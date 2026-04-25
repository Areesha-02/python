
import random
import string

def generate_password():
    length = 8
    password = ""
    characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(length):
        password += random.choice(characters)

    return password


print(generate_password())