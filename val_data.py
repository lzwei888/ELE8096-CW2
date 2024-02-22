import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.linear_model import LinearRegression
import data
import pandas as pd

data_array = data.data_array
# get data, in array
date = data_array[0]
pm25 = data_array[1]
no2 = data_array[2]
o3 = data_array[3]
tem = data_array[4]
hum = data_array[5]


# function to define the outliers, which is the abs(residual) > std(residual) * 2
def outlier_finder(arr1):
    outlier_pos = []
    arr1 = np.sort(arr1)
    x = np.array([i for i in range(0, len(arr1))])
    fit1 = np.polyfit(x.astype(np.float64), arr1.astype(np.float64), 1)
    poly = np.poly1d(fit1)
    pred = poly(x)
    residual = arr1 - pred
    std = 2 * np.std(residual)
    for i in range(len(residual)):
        if np.abs(residual[i]) >= 2 * std:
            outlier_pos.append(i)
    return outlier_pos

# Remove values in the 2 array at the same time
def outlier_remover(data1, data2, outlier_pos):
    n = len(outlier_pos)
    max_indices = np.argsort(data1)[-n:]
    data1 = np.delete(data1, max_indices)
    data2 = np.delete(data2, max_indices)
    return data1, data2

# Remove outliers as groups, in two related variables
def group_remover(data1, data2):
    data1, data2 = outlier_remover(data1, data2, outlier_finder(data1))
    data2, data1 = outlier_remover(data2, data1, outlier_finder(data2))
    return data1, data2


# example: remove outliers in NO2 and O3, and store the result in Excel
no2, o3 = group_remover(no2, o3)
# data_df = pd.DataFrame(no2, o3)
# writer = pd.ExcelWriter('test.xlsx')
# data_df.to_excel(writer, 'page_1', float_format='%.5f')
# writer.save()


# plot
plt.scatter(no2, o3)
plt.xlabel("NO2")
plt.ylabel("O3")
plt.title("NO2-O3 (After removing outliers)")
plt.show()
