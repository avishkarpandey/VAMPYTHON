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

# #create table in my sql
# createTable1 = "create table if not exists table1(name text, email text);"
# mycursor.execute(createTable1)
# myconnection.commit()

# # add new record in database
# insertQuerry = "insert into table1 values('{}', '{}');".format(input("Enter name"), input("Enter email"))
# mycursor.execute(insertQuerry)
# myconnection.commit()

# # retrive records form database
# selectQuerry = "select * from table1;"
# mycursor.execute(selectQuerry)
# for table1 in mycursor.fetchall():
#     print(table1)
# myconnection.commit()

# # retrive the specific record under the specific condition using 'where' clause
# wherequerry = "select * from table1 where email = '{}';".format(input("Enter enter the email you want to search"))
# mycursor.execute(wherequerry)
# for table1 in mycursor.fetchall():
#     print(table1)
# myconnection.commit()

# # #update an existing record
# updateQuerry = "update table1 set name = 'rohit' where email = 'rahul@gmail.com';"
# mycursor.execute(updateQuerry)
# myconnection.commit()

# #delete the record form database
# deleteQuerry = "delete from table1 where email = 'rahul@gmail.com';"
# mycursor.execute(deleteQuerry)
# myconnection.commit()


