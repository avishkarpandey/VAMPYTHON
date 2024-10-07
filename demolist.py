#Example of data set

myList=["Pawan","Kshitij","Harshit",]
mytuple=("Pawan","Kshitij","Harshit",)
myset={"Pawan","Kshitij","Harshit", }
mydict ={"Name":"Pawan","age":20, }
convertlist = list(mytuple)
print(type(convertlist))
convertlist.append("avishkar")
print(convertlist)
convertlist.pop(2)
print(convertlist)
qwe=tuple(convertlist)
print(type(qwe))