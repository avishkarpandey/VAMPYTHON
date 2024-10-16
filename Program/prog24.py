import numpy as np
import pandas as pd
emp=np.arange(1000000)

#fired top 10 higest  paid employees
highest=pd.DataFrame(data=emp.reshape(100000  ,10))

# # print(highest.tail(1))
# # print(highest.head(1)+500)
# #tail gives by default bottom 5 rows
# # lowest=pd.DataFrame(data=emp.reshape(100000,10))
# # lowest=lowest+500
# # print(lowest.head(1))

# # print(highest.loc[[45000,55000]]+100)
# highest=pd.DataFrame(data=emp.reshape(10 ,100000))
# print(highest.loc[[5,]]+100)