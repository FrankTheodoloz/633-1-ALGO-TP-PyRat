# Template file to create an AI for the game PyRat
# http://formations.telecom-bretagne.eu/pyrat

###############################
# When the player is performing a move, it actually sends a character to the main program
# The four possibilities are defined here
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

TEAM_NAME = 'improved_rand'

###############################
# Please put your imports here
import math
import random
import numpy

###############################
# Please put your global variables here
visitedCells = []


def randMove():
    moves = [MOVE_LEFT, MOVE_UP, MOVE_RIGHT, MOVE_DOWN]
    return moves[random.randint(0, 3)]


def discoverMove(playerLocation, mazeMap):
    moves = []
    for neighbor in mazeMap[playerLocation]:
        if neighbor not in visitedCells:
            move = moveFromLocation(playerLocation, neighbor)
            moves.append(move)
    return moves


def moveFromLocation(sourceLocation, targetLocation):
    difference = tuple(numpy.subtract(targetLocation, sourceLocation))
    if difference == (0, -1):
        return MOVE_DOWN
    elif difference == (0, 1):
        return MOVE_UP
    elif difference == (1, 0):
        return MOVE_RIGHT
    elif difference == (-1, 0):
        return MOVE_LEFT
    else:
        raise Exception("Impossible move")


###############################
# Preprocessing function
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
###############################
# Arguments are:
# mazeMap : dict(pair(int, int), dict(pair(int, int), int))
# mazeWidth : int
# mazeHeight : int
# playerLocation : pair(int, int)
# opponentLocation : pair(int,int)
# piecesOfCheese : list(pair(int, int))
# timeAllowed : float
###############################
# This function is not expected to return anything
def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed):
    pass


###############################
# Turn function
# The turn function is called each time the game is waiting
# for the player to make a decision (a move).
###############################
# Arguments are:
# mazeMap : dict(pair(int, int), dict(pair(int, int), int))
# mazeWidth : int
# mazeHeight : int
# playerLocation : pair(int, int)
# opponentLocation : pair(int, int)
# playerScore : float
# opponentScore : float
# piecesOfCheese : list(pair(int, int))
# timeAllowed : float
###############################
# This function is expected to return a move
def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese,
         timeAllowed):
    global visitedCells
    if playerLocation not in visitedCells:
        visitedCells.append(playerLocation)

    moves = discoverMove(playerLocation, mazeMap)
    if moves:
        return moves[random.randint(0, len(moves) - 1)]
    else:
        return randMove()
