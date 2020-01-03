###############################
# When the player is performing a move, it actually sends a character to the main program
# The four possibilities are defined here
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

TEAM_NAME = '[DFS] R@t_of_Fortune_888'

###############################
# Please put your imports here
import numpy
from AIs.tools.depth_first_search import *

###############################
# Please put your global variables here
PATHS_TO_POC = {}
MOVES_TO_TARGET = []


#  Gets the routes from the maze
def get_routes(maze_map, source_location):
    routes = depth_first_search_routing(maze_map, source_location)
    return routes


#  Gets the path to the target
def get_path(target_location):
    return PATHS_TO_POC[target_location]


def move_from_location(source_location, target_location):
    print("going from:", source_location, "to:", target_location)
    difference = tuple(numpy.subtract(target_location, source_location))
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
    global PATHS_TO_POC
    global MOVES_TO_TARGET

    ROUTES = get_routes(mazeMap, playerLocation)
    PATH_TO_TARGET = get_path(piecesOfCheese[0])
    print("path to do:", repr(PATH_TO_TARGET))


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
    while MOVES_TO_TARGET:
        return move_from_location(playerLocation,
                                  MOVES_TO_TARGET.pop(1))  # removes second item since player location is the first
