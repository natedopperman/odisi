# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:23:08 2023

@author: cjako
"""

from quickParseODiSI import parse_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://plotly.com/python/contour-plots/ uses contour module from plotly, see link for more info

data = parse_data(r"G:\Shared drives\GeoD\research\fiber_data\EGS_data\december_23_EGS\EGS_TEST_Y_2023-12-15_15-42-23_ch1_full.tsv")
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


# this chunk finds the min and max values
#for _ in values:
    #find_max = values.max().max()
    #find_min = values.min().min()
    
#This chunk finds the index of the min and max values 
#max_location = np.unravel_index(np.nanargmax(values), values.shape)
#min_location = np.unravel_index(np.nanargmin(values), values.shape)
# Create meshgrid for imshow plot

#set font size

plt.rcParams.update({'font.size': 22})

# Create meshgrid for imshow plot
X, Y = np.meshgrid(time, position)

# Create a subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the pcolormesh
color_plot = ax.pcolormesh(X, Y, values, cmap='bwr', shading='auto', vmax = std, vmin = -std)

# Add colorbar
cbar = plt.colorbar(color_plot, ax=ax, label=r'microstrain ($\mu\varepsilon$)')

#plotting a line at a gauge of interest

at_position = [1692.5]*len(time) #average of two gages to match strain gage length of 5mm.
x = np.linspace(xmin, xmax, len(values[gage_to_plot,:]))

ax.plot(time,at_position)
# Plot the min max
#ax.plot(time[max_location[1]], position[max_location[0]], color='lime', marker='o', label='Max Value')
#ax.plot(time[min_location[1]], position[min_location[0]], color='deeppink', marker='o', label='Min Value')

# Set labels and title
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position in Fiber (m)')
ax.set_title('Strain in Fiber')
ax.legend(framealpha=1)
# Show the plot
plt.show()

