import mysql.connector

#establish the connection for mysql database
myconnection = mysql.connector.connect(host = "localhost", username = "root", password = "Av@12345", database = "event")

#to verify the connection
if myconnection.is_connected():
    print("DB connected")
else :
    print("DB not connected")

#to pass the data execution using cursor
mycursor = myconnection.cursor()

#create table in my sql
firstTable = "Create table event(id integer primary key,task text,venue text);"
mycursor.execute(firstTable)
myconnection.commit()


