import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
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


# output the information of the variable
def data_printer(arr1):
    name = var_name(arr1)
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
    n = len(outlier_pos)
    max_indices = np.argsort(arr1)[-4:]
    print(name + ": ")
    print("mean: ", np.mean(arr1))
    print("median: ", np.median(arr1))
    print("Q1: ", np.percentile(arr1, 25))
    print("Q3: ", np.percentile(arr1, 75))
    print("outliers: ", end="")
    for j in max_indices:
        print(arr1[j], end=", ")


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


# Remove outliers of 3 variables for Multi-variable Regression Model
def outlier_remover2(data1, data2, data3, outlier_pos):
    n = len(outlier_pos)
    max_indices = np.argsort(data1)[-n:]
    data1 = np.delete(data1, max_indices)
    data2 = np.delete(data2, max_indices)
    data3 = np.delete(data3, max_indices)
    return data1, data2, data3


def group_remover2(data1, data2, data3):
    data1, data2, data3 = outlier_remover2(data1, data2, data3, outlier_finder(data1))
    data2, data1, data3 = outlier_remover2(data2, data1, data3, outlier_finder(data2))
    data3, data1, data2 = outlier_remover2(data3, data1, data2, outlier_finder(data3))
    return data1, data2, data3


# build models of 2, 3, 4-orders
def func2(x, a, b, c):
    return a * x ** 2 + b * x + c


def func3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def func4(x, a, b, c, d, e):
    return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e


# for plotting, change variable name to str for labels
def var_name(var, all_var=locals()):
    return [var_name for var_name in all_var if all_var[var_name] is var][0]


# surface model, Multi-variable Regression Model
def model_fit_3D(x, y, z, N):
    x_name = var_name(x)
    y_name = var_name(y)
    z_name = var_name(z)
    x = x.astype(float)
    y = y.astype(float)
    z = z.astype(float)

    poly = PolynomialFeatures(degree=N)
    X_poly = poly.fit_transform(np.column_stack((x, y)))

    # model fitting
    model = LinearRegression()
    model.fit(X_poly, z)

    # plot surface
    x_range = np.linspace(min(x), max(x), 50)
    y_range = np.linspace(min(y), max(y), 50)
    X, Y = np.meshgrid(x_range, y_range)
    X_flat = X.flatten()
    Y_flat = Y.flatten()
    X_poly_flat = poly.transform(np.column_stack((X_flat, Y_flat)))
    Z_flat = model.predict(X_poly_flat)
    Z = Z_flat.reshape(X.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='r', label='Original Data')
    ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis', label='Fitted Plane')

    ax.set_title(x_name + "-" + y_name + "-" + z_name)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.set_zlabel(z_name)

    plt.show()


# regression model, plot and output errors
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
    x_fit = np.array([i for i in range(6, int(max(x)) + 1)])
    y_fit = func(x_fit, *coe)
    plt.scatter(x_train, y_train, color='blue', label='Training data')
    plt.scatter(x_test, y_test, color='green', label='Testing data')
    plt.plot(x_fit, y_fit, color='r', linewidth=2, label='Fitted curve')
    plt.title(x_name + " - " + y_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(y_pred - y_test, marker='o', linestyle='None', color='blue')
    plt.title('Error Plot of $NO_2$')
    plt.xlabel('Testing Data')
    plt.ylabel('Residuals')
    plt.grid(True)
    plt.show()

    print("n = ", N, ":")
    mse = mean_squared_error(y_test, y_pred)
    print('Mean Squared Error:', mse)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("RMSE: ", rmse)
    r2 = r2_score(y_test, y_pred)
    print("R-squared: ", r2)

    i, j = len(coe) - 1, 0
    while i != 0:
        print(coe[j], "x^" + str(i), end=" + ")
        i -= 1
        j += 1
    print(coe[-1])


temperature, NO2 = group_remover(tem, no2)
model_fit(temperature, NO2, 2)
# # model_fit(temperature, NO2, 3)
# # model_fit(temperature, NO2, 4)

# temperature, O3 = group_remover(tem, o3)
# model_fit(temperature, O3, 2)
# # model_fit(temperature, O3, 3)
# # model_fit(temperature, O3, 4)


# NO2, O3, PM25 = group_remover2(no2, o3, pm25)
# x, y, z = NO2, O3, PM25
# model_fit_3D(x, y, z, 3)


# # store data into Excel
# data_df = pd.DataFrame(NO2, O3, PM25)
# writer = pd.ExcelWriter('NO2-O3-PM25.xlsx')
# data_df.to_excel(writer, 'page_1', float_format='%.5f')
# writer.save()
