import pandas as pd
import numpy as np

# read excel
# !!! put .xlsx file into the same folder with python files !!!
# !!! use .xlsx file uploaded in GitHub, DON'T use the file from canvas !!!
data_frame = pd.read_excel('2324MScCW2DataBelfast centre.xlsx', sheet_name='Sheet1')
# get data, in array
date = data_frame["Date"].values
pm25 = data_frame["PM2.5"].values
no2 = data_frame["NO2"].values
o3 = data_frame["O3"].values
tem = data_frame["temperature"].values
hum = data_frame["humidity"].values


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


# testing
data1 = np.array([1, 2, 3, 4, 5, 6, 7])  # define the 1st array
data2 = np.array([0, 4, 5, 6, 7, 8, 9])  # define the 2nd array
outlier_pos = outlier_finder(data1, 4)  # find the pos of elements in 2 array that greater than 4
data1, data2 = outlier_remover(data1, data2, outlier_pos)  # remove elements in 2 array that greater than 4
print("array 1: ", data1, "\narray 2: ", data2, "\nelements at position", outlier_pos, "is removed")  # show results
