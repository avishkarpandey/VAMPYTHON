import numpy as np
#create numpy array to store 
#friend name edit 
myFriends = np.array(["avi       ","jai     ","harshit          ","divyansh        "])
print(myFriends)
print(type(myFriends))
#printitng truough  numpy array
print("normal array")
for i in myFriends:
    print(i)
#updating a numpy array
print("updated array")
myFriends[0] = "avi pandey"
myFriends[1] = "jai chauhan"
myFriends[2] = "harshit dhingra"
myFriends[3] = "divyansh tyagi"
for i in myFriends:
    print(i)
#sort a numpy  array
print("sorted arrya")
myFriends = np.sort(myFriends)
for i in myFriends:
    print(i)
#reverse sort of numpy array methord 1
print("reversed array methord 1")
myFriends =  np.sort(myFriends)[::-1]
for i in myFriends:
    print(i)
#reverse sort of numpy array methord 2
print("reversed array methord 2")
myFriends =  np.flip(myFriends)
for i in myFriends:
    print(i)
#reverse sort of numpy array methord 3
print("reversed array methord 3")
y = 3
while y>=0:
    print(myFriends[y])
    y = y - 1
