import matplotlib.pyplot as plt
from scipy import stats as st
import numpy as np

age = [20, 30, 40, 50, 60]
salary = [20000, 75000, 55000, 60000, 25000]

from sklearn.metrics import r2_score
futureData = np.poly1d(np.polyfit(age, salary, 3))
print(r2_score,salary, futureData(35))


