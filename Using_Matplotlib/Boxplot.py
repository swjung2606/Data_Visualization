# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:58:07 2021

@author: Sungwoo Jung
"""

import numpy as np
import matplotlib.pyplot as plt


### Single Dataset ###

np.random.seed(196998801)
spread = np.random.rand(40) * 80
center = np.ones(20) * 40
filter_high = np.random.rand(8)*80 + 80
filter_low = np.random.rand(8) * (-80)
blue_plus = dict(markerfacecolor="b", marker='+')

# Merge all data
data = np.concatenate((spread,center,filter_high,filter_low))

fig, ax = plt.subplots(2,3,figsize=(16,10))
ax[0,0].boxplot(data)
ax[0,0].set_title("Basic Plot")
ax[0,1].boxplot(data, notch=True)
ax[0,1].set_title("Notched Plot")
ax[0,2].boxplot(data, flierprops=blue_plus)
ax[0,2].set_title("Change outlier")

ax[1,0].boxplot(data, showfliers=False)
ax[1,0].set_title("Removed outliers")
ax[1,1].boxplot(data, vert=False, flierprops=blue_plus)
ax[1,1].set_title("Horizontal Plot")
ax[1,2].boxplot(data, flierprops=blue_plus, whis=0.6)
ax[1,2].set_title("Shorter Whisker size")
plt.show()



### Multiple Datasets ###

np.random.seed(196998802)
spread1 = np.random.rand(40) * 80
center1 = np.ones(20) * 40
flier_high1 = np.random.rand(8) * 80 + 80
flier_low1 = np.random.rand(8) * (-80)
indigo_triangle = dict(markerfacecolor="indigo", marker="v")
data1 = np.concatenate((spread1, center1, flier_high1, flier_low1))
data2 = np.concatenate((spread1 / 2, center / 2, 
                        flier_high1 / 2, flier_low1 / 2))
data3 = np.concatenate((spread1 * 2, center1 * 2, flier_high1 * 2,
                        flier_low1 * 2))

datasets = [data1, data2, data3]

fig1 , ax1 = plt.subplots()
ax1.set_title("Multiple Samples with Different sizes")
ax1.boxplot(datasets)
plt.show()