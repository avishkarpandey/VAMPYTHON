usergender=input("Enter your gender")
userage=int(input("Enger your age"))
if usergender == "male" and userage>18 :
    print("You can apply for private job")
elif userage > 18 and usergender == "female" :
    print("You can apply for Govt job")
else :
    print("You have entered an invalid information")