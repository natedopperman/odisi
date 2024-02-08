# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:41:18 2024

@author: cjako, nopperman
"""

from quickParseODiSI import parse_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://plotly.com/python/contour-plots/ uses contour module from plotly, see link for more info

data = parse_data(r"G:\Shared drives\GeoD\research\fiber_data\steeldeck_data\121523 test\121523_test_2023-12-15_18-24-10_ch2_full.tsv") ### make sure there is a tare
strain_gauge = pd.read_excel(r'C:\Users\natha\Documents\coding\excel\SLT5.xlsx')
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
strain_gauge = strain_gauge.values.flatten()

# Replace values outside 1 standard deviation with zeros
# values[(values > std) | (values < -std)] = 0



position = position.values.flatten()
time = time.values.flatten()
values = values.values.T


#plotting

#set font size

plt.rcParams.update({'font.size': 14})

# set x and y limits based on values from the experiment

xmin = -800
xmax = 800
ymin = 0
ymax = 2582.8

# choose the gage you want to plot

gage_to_plot = 1696

# creating figure, scaling

fig, ax = plt.subplots(figsize=(6, 12))

#plot strain data

ax.plot(values[gage_to_plot,:], time, linewidth = 2.0, color = 'r')

#ax.plot(strain_gauge, time[0:15192], linewidth = 2.0, color = 'r')

# testing horizontal plot

#at_time = [1500]*len(values[gage_to_plot,:])
#x = np.linspace(xmin, xmax, len(values[gage_to_plot,:]))

#ax.plot(x,at_time)

# setting axes

ax.set(xlim=(xmin, xmax),ylim=(ymin, ymax))

# Set labels and title
ax.set_xlabel('Strain (microstrain)')
ax.set_ylabel('Time (s)')
ax.set_title('Strain in FLT2 gauge 1696')

plt.grid()

# showing plot
plt.show()
