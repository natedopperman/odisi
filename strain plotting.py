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

# Replace values outside 1 standard deviation with zeros
# values[(values > std) | (values < -std)] = 0



position = position.values.flatten()
time = time.values.flatten()
values = values.values.T

#gage = position[1692:1694] # selecting gages we want
#result = values[1692:1694] # making sure we only have values from the selected gages


#plotting

#set font size

plt.rcParams.update({'font.size': 14})

xmin = -800
xmax = 800
ymin = 0
ymax = 2582.8

zero = [0]*len(time)

fig, ax = plt.subplots(figsize=(6, 12))

#plot strain data

ax.plot(values[1692,:], time, linewidth = 2.0, color = 'r')

# setting axes

ax.set(xlim=(xmin, xmax),ylim=(ymin, ymax))

# Set labels and title
ax.set_xlabel('Strain (microstrain)')
ax.set_ylabel('Time (s)')
ax.set_title('Strain at gage #1692 for fiber 2')

plt.grid()

# showing plot
plt.show()
