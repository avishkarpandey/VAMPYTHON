mypassword = open("firstname.txt", "w")
mypassword.write("my name is avi")
mypassword = open("firstname.txt", "r")
mydata = mypassword.read()
if "is" in mydata:
    print("yes")
else :
    print("no")