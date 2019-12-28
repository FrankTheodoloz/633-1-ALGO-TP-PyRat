# Template file to create an AI for the game PyRat
# http://formations.telecom-bretagne.eu/pyrat

###############################
# When the player is performing a move, it actually sends a character to the main program
# The four possibilities are defined here
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

TEAM_NAME = '[Sandbox] R@t_of_Fortune_888'

###############################
# Please put your imports here
import numpy

###############################
# Please put your global variables here
routes = {}
path = []


def above_of(maze_width, maze_height, source_location):
    if source_location[1] == maze_height:
        return None
    return source_location[0], source_location[1] + 1


def below_of(maze_width, maze_height, source_location):
    if source_location[1] == 0:
        return None
    return source_location[0], source_location[1] - 1


def left_of(maze_width, maze_height, source_location):
    if source_location[0] == 0:
        return None
    return source_location[0] - 1, source_location[1]


def right_of(maze_width, maze_height, source_location):
    if source_location[0] == maze_width:
        return None
    return source_location[0] + 1, source_location[1]


def can_move(maze_map, source_location, target_location):
    # return if target location is connected to source location
    return target_location in maze_map[source_location]


def move_from_location(source_location, target_location):
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
    global routes
    global path

    # tests can_move
    print("Cell above:", repr(above_of(mazeWidth, mazeHeight, playerLocation)), "can move there ?",
          can_move(mazeMap, playerLocation, above_of(mazeWidth, mazeHeight, playerLocation)))

    print("Cell below:", repr(below_of(mazeWidth, mazeHeight, playerLocation)), "can move there ?",
          can_move(mazeMap, playerLocation, below_of(mazeWidth, mazeHeight, playerLocation)))

    print("Cell on the left:", repr(left_of(mazeWidth, mazeHeight, playerLocation)), "can move there ?",
          can_move(mazeMap, playerLocation, left_of(mazeWidth, mazeHeight, playerLocation)))

    print("Cell on the right:", repr(right_of(mazeWidth, mazeHeight, playerLocation)), "can move there ?",
          can_move(mazeMap, playerLocation, right_of(mazeWidth, mazeHeight, playerLocation)))


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
    pass
