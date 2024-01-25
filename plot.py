import pandas as pd
from matplotlib import pyplot as plt

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

# plt.show()

# temperature as x-axis
fig2, axes2 = plt.subplots(nrows=1, ncols=3, figsize=(9, 4))
axes2[0].scatter(tem, pm25)
axes2[1].scatter(tem, no2)
axes2[2].scatter(tem, o3)
for i in range(3):
    axes2[i].set_xlabel(label[i])

# humidity as x-axis
fig3, axes3 = plt.subplots(nrows=1, ncols=3, figsize=(9, 4))
axes3[0].scatter(hum,pm25)
axes3[1].scatter(hum,no2)
axes3[2].scatter(hum,o3)
for i in range(3):
    axes3[i].set_xlabel(label[i])

plt.show()