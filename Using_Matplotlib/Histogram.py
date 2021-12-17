# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:35:37 2021

@author: Sungwoo Jung
"""

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

'''
### Simple case ###
np.random.seed(19681)
x = np.random.randn(750)
# num_bins = number of bars
num_bins = 15

fig, ax = plt.subplots()
# n 은 막대기 갯수(15개)를,
# bins 는 각 막대기 좌측 하단과 x 축이 만나는 값을 나타낸다.
# 즉, bins 는 n 보다 항상 1이 더 많음.
n, bins, patches = ax.hist(x, num_bins, density=False,
                           color="skyblue",edgecolor="green",
                           histtype="bar",orientation="vertical")

ax.set_xlabel("Distribution")
ax.set_title(r"Histogram")
fig.tight_layout()
plt.show()
'''



### Example 1 ###

np.random.seed(190007)
mu = 120
sigma = 11

# generate example data
# 평균과 표준편차를 바탕으로 한 랜덤 값이 10만개 생성.
x1 = mu + sigma * np.random.randn(100000)

fig, ax = plt.subplots()
n, num_bins, patches = ax.hist(x1, mu, density=1, color="gold")

# Gaussian distribution
# y는 num_bins 값들을 기준으로한 가우시안 분포함수 
y = ( (1 / (np.sqrt(2*np.pi) * sigma)) *
     np.exp(-0.5 * ((num_bins - mu) / sigma)**2) ) 

ax.plot(num_bins, y, ".-", color="blue")
ax.set_xlabel("Distribution")
ax.set_ylabel("Probability density")
ax.set_title(r"Histogram with values of $\mu = $ " + str(mu) + r", $\sigma = $ "+str(sigma))

fig.tight_layout()
plt.show()
