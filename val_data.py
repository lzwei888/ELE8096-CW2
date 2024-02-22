import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import data
from scipy.optimize import curve_fit
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


def model_fit(x, y, N):
    if N == 2:
        func = func2
    elif N == 3:
        func = func3
    elif N == 4:
        func = func4
    x_name = var_name(x)
    y_name = var_name(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    coe, _ = curve_fit(func, x_train, y_train)
    y_pred = func(x_test, *coe)
    # plot
    x_fit = np.array([i for i in range(0, 120)])
    y_fit = func(x_fit, *coe)
    plt.scatter(x_train, y_train, color='blue', label='Training data')
    plt.scatter(x_test, y_test, color='green', label='Testing data')
    plt.plot(x_fit, y_fit, color='r', linewidth=2, label='Fitted curve')
    plt.title(x_name + " - " + y_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.show()

    mse = mean_squared_error(y_test, y_pred)
    print('Mean Squared Error:', mse)

    i, j = len(coe) - 1, 0
    while i != 0:
        print(coe[j], "x^" + str(i), end=" + ")
        i -= 1
        j += 1
    print(coe[-1])


def func2(x, a, b, c):
    return a * x ** 2 + b * x + c


def func3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def func4(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e


def var_name(var, all_var=locals()):
    return [var_name for var_name in all_var if all_var[var_name] is var][0]


# NO2, O3 = group_remover(no2, o3)
# model_fit(NO2, O3)

NO2, PM25 = group_remover(no2, pm25)
model_fit(NO2, PM25, 3)

# data_df = pd.DataFrame(no2, o3)
# writer = pd.ExcelWriter('test.xlsx')
# data_df.to_excel(writer, 'page_1', float_format='%.5f')
# writer.save()
