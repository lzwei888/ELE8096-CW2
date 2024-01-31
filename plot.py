import data
from matplotlib import pyplot as plt

data_array = data.data_array
# get data, in array
date = data_array[0]
pm25 = data_array[1]
no2 = data_array[2]
o3 = data_array[3]
tem = data_array[4]
hum = data_array[5]

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
axes3[0].scatter(hum, pm25)
axes3[1].scatter(hum, no2)
axes3[2].scatter(hum, o3)
for i in range(3):
    axes3[i].set_xlabel(label[i])

label2 = ["PM2.5-NO2", "PM2.5-O3", "NO2-O3"]
fig4, axes4 = plt.subplots(nrows=1, ncols=3, figsize=(9, 4))
axes4[0].scatter(pm25, no2)
axes4[1].scatter(pm25, o3)
axes4[2].scatter(no2, o3)
for i in range(3):
    axes4[i].set_xlabel(label2[i])

plt.show()
