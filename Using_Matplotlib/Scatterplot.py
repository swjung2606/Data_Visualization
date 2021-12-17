# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 08:56:46 2021

@author: Sungwoo Jung
"""

import matplotlib.pyplot as plt
import numpy as np
from math import *


# Set a seed
np.random.seed(1968)
number = 20

# np.random.rand(a,b) 
# Generate a x b size matrix where elements are between 0 and 1
x = np.random.rand(number)
y = np.random.rand(number)

# set a color
colors = np.random.rand(number)
# choose a size for the scatter point
area = (40 * np.random.rand(number))**2

plt.figure()
plt.subplot(1,2,1)
plt.scatter(x, y, c=colors, alpha=0.8)
plt.title("Without setting s", fontweight="bold")

plt.subplot(1,2,2)
plt.scatter(x, y, s=area, c=colors, alpha=0.8)
plt.title("With setting s", fontweight="bold")

plt.show()



### Rainbow color example ###
'''
import matplotlib.cm as cm

x1 = np.arange(50)
y1 = [(i*x1)**0.5 for i in np.linspace(0.5,1,10)]
colors1 = cm.rainbow(np.linspace(0,1,len(y1)))

for y,c in zip(y1, colors1):
    plt.scatter(x1,y,color=c)

plt.title("Scatter chart in a liner manner")
plt.show()
'''
