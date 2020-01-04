###############################
# When the player is performing a move, it actually sends a character to the main program
# The four possibilities are defined here
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

TEAM_NAME = 'Depth first search'

###############################
# Please put your imports here
import numpy
from AIs.tools.depth_first_search import depth_first_search_routing_maze as depth_first_search
from typing import Tuple, List, Dict

###############################
# Please put your global variables here
Node = Tuple[int, int]
ROUTES: Dict[Node, List[Node]]  # paths to any node
MOVES_TO_TARGET: List[Node] = []  # queue of moves


def get_routes(maze_map: Dict[Node, Dict[Node, int]], source_location: Node) -> Dict[Node, List[Node]]:
    """ Function that returns a dict of routes using dfs """
    return depth_first_search(maze_map, source_location)


def get_path(target_location: Node) -> List[Node]:
    """ Function that returns a path to a node from the ROUTES """
    return ROUTES[target_location]


def move_from_location(source_location: Node, target_location: Node) -> str:
    """ Function that return the move to do from a source to a target """
    # print("going from:", source_location, "to:", target_location)
    difference: Tuple[int, int] = tuple(numpy.subtract(target_location, source_location))
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
    global ROUTES
    global MOVES_TO_TARGET

    ROUTES = get_routes(mazeMap, playerLocation)
    MOVES_TO_TARGET = get_path(piecesOfCheese[0])[1:]
    print("path to do:", repr(MOVES_TO_TARGET))


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
        return move_from_location(playerLocation, MOVES_TO_TARGET.pop(0))  # queue
