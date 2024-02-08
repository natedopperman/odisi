# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:23:08 2023

@author: cjako
"""

from quickParseODiSI import parse_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

# https://plotly.com/python/contour-plots/ uses contour module from plotly, see link for more info

data = parse_data(r"G:\Shared drives\GeoD\research\fiber_data\steeldeck_data\121523 test\121523_test_2023-12-15_18-24-10_ch3_full.tsv") ### make sure there is a tare
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

gage = position[410:2164] # selecting gages we want
result = values[410:2164] # making sure we only have values from the selected gages

# this chunk finds the min and max values
# for _ in values:
#     find_max = values.max().max()
#     find_min = values.min().min()
    
# #This chunk finds the index of the min and max values 
# max_location = np.unravel_index(np.nanargmax(values), values.shape)
# min_location = np.unravel_index(np.nanargmin(values), values.shape)


# Create meshgrid for imshow plot
X, Y = np.meshgrid(time, gage)

# Create a subplot
fig, ax = plt.subplots(figsize=(20, 12))

# Plot the pcolormesh
color_plot = ax.pcolormesh(X, Y, result, cmap='bwr', shading='auto', vmax = 1000, vmin = -1000)

# Add colorbar
cbar = plt.colorbar(color_plot, ax=ax, label=r'microstrain ($\mu\varepsilon$)')

# plotting gauge location
at_position = [4.5311]*len(time) #average of two gages to match strain gage length of 5mm.

ax.plot(time,at_position, linewidth=5.0, color = "black", linestyle = '--', label = 'location of STB5')

# plotting chosen timestamp
plt.axvline(x = 1650, color = 'black', linestyle = '--', linewidth = 5.0, label = 't = 1650s')

# Plot the min max
# ax.plot(time[max_location[1]], position[max_location[0]], color='lime', marker='o', label='Max Value')
# ax.plot(time[min_location[1]], position[min_location[0]], color='deeppink', marker='o', label='Min Value')

# Set labels and title
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position in Fiber (m)')
ax.set_title('Strain in FBL1')
ax.legend(framealpha=1)
    
# Show the plot
plt.show()

