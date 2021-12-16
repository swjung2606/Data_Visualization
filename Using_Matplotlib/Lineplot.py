# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:23:31 2021

@author: Sungwoo Jung
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "x" : range(1,21) ,
    "yy" : np.random.randn(20) ,
    "zz" : 2 * np.random.randn(20) + range(1,21) ,
    "ww" : 4 * np.random.randn(20) + range(1,21) ,
    "aa" : 8 * np.random.randn(20) + range(1,21) ,
    })

plt.plot("x", "yy", data=df, marker="p", markerfacecolor="blue",
         markersize=8, label="Pentagon", color="skyblue",
         linewidth=4)

plt.plot("x", "zz", data=df, marker="h", color="green", 
         linewidth=2, label="Hexagon")

plt.plot("x", "ww", data=df, marker="8", color="red",
         linewidth=2, linestyle="dashdot", label="Octagon")

plt.plot("x", "aa", data=df, marker="d", color="violet", 
         linewidth=2, linestyle="dotted", label="Diamond")

plt.title("Linechart with Multiple Line Charts")

# Show the legend that displays colors and markers
plt.legend()
plt.show()