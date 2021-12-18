# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:44:49 2021

@author: Sungwoo Jung
"""


import matplotlib.pyplot as plt
import numpy as np



### Donut Chart ###

brands = ["Samsung", "Apple", "Huawei", "Xiaomi", "Oppo", "Others"]
data = [30.25, 26.53, 10.44, 9.67, 4.83, 18.28]
colors = ["green", "yellowgreen", "gold", "lightskyblue", "olive", "violet"]

# Create a circle for the center of the plot
my_circle = plt.Circle((0,0), 0.7, color="white")
plt.pie(data, labels=brands, wedgeprops = {"linewidth": 7, "edgecolor": "white"}, colors = colors)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title("Global smartphone market share")
plt.show()



### Area Charts ###

plt.figure(figsize=(10,6))
x = range(1,8)
y = [[1,4,6,8,9,11,14], [2,2,7,10,12,8,12], [2,8,5,10,6,10,12]]
plt.stackplot(x, y, labels = ["Series 1", "Series 2", "Series 3"])
plt.legend(loc = "upper left")
plt.title("Basic Area Chart")
plt.show()
