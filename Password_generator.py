import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation

characters = letters + numbers + special_characters

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nYour generated password is:")
print(password)