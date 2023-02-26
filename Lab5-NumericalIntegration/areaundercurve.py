#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:12:04 2023

@author: nav
"""

import math
import scipy.integrate
import matplotlib.pyplot as plt

def y1(x):
    return -0.5 * x + 4.0

def y2(x):
    return -0.29 * x ** 2 - x + 12.5

def y3(x):
    return 1.0 + 10 * (x + 1.0) * math.exp(-x ** 2)

# user inputs data
num_rectangles = int(input("Enter the number of rectangles to use: "))
rect_width = float(input("Enter the width of the rectangles: "))

# define the limits
a = -5.0
b = 5.0

# initial area
area1 = 0.0
area2 = 0.0
area3 = 0.0

# calculate the area under each curve using the rectangle method
for i in range(num_rectangles):
    x = a + i * rect_width
    area1 += y1(x) * rect_width
    area2 += y2(x) * rect_width
    area3 += y3(x) * rect_width

# print the results
print("Area under y1 = -0.5x + 4.0:", area1)
print("Area under y2 = -0.29x^2 - x + 12.5:", area2)
print("Area under y3 = 1.0 + 10(x + 1.0)*exp(-x^2):", area3)

# integrate each function to find actual area
actual_area1, _ = scipy.integrate.quad(y1, a, b)
actual_area2, _ = scipy.integrate.quad(y2, a, b)
actual_area3, _ = scipy.integrate.quad(y3, a, b)

print("The actual Area under y1 is:", actual_area1)
print("The actual Area under y2 is:", actual_area2)
print("The actual Area under y3 is:", actual_area3)

#difference between area and actual area
difference1 = abs(actual_area1 - area1)
difference2 = abs(actual_area2 - area2)
difference3 = abs(actual_area3 - area3)

#print the differences out 
print("The difference between the inputed values and the actual value for y1 is:", difference1)
print("The difference between the inputed values and the actual value for y2 is:", difference2)
print("The difference between the inputed values and the actual value for y3 is:", difference3)

#calculate & plot the percent difference 
percent_difference_1 = ((difference1) / ((actual_area1 + area1)/2) * 100)
percent_difference_2 = ((difference2) / ((actual_area2 + area2)/2) * 100)
percent_difference_3 = ((difference3) / ((actual_area3 + area3)/2) * 100)

data = {'eqn 1':percent_difference_1, 'eqn 2':percent_difference_2, 'eqn 3':percent_difference_3}
equations = list(data.keys())
percent_difference = list(data.values())
                        
plt.bar(equations, percent_difference, color = 'green', width = 0.4)
plt.xlabel('equation number')
plt.ylabel('percent difference')
plt.show()
