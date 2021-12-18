# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:03:17 2021

@author: Sungwoo Jung
"""

import matplotlib.pyplot as plt
import numpy as np
import random


### Matshow example ###

array = np.random.randint(1,100,(20,20))

fig, ax = plt.subplots()
ax.matshow(array, cmap = "viridis")

# Show each entry(number) in array on the cell.
for (i,j),z in np.ndenumerate(array):
    ax.text(j, i, "{:0.0f}".format(z), ha="center", va="center",color="w")

plt.title("Matrix Show example")
plt.show()



### My own practice_Matshow ###

mean = 50
std = 15
# For random samples from N(u,sigma^2)
x = mean + std * np.random.randn(400)

# Any entry in x should be between 1 and 100
for i in range(len(x)):
    if x[i]<=0:
        x[i] = 1
    if x[i]>=100:
        x[i] = 100

# Make x as a matrix form
x = x.reshape((20,20))

fig1, ax1 = plt.subplots()
ax1.matshow(x, cmap = "viridis")

for (i,j),z in np.ndenumerate(x):
    ax1.text(j,i, "{:0.0f}".format(z), ha="center", va="center", color="w")

plt.title("My Own Practice")
plt.show()



'''
### Violin plot ###

# np.random.normal(mean, sigma, n) : generate data that follows N(mean, sigma^2), n  is number of samples

ds1 = np.random.normal(0,6,100)
ds2 = np.random.normal(0,20,200)
ds3 = np.random.normal(0,12,400)
data = list([ds1,ds2,ds3])

fig, ax = plt.subplots()
vio_part = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=True)
for pc in vio_part["bodies"]:
    pc.set_facecolor("yellowgreen")
    pc.set_edgecolor("green")
ax.set_title("Sample Violin plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
xticklabels = ["Group1", "Group2", "Group3"]
ax.set_xticks([1,2,3])
ax.set_xticklabels(xticklabels)
ax.yaxis.grid(True)
plt.show()
'''