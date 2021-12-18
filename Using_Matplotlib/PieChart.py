# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:30:54 2021

@author: Sungwoo Jung
"""

import numpy as np
import matplotlib.pyplot as plt


brands = ["Samsung", "Apple", "Huawei", "Xiaomi",
          "Oppo", "Others"]
data = [30.25, 26.53, 10.44, 9.67, 4.83, 18.28]
colors = ["green", "yellowgreen", "gold", "lightskyblue",
          "olive", "violet"]


fig, axs = plt.subplots(2,2, figsize=(16,10))
axs[0,0].pie(data, labels = brands)
axs[0,0].set_title("Basic Pie Plot")
axs[0,1].pie(data, labels = brands, colors=reversed(colors))
axs[0,1].set_title("Basic Pie Plot with custom colors")

axs[1,0].pie(data, labels = brands, colors = colors, autopct="%1.1f%%", 
             shadow = True, startangle = 90)
axs[1,0].set_title("With percentage Pies and colors and shadows")
axs[1,1].pie(data, labels = brands, colors = colors, explode=(0.2,0.3,0.2,0.2,0.1,0.1), 
             autopct = "%1.0f%%", shadow = True, startangle = 90)
axs[1,1].set_title("Global Mobile Phone Market share")
plt.show()