#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:24:49 2023

@author: nav
"""

import matplotlib.pyplot as plt
import csv

# use the data in the csv file to create the basis of the chart that will be plotted in the subsequent step
TIMESTEP = []
MEAN = []
with open('/Users/nav/Downloads/TempUpd.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row 
    for row in reader:
        TIMESTEP.append(str(row[0]))
        MEAN.append(float(row[1]))

# Plot the chart
plt.plot(TIMESTEP, MEAN)
plt.xlabel('Time (days)')
plt.ylabel('Temperature (Celsius)')
plt.title('Temperature vs Time')
plt.show()


#print out a short description about said chart
print("This figure is a Temperature vs Time plot showing the change in temperature over time, with time on the x-axis and temperature on the y-axis. There is a clear upward trend in the temperature as time passes by.")


#run several analysis such as mean & median

with open('/Users/nav/Downloads/TempUpd.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Initialize variables
    x_values = []
    y_values = []

    # Read the data into separate lists
    for row in csvreader:
        x_values.append(str(row[0]))
        y_values.append(float(row[1]))

    # Calculate the median
    sorted_y = sorted(y_values)
    n = len(sorted_y)
    median = (sorted_y[n // 2] if n % 2 == 1 else 0.5 * (sorted_y[n // 2 - 1] + sorted_y[n // 2]))

    # Calculate the average
    average = sum(y_values) / len(y_values)

    # Print the results
    print(f"Median: {median:.2f} degrees Celsius")
    print(f"Average: {average:.2f} degrees Celsius")



