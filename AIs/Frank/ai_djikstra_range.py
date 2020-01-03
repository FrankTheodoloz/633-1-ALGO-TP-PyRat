# Template file to create an AI for the game PyRat
# http://formations.telecom-bretagne.eu/pyrat

###############################
# When the player is performing a move, it actually sends a character to the main program
# The four possibilities are defined here
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

TEAM_NAME = '[DJIKSTRA_RANGE] R@t_of_Fortune_888'

###############################
# Please put your imports here
import numpy
from AIs.tools.djikstra import *

###############################
# Please put your global variables here


PATHS_TO_POC: list = []
MOVES_TO_TARGET: list = []
MAX_DEPTH: int = 6
REMAINING_POC: set


# recursive function that build routes of closest piece of cheese
def get_closest_poc(maze_map: dict, maze_width: int, maze_height: int, source_location: tuple) -> None:
    global PATHS_TO_POC
    global MAX_DEPTH

    while len(REMAINING_POC):  # while there are remaining POC to calculate paths
        # get distances and routes around location
        distances: dict
        toutes: dict
        (distances, routes) = dijkstra_route_maze_range(maze_map, maze_width, maze_height, source_location, MAX_DEPTH)

        # get min distances to poc
        poc_distances: dict = {k: v for k, v in distances.items() if 0 < v < float("inf") and k in REMAINING_POC}

        closest_poc: tuple = (float("inf"), float("inf"))  # source_location

        # select closest poc
        if poc_distances.keys():
            closest_poc = min(poc_distances, key=poc_distances.get)
        else:
            MAX_DEPTH += 4
            print("increasing depth")
            get_closest_poc(maze_map, maze_width, maze_height, closest_poc)

        # add the route to the next closest poc in the closest_poc
        PATHS_TO_POC.append(get_path(source_location, closest_poc, routes))

        # remove the poc from REMAINING_POC
        REMAINING_POC.remove(closest_poc)

        get_closest_poc(maze_map, maze_width, maze_height, closest_poc)


#  Gets the path to the target by querying the route recursively
def get_path(source_location: tuple, target_location: tuple, routes: dict) -> list:
    """ Function that returns a path to a point from the routing table """
    path: list = []

    def recursive_path_find(location):
        """ Recursive function that gets the path from target to initial location """
        path.append(location)

        if routes.get(location) != source_location:  # until the initial location is met
            recursive_path_find(routes.get(location))  # invoke recursion

    recursive_path_find(target_location)  # starts recursion

    return path


def move_from_location(source_location, target_location):
    """ Function that return the move to do from a source to a target """
    # print("going from:", source_location, "to:", target_location)
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
    global REMAINING_POC
    global PATHS_TO_POC
    REMAINING_POC = set(piecesOfCheese)

    get_closest_poc(mazeMap, mazeWidth, mazeHeight, playerLocation)


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
    global MOVES_TO_TARGET
    global PATHS_TO_POC
    global REMAINING_POC

    if MOVES_TO_TARGET:  # if there are remaining moves

        # if the target poc has been eaten before
        if MOVES_TO_TARGET[0] not in piecesOfCheese:
            # recalculate paths from playerLocation
            MOVES_TO_TARGET, PATHS_TO_POC = [], []
            REMAINING_POC = piecesOfCheese
            get_closest_poc(mazeMap, mazeWidth, mazeHeight, playerLocation)
            MOVES_TO_TARGET = PATHS_TO_POC.pop(0)

    elif PATHS_TO_POC:  # if there are remaining paths
        MOVES_TO_TARGET = PATHS_TO_POC.pop(0)  # process next path

    else:  # there is no moves nor targets
        get_closest_poc(mazeMap, mazeWidth, mazeHeight, playerLocation)

    return move_from_location(playerLocation, MOVES_TO_TARGET.pop())
