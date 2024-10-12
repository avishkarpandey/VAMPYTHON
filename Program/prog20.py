#CREATING A CSV FILE
#creating file
mycsvfile = open("file1.csv", "w")
#writing in a file
mycsvfile.write("this is a csv file ")
#reading the csv file
mycsvfile = open("file1.csv", "r")
print(mycsvfile.read())
#deleting a csv file 
mycsvfile.close()
import os
os.remove("file1.csv")
