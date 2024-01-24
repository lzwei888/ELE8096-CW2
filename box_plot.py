import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read excel
# !!! change 'C:\\Users\\18519\\Desktop\\ELE8096-CW2\\2324MScCW2DataBelfast centre.xlsx' to your path !!!
data_frame = pd.read_excel('2324MScCW2DataBelfast centre.xlsx', sheet_name='Sheet1')
# get data, in array
date = data_frame["Date"].values
pm25 = data_frame["PM2.5"].values
no2 = data_frame["NO2"].values
o3 = data_frame["O3"].values
tem = data_frame["temperature"].values
hum = data_frame["humidity"].values

# box plot for pm25, no2, o3
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(9, 4))
plt.grid(True)
box_pm25 = axes[0].boxplot(pm25,
                           notch=True,
                           vert=True,
                           patch_artist=True)
box_no2 = axes[1].boxplot(no2,
                          notch=True,
                          vert=True,
                          patch_artist=True)
box_o3 = axes[2].boxplot(o3,
                         notch=True,
                         vert=True,
                         patch_artist=True)
# set label
label = ["PM2.5", "NO2", "O3"]
for i in range(3):
    axes[i].set_xlabel(label[i])

plt.show()
