import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
years = np.array([2020, 2021, 2022, 2023, 2024])
sales = np.array([89, 92, 95, 88, 99])
plt.title("Sale Growth of JIO")
plt.plot(years, sales, marker = 'o')
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()