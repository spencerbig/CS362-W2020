# -*- coding: utf-8 -*-
"""
Created on Sat Jan 2020

@Author: Spencer Schibig
"""

import Dominion
import random
from collections import defaultdict

# number of victory cards
def init_VictoryCards(playerNames):
    if len(playerNames) > 2:
        victoryCardAmount = 12
    else:
        victoryCardAmount = 8

    return victoryCardAmount


def init_CurseCards(playerNames):
    curseCardAmount = -10 + 10 * len(playerNames)

    # number of curses
    return curseCardAmount


def getBoxes(victoryCardAmount):
    # Define box
    box = {}

    box["Woodcutter"] = [Dominion.Woodcutter()] * 10
    box["Smithy"] = [Dominion.Smithy()] * 10
    box["Laboratory"] = [Dominion.Laboratory()] * 10
    box["Village"] = [Dominion.Village()] * 10
    box["Festival"] = [Dominion.Festival()] * 10
    box["Market"] = [Dominion.Market()] * 10
    box["Chancellor"] = [Dominion.Chancellor()] * 10
    box["Workshop"] = [Dominion.Workshop()] * 10
    box["Moneylender"] = [Dominion.Moneylender()] * 10
    box["Chapel"] = [Dominion.Chapel()] * 10
    box["Cellar"] = [Dominion.Cellar()] * 10
    box["Remodel"] = [Dominion.Remodel()] * 10
    box["Adventurer"] = [Dominion.Adventurer()] * 10
    box["Feast"] = [Dominion.Feast()] * 10
    box["Mine"] = [Dominion.Mine()] * 10
    box["Library"] = [Dominion.Library()] * 10
    box["Gardens"] = [Dominion.Gardens()] * victoryCardAmount
    box["Moat"] = [Dominion.Moat()] * 10
    box["Council Room"] = [Dominion.Council_Room()] * 10
    box["Witch"] = [Dominion.Witch()] * 10
    box["Bureaucrat"] = [Dominion.Bureaucrat()] * 10
    box["Militia"] = [Dominion.Militia()] * 10
    box["Spy"] = [Dominion.Spy()] * 10
    box["Thief"] = [Dominion.Thief()] * 10
    box["Throne Room"] = [Dominion.Throne_Room()] * 10

    return box


def init_SupplyOrder():

    supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
                    'Throne Room'],
                5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                6: ['Gold', 'Adventurer'], 8: ['Province']}

    return supply_order


def init_DefaultSupply(box, playerNames):

    # Pick 10 cards from box to be in the supply
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list, [(k, box[k]) for k in random10])

    # victory and curse card amounts for readability
    victoryCardAmount = init_VictoryCards(playerNames)
    curseCardAmount = init_CurseCards(playerNames)

    # The supply always has these cards
    supply["Copper"] = [Dominion.Copper()] * (60 - len(playerNames) * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * victoryCardAmount
    supply["Duchy"] = [Dominion.Duchy()] * victoryCardAmount
    supply["Province"] = [Dominion.Province()] * victoryCardAmount
    supply["Curse"] = [Dominion.Curse()] * curseCardAmount

    return supply


def init_Trash():
    # initialize the trash
    trash = []
    return trash


def init_Players(player_names):

    # Construct the Player objects
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))

    return players