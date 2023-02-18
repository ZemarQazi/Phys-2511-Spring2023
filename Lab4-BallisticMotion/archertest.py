#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:18:32 2023

@author: nav
"""

import math

# constants that will be used throughout the rest of the program
gr = 9.81    # Acceleration due to gravity (m/s^2)
d = 1.2   # Density of air (kg/m^3)
C = 0.47    # Drag coefficient 
m = 0.1     # Mass of the arrow (kg)
deltat = 0.01  # Time step (s)

# where the target is positioned
target_x = 100.0
target_y = 0.0
target_radius = 0.5

while True:
    print("Take your first shot!")
    # inputs for the archer, what angle and speed will he shoot at to try to hit said target 
    angle = float(input("Enter the launch angle (degrees): "))
    speed = float(input("Enter the launch speed (m/s): "))

    # convert the angle to radians, allows for easier use later
    theta = math.radians(angle)

    # the initial conditions of the arrow
    x = 0.0     # Horizontal position (m)
    y = 0.0     # Vertical position (m)
    speed_x = speed * math.cos(theta)   # Horizontal velocity (m/s)
    speed_y = speed * math.sin(theta)   # Vertical velocity (m/s)

    # keep track of misses, also allows us to check if we have hit the target yet in the main loop
    misses = 0

    # main loop
    while True:
        # update position and velocity after input
        x += speed_x * deltat
        y += speed_y * deltat
        speed_x -= (0.5 * d * C * math.pi * (0.005**2) * speed_x**2 / m) * deltat # hoping this is the right math, looked this up
        speed_y -= (gr + 0.5 * d * C * math.pi * (0.005**2) * speed_y**2 / m) * deltat

        # check if the arrow has hit the ground
        if y <= 0:
            # Check if the arrow has hit the target
            if math.sqrt((x - target_x)**2 + y**2) <= target_radius:
                print("Target hit!")
                break
            else:
                misses += 1
                if x < target_x:
                    print(f"Missed by {target_x - x:.2f} meters to the left")
                else:
                    print(f"Missed by {x - target_x:.2f} meters to the right")

                # reset the position and velocity for next try 
                x = 0.0
                y = 0.0
                speed_x = speed * math.cos(theta)
                speed_y = speed * math.sin(theta)

                # makes sure program doesn't run for forever, shortens time
                deltat /= 2

        # check if the arrow has gone too far
        if x > 200:
            print("Arrow went too far!")
            break

    #  check if the archer has hit the target
    if math.sqrt((x - target_x)**2 + y**2) <= target_radius:
        print("You hit the target!")
      
        #calculate the final position relative to the archer 
        final_x = target_x - x
        final_y = target_y - y
        print(f"The final position is ({final_x:.2f}, {final_y:.2f}) meters relative to the archer")
        break 
    
    else:
        print("you missed the target!")
        print(f"You missed by {math.sqrt((x - target_x)**2 + y**2):.2f} meters")

#used the inputs of 10 degrees and 54 m/s to test the code as the target first misses the target but then finds balance and hits the target. Changing the angle angle up and down one also shows that both the "missed to the right" and "missed to left" functions work. 