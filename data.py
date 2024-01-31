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

data_array = np.array([date, pm25, no2, o3, tem, hum])

