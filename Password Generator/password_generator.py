# Modules string 
import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digit = string.digits
puntc = string.punctuation

# print(lowercase)
# print(uppercase)
# print(digit)
# print(puntc)

user = int(input("Enter length of password: "))

s = []
s.extend(list(lowercase))
s.extend(list(uppercase))
s.extend(list(digit))
s.extend(list(puntc))

random.shuffle(s)

print("".join(s[0:user]))