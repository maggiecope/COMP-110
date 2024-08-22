"""
Module: comp110_lab08

Starter code for COMP110 lab 08.
"""

import sys
import math
import matplotlib.pyplot as pp
from imageio import imread




def get_eq_locs(filename):
    """
    Returns a tuple containing a list of latitudes and longitudes for
    earthquakes in a file.
    """

    latitudes = []
    longitudes = []

    eq_data_file = open(filename, 'r')

    #makes lists of latitudes and longitudes given in the file 
    for line in eq_data_file:
        vals = line.split(',')
        latitudes.append(float(vals[1]))
        longitudes.append(float(vals[2]))
    


    # To Do: Loop through the lines, adding each latitude and longitude to the lists
    # initialized above.
    # Don't forget to handle the header line before the loop.


    return (latitudes,longitudes) # Replace this with code that returns a tuple of latitudes and longitudes


def main():
    """
    Plots the locations of earthquakes on a worldmap.
    """
  

    # To Do: Call your get_eq_locs function then use pyplot's scatter function to
    # graph these.
    # The filename you should use is the full dataset (usgs_earthquakes_last_week.csv)


    # Set the image background to be a world-map
    # Don't change anything after this point.
    img = imread("world-map-full.jpg")
    pp.imshow(img, zorder=0, extent=[-180, 180, -90, 90])
    pp.axis('off')
    pp.show()


if __name__ == "__main__":
    main()
