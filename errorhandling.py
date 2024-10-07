#5 TypeError

amount = 400
email = "p@mail.com"
#total = amount + email

try:
    total = amount + email
except TypeError:
    print("String cannot be concatenated with integer")
