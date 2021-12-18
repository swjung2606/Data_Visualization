# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:41:02 2021

@author: Sungwoo Jung
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import squarify


'''
### Treemap ###

plt.figure(figsize=(6,4))
squarify.plot(sizes=[33,22,15,45], label=["Area A", "Area B", "Area C", "Area D"],
              color=["yellowgreen", "green", "gold", "beige"], alpha=0.91)
plt.axis("off")
plt.title("Sample Treemap - Matplotlib & Squarify")
plt.show()
'''


### ANNOTATION ###

n = 12
X = np.arange(12)
Y1 = (1 - X/float(n)) * np.random.uniform(1.5, 2.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(1.5, 2.0, n)

plt.bar(X, +Y1, facecolor="#6666ff", edgecolor="white")
plt.bar(X, -Y2, facecolor="#ff4444", edgecolor="white")

for x,y in zip(X,Y1):
    plt.text(x+0.2, y+0.05, "%.2f" % y, ha="center", va="bottom")

for x,y in zip(X,Y2):
    plt.text(x+0.05, -1*(y+0.2), "%.2f" % y, ha="center", va="bottom")
    
plt.annotate("Example of annotation in reference to data",
             xy=(8,0), xycoords="data", xytext=(5, 1.5),
             arrowprops = dict(facecolor="blue", shrink=0.10), 
             horizontalalignment="left", verticalalignment="center")
plt.title("Example of bi-directional bar chart with annotations")
plt.ylim(-2.5, +2.5)
plt.show()
