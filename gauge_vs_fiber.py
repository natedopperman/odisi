# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:39:58 2024

@author: cjako, Nate
"""

from quickParseODiSI import parse_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://plotly.com/python/contour-plots/ uses contour module from plotly, see link for more info

data = parse_data(r"G:\Shared drives\GeoD\research\fiber_data\steeldeck_data\121523 test\121523_test_2023-12-15_18-24-10_ch2_full.tsv") ### make sure there is a tare
# using the quickParseODiSI function, import all the data from the ODiSi file

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

# Replace values outside 1 standard deviation with zeros
# values[(values > std) | (values < -std)] = 0


# now read in the data from the strain gauge

strain_gauge = pd.read_excel(r'C:\Users\natha\Documents\coding\excel\SLT5.xlsx')
strain_gauge = strain_gauge.values.flatten()
position = position.values.flatten()
time = time.values.flatten()
values = values.values.T


#plotting

#set font size

plt.rcParams.update({'font.size': 14})

# choose the gage you want to plot

gage_to_plot = 1696

# creating figure, scaling

# set x and y limits based on values from the experiment

# xmin = -800
# xmax = 800
# ymin = 0
# ymax = 2582.8

fig, ax = plt.subplots(figsize=(13, 13))

#plot your data

ax.axline((0,0), slope = 1.0, color = 'black')
ax.plot(strain_gauge[0:3239], values[gage_to_plot,0:3239], linewidth = 0.8, color = 'r', label = "Loading Nonlinearity") # loading hook
ax.plot(strain_gauge[3240:10325], values[gage_to_plot,3240:10325], linewidth = 0.8, color = 'b', label = "Linear Loading") # linear loading
ax.plot(strain_gauge[10326:12546], values[gage_to_plot,10326:12546], linewidth = 0.8, color = 'g', label = "Linear Deloading") # linear deload
ax.plot(strain_gauge[12547:15190], values[gage_to_plot,12547:15190], linewidth = 0.8, color = 'magenta', label = 'Nonlinear Deloading ') # deloading hook

# setting axes

#ax.set(xlim=(xmin, xmax),ylim=(ymin, ymax))

# Set labels and title
ax.set_xlabel('Strain in SLT5')
ax.set_ylabel('Strain in gage 1696')
ax.set_title('Strain at FLT2 gage 1696 vs. strain at SLT5')
ax.legend()

plt.grid()

# showing plot
plt.show()
