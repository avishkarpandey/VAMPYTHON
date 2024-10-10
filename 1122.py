#Types of Graph
#show data in graph-line(x,y), pie(x), bar(x,y), scatters(x,y)
#Making a line graph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
years = np.array([2021, 2022, 2023, 2024])
grades = np.array([61, 65, 64, 74])
#Repersenting a line graph
plt.plot(years, grades, marker = 'o')
#to add title to the graph
plt.title("Academic Growth")
#set the name for x, y axis 
plt.xlabel("Passing Years")
plt.ylabel("Student Marks")
plt.show()