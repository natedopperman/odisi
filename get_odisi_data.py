# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:38:03 2024

@author: Nate
"""

from quickParseODiSI import parse_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://plotly.com/python/contour-plots/ uses contour module from plotly, see link for more info

data = parse_data(r"G:\Shared drives\GeoD\research\fiber_data\steeldeck_data\121523 test\121523_test_2023-12-15_18-24-10_ch2_full.tsv") ### make sure there is a tare
# using the quickParseODiSI function, import all the data from the file

time = data['Time']
tare = data['Data']['Tare']
values = data['Data']['Values']
position = data['Location']['Location_Values']

# Convert to DataFrames if not already
time = pd.DataFrame(time)
position = pd.DataFrame(position)
values = pd.DataFrame(values)
values = values.fillna(0)
mean_val = values.values.mean()
std = values.values.std(ddof=1)

# Saving data to pickle files in \pickle\file.pkl. make the

time.to_pickle(r"C:\Users\natha\Documents\coding\fiber optics\pickle\test.pkl")
#position.to_pickle('position.pkl')
#values.to_pickle('values.pkl')

# Replace values outside 1 standard deviation with zeros
# values[(values > std) | (values < -std)] = 0



# position = position.values.flatten()
# time = time.values.flatten()
# values = values.values.T

# #plotting

# #set font size

# plt.rcParams.update({'font.size': 12})

# # set x and y limits based on values from the experiment

# # xmin = 0
# # xmax = 800
# # ymin = 0
# # ymax = 2582.8

# values_to_plot = values[339:2196,10310]
# gages_chosen = position[339:2196]
# # creating figure, scaling

# fig, ax = plt.subplots(figsize=(12, 4))

# #plot strain data

# ax.plot(gages_chosen, values_to_plot, linewidth = 2.0, color = 'r')


# # setting axes

# #ax.set(xlim=(xmin, xmax),ylim=(ymin, ymax))

# # Set labels and title
# ax.set_xlabel('Position along fiber (m)')
# ax.set_ylabel('Strain (microstrain)')
# ax.set_title('Strain  in FTL2 at t = 1650s')

# plt.grid()

# # showing plot
# plt.show()