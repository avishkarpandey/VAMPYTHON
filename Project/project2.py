def dollarTorupees():
    rupees = 84.01
    dollar = float(input("Enter the value of dollar"))
    x = dollar * rupees
    print(f"{dollar} Dollar to Rupees = {x} Rupees")

def rupeesTodollar():
    y = 84.01
    rupees = float(input("Enter the value of rupees"))
    x = rupees / y
    print(f"{rupees} rupees to Dollar = {x}Dollar")

a = int(input("Enter 1 to convert dollar to rupees and 2 to convert rupees to dollar "))
print(a)
if a == 1 :
    dollarTorupees()
elif a == 2 :
    rupeesTodollar()
else :
    print("You have entered a wrong value")
    