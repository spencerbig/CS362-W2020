# -*- coding: utf-8 -*-
"""
Created on Sat Jan 2020

@Author: Spencer Schibig
"""

import testUtility
import Dominion
import random
from collections import defaultdict

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# create number of victory and curse cards
victoryCardAmount = testUtility.init_VictoryCards(player_names)
curseCardAmount = testUtility.init_CurseCards(player_names)

# define box
box = testUtility.getBoxes(victoryCardAmount)

# game supply order
supply_order = testUtility.init_SupplyOrder()

# Pick 10 cards from box to be in the supply.
# The supply always has these cards
supply = testUtility.init_DefaultSupply(box, player_names)

# initialize the trash
trash = testUtility.init_Trash()

# Construct the Player objects
players = testUtility.init_Players(player_names)

# --------------start game------------------------#
# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1

# ---------------------------BUG: COPY AND PASTE ERROR SCENARIO- 'turn+=1' is instigated twice--------------------------
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dominion_CardSummary = Dominion.cardsummaries(players)
victoryPoints = dominion_CardSummary.loc['VICTORY POINTS']
max_VictoryPoints = victoryPoints.max()
winners = []

for i in victoryPoints.index:
    if victoryPoints.loc[i] == max_VictoryPoints:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dominion_CardSummary)
