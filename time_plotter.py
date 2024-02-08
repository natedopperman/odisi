# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:38:03 2024

@author: Nate
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # https://plotly.com/python/contour-plots/ uses contour module from plotly, see link for more info

# read in .pkl files from get_odisi_data.py

position = pd.read_pickle(r"C:\Users\natha\Documents\coding\fiber optics\pickle\position.pkl")
time = pd.read_pickle(r"C:\Users\natha\Documents\coding\fiber optics\pickle\time.pkl")
values = pd.read_pickle(r"C:\Users\natha\Documents\coding\fiber optics\pickle\values.pkl")

position = position.values.flatten()
time = time.values.flatten()
values = values.values.T

#plotting

# setting ranges for gage selection and time

min_gage = 339
max_gage = 2196
timestamp = 12000

values_to_plot = values[min_gage:max_gage,timestamp]
gages_chosen = position[min_gage:max_gage]

#set font and figure size

plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots(figsize=(12, 4))



#plot strain data

ax.plot(gages_chosen, values_to_plot, linewidth = 2.0, color = 'r')


# setting axes
# set x and y limits based on values from the experiment

# xmin = 0
# xmax = 800
# ymin = 0
# ymax = 2582.8

#ax.set(xlim=(xmin, xmax),ylim=(ymin, ymax))

# Set labels and title
ax.set_xlabel('Position along fiber (m)')
ax.set_ylabel('Strain (microstrain)')
ax.set_title('Strain  in FTL2 at t = 1650s')

plt.grid()

# save it to a file
plt.savefig(r"C:\Users\natha\Documents\coding\fiber optics\timeplots\time.png")
# showing plot
plt.show()

