from pymongo import MongoClient

# create mongo client connection
client = MongoClient("mongodb://localhost:27017/")

#create new database for todoApp
mydb = client["todoDB"]

#create friend collection in todoApp
myfriendlist = mydb["friendlist"]

#add the list of three firends
friend = [{"name":"Rahul","age":25,"gender":"male"},{"name":"Aniket","age":25,"gender":"male"},{"name":"Aman","age":22,"gender":"male"}] 

#update the firendlist
name = {"name":"Rahul Agrahari"}
myfriendlist.update_one({'age':25}, {"$set":name})
#get the friend list
friends = myfriendlist.find()
for data in friends:
    print(data)