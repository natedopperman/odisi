# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:04:28 2024

@author: Nate
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from pathlib import Path

# # https://plotly.com/python/contour-plots/ uses contour module from plotly, see link for more info

# read in .pkl files from get_odisi_data.py

position = pd.read_pickle(r"C:\Users\natha\Documents\coding\fiber optics\pickle\position.pkl")
time = pd.read_pickle(r"C:\Users\natha\Documents\coding\fiber optics\pickle\time.pkl")
values = pd.read_pickle(r"C:\Users\natha\Documents\coding\fiber optics\pickle\values.pkl")

position = position.values.flatten()
time = time.values.flatten()
values = values.values.T

#plotting

# setting ranges for gage selection

min_gage = 339
max_gage = 2196

for x in range(1,43):
    timestamp = x*375
    
    values_to_plot = values[min_gage:max_gage,timestamp]
    gages_chosen = position[min_gage:max_gage]
    
    #set font and figure size
    
    plt.rcParams.update({'font.size': 12})
    fig, ax = plt.subplots(figsize=(12, 4))
    
    
    
    #plot strain data
    
    ax.plot(gages_chosen, values_to_plot, linewidth = 2.0, color = 'r')
    
    
    # setting axes
    # set x and y limits based on values from the experiment
    
    #xmin = min_gage
    #xmax = max_gage
    ymin = -1200
    ymax = 1200
    
    ax.set(ylim=(ymin, ymax))
    
    # Set labels and title
    ax.set_xlabel('Position along fiber (m)')
    ax.set_ylabel('Strain (microstrain)')
    ax.set_title('Strain  in FTL2 at t = {x}s'.format(x=timestamp))
    
    plt.grid()
    
    # save it to a file
   
    plt.savefig(r"C:\Users\natha\Documents\coding\fiber optics\timeplots\time{x}.png".format(x=x*375))
    plt.close()
    # showing plot 
    # plt.show()
    
# making movie
images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave(r"C:\Users\natha\Documents\coding\fiber optics\timeplots\gif\FTL2_movie.gif", images)