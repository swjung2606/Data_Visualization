# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:27:36 2021

@author: Sungwoo Jung
"""

import matplotlib.pyplot as plt
import numpy as np
import random


### Simple Bar chart part ###


plt.style.use("default")

year = [2008, 2009, 2010, 2011, 2012, 2013, 2014,
        2015, 2016, 2017, 2018, 2019, 2020]

revenue = [37.5, 42.9, 65.2, 108.2, 156.5, 170.9, 
           182.8, 233.7, 215.6, 229.2, 265.6, 260.2, 274.5]

plt.bar(year, revenue, color="purple")
plt.title("Technology revenues in billions of US $ dollar")
plt.xlabel("Year")
plt.ylabel("revenue")
plt.show()




### Multi Data Bar Chart ###

year1 = [2008, 2009, 2010, 2011, 2012, 2013, 2014,
        2015, 2016, 2017, 2018, 2019]
# There are public data for big tech giants

com1 = [37.5, 42.9, 65.2, 108.2, 16.5, 170.9, 182.8, 
        233.7, 21.6, 229.2, 265.6, 260.2 ]
com2 = [60.42, 58.44, 62.48, 69.94, 73.72, 77.85, 86.83, 
        93.58, 85.32, 89.95, 110.36, 125.84]
com3 = [21.8, 23.7, 29.3, 37.9, 50.18, 55.51, 65.67, 
        74.54, 89.98, 110.55, 136.36, 160.74]
com4 = [19.17, 24.51, 34.2, 48.08, 61.09, 74.45, 88.99, 
        107.01, 135.99, 177.87, 232.89, 280.52]

# Let's build a bar chart with a purple color filling
barWid = 0.18

# Define a subplot
fig = plt.subplots(figsize = (15,15))
reference_array = np.arange(len(year1))
com1bar = [x - 2*barWid for x in reference_array]
com2bar = [x - barWid for x in reference_array]
com3bar = reference_array
com4bar = [x + barWid for x in reference_array]

# Make the plot
# Use different edge colors and bar colors
plt.bar(com1bar, com1, color="purple", width = barWid,
        edgecolor="skyblue", label="Tech company-1")
plt.bar(com2bar, com2, color="yellow", width=barWid,
        edgecolor="green", label="Tech company-2")
plt.bar(com3bar, com3, color="violet", width=barWid,
        edgecolor="black", label="Tech company-3")
plt.bar(com4bar, com4, color="blue", width=barWid,
        edgecolor="yellow", label="Tech company-4")

plt.xlabel("Year of Reporting", fontweight="bold")
plt.ylabel("Annual Revenue( US $)", fontweight="bold")
# It shows year1 on x-axis. 
plt.xticks([r-barWid for r in range(len(year1))], year1)


plt.title("Revenues in Billions of US $Dollar")
plt.legend()
plt.show()





### Horizontal Bar Chart ###

'''

height = np.random.randint(100, size=4)

# define the names of the bars
bars = ("One","Two","Three","Four")

# define the position in y-axis
pos = np.arange(len(bars))

# Let us define some patters to fill the bar and colors to choose from
patterns = ("-","+","x","\\","*",".")
colorlist = ("violet","indigo","blue","yellow","orange",
             "red","green","purple","skyblue")

# Create horizontal bars
plt.barh(pos, height, hatch=random.choice(patterns),
         color=random.choice(colorlist),
         edgecolor=random.choice(colorlist))

plt.yticks(pos,bars)
plt.show()

'''
