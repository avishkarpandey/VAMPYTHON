import numpy  as np
import pandas as pd
a = np.arange(50)
print(a.min()) # shows the min value
print(a.max()) # show the max value 
print(a.mean()) #shows the mean of the array
print(a.shape) #show the dimenssion
mydata = a.reshape(5,10) # 5 is no. of rows and 10 is no. of col 
print(mydata) 
print(a)
