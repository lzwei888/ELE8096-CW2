import numpy as np
from sklearn.linear_model import LinearRegression
import data

data_array = data.data_array
# get data, in array
date = data_array[0]
pm25 = data_array[1]
no2 = data_array[2]
o3 = data_array[3]
tem = data_array[4]
hum = data_array[5]


# find locations of elements in array that greater than threshold value
def outlier_finder(data, threshold):
    outlier_pos = []
    for i in range(len(data)):
        if data[i] > threshold:
            outlier_pos.append(i)
    return outlier_pos


# remove values in the 2 array at the same time
def outlier_remover(data1, data2, outlier_pos):
    index = np.flip(outlier_pos)
    for i in index:
        data1 = np.delete(data1, i)
        data2 = np.delete(data2, i)
    return data1, data2


# # testing
# data1 = np.array([1, 2, 3, 4, 5, 6, 7])  # define the 1st array
# data2 = np.array([0, 4, 5, 6, 7, 8, 9])  # define the 2nd array
# outlier_pos = outlier_finder(data1, 4)  # find the pos of elements in 2 array that greater than 4
# data1, data2 = outlier_remover(data1, data2, outlier_pos)  # remove elements in 2 array that greater than 4
# print("array 1: ", data1, "\narray 2: ", data2, "\nelements at position", outlier_pos, "is removed")  # show results

# fit linear regression
tem_pm25 = LinearRegression().fit(tem.reshape(-1, 1), pm25)
print(tem_pm25.score(tem.reshape(-1, 1), pm25))
