# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:56:33 2021

@author: Sungwoo Jung
"""

import matplotlib.pyplot as plt
import numpy as np

# define the figure and axes
fig = plt.figure(figsize=(10,12))
ax = fig.add_subplot(111, projection="3d")

# Create the grid mesh with a polar coordinates type
# use the values of RHO - r and PHI - p to determine Theta - Z

r = np.linspace(0, 5/3.6, 100) # define RHO
p = np.linspace(0, 2.2*np.pi, 100) # define PHI
R,P = np.meshgrid(r,p)
Z = ((R**2 - 0.989)**2) # define theta

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface - Use a Spectral color map
ax.plot_surface(X,Y,Z, cmap=plt.cm.Spectral)

# Tweak the limits and add laTeX based mathematical labels.
ax.set_zlim(0,1.4) # Set Z-axis
ax.set_xlabel(r"$\phi_\mathrm{real}$", fontsize=18)
ax.set_ylabel(r"$\phi_\mathrm{imaginary}$", fontsize=18)
ax.set_zlabel(r"$V(\phi)-Phi$", fontsize=12)
plt.title("3D Surface Chart example")
plt.show()
