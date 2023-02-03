#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 23:18:30 2023

@author: nav
"""

import random 
from sys import exit #didn't like how the exit function would work but still provide an error

#define board wiith 50 spaces 
board = [None] * 50

#define 25% of the spaces with special rules + has to be above the value of 6. The program selects a random number between 1 & 6 to subtract from the position when somoene lands on a special place, so no special spaces before 6 
for i in range (6, 50, 2):
    board[i] = "Special"

#Define the starting and ending points, making the end at 50 causes endless loop due to for loop above
start = 0
end = 49

#Define the players and thier positions 
players = [{"name": "Player 1", "position": start},
           {"name": "Player 2", "position": start}]

# Define a functiion to move the player 
def move_player(player): 
    dice = random.randint(1,6)
    print(f"{player['name']} rolled a " + str(dice))
    player["position"] = (player["position"] + dice) % 50
        
    
# Play the game 
while True: 
    for player in players: 
        move_player(player)
        if player["position"] == end:
            print(f"{player['name']} wins!")
            exit()
        print(f"{player['name']} is at {player['position']}")
        if board[player["position"]] == "Special":
            player["position"] = (player["position"] - random.randint(1,6)) % 50
            print(f"{player['name']} & is now at {player['position']} because he landed on a special space!")
    