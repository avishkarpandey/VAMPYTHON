from scipy import stats as st
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
# 2023: $30.4 billion
# 2022: -$2.7 billion (loss)
# 2021: $33.4 billion
# 2020: $21.3 billion
# 2019: $11.6 billion
# 2018: $10.1 billion
# 2017: $3.0 billion
# 2016: $2.4 billion
# 2015: $0.6 billion
# 2014: -$0.2 billion (loss)

year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023] 
profit = [30.0, -2.7, 33.4, 21.3, 11.6, 10.1, 3.0, 2.4, 0.6, -0.2]    # profit in billions of dollars
# plt.scatter(age, salary, marker = 'o')
# plt.show()
#Through polynamial regression

# futureSalary = np.poly1d(np.polyfit(year, profit, 3))
# print(futureSalary(2025))
# print(r2_score(profit, futureSalary(year)))

#Through leanier regression

slope, intercept, r, p, std_err = st.linregress(year, profit)
print("slope",slope, "intercept", intercept, "r", r, "p", p, "std_err", std_err)
def futureSalary(age):
    return slope * age + intercept
print(futureSalary(35))



