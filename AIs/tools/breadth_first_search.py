# Breadth First Search (parcours en largeur)
from typing import Tuple, List, Dict, Union

Node = Tuple[int, int]


def breadth_first_search(graph: List[List[int]], source_node: int) -> None:
    """ Function BFS that prints how the algorithm is visiting nodes """
    graph_queue: List[Tuple[int, List[int]]] = [(source_node, [source_node])]  # add source_node to queue
    visited_vertices: List[int] = [source_node]  # add source_node as visited

    while graph_queue:  # while there is a neighbour to visit in the queue
        (current_node, path) = graph_queue[0]  # get the current_node and his path
        graph_queue = graph_queue[1:]  # remove the current_node from the queue
        print(current_node, "path = ", repr(path))

        for neighbour in graph[current_node]:  # for each neighbour
            if neighbour not in visited_vertices:  # not visited
                graph_queue.append((neighbour, path + [neighbour]))  # add neighbour with his path to the queue
                visited_vertices.append(neighbour)  # add the neighbour as visited


def breadth_first_search_routing(graph: List[List], source_node: int) -> List[int]:
    """ Function BFS that return a list of routes from source_node to all other nodes """
    graph_queue: List[Tuple[int, List[int]]] = [(source_node, [source_node])]  # add source_node to queue
    visited_vertices: List[int] = [source_node]  # add source_node as visited
    routes: List[Union[int, None]] = [None for i in range(len(graph))]  # init routing table of the graph size

    while graph_queue:  # while there is a neighbour to visit in the queue
        (current_node, path) = graph_queue.pop(0)  # get the current_node and his path
        # print(current_node, "path = ", repr(path))

        for neighbour in graph[current_node]:  # for each neighbour
            if neighbour not in visited_vertices:  # not visited
                graph_queue.append((neighbour, path + [neighbour]))  # add neighbour with his path to the queue
                visited_vertices.append(neighbour)  # add the neighbour as visited
                routes[neighbour] = current_node  # adds current_node as path for the neighbour

    return routes


# For Pyrat maze
def breadth_first_search_routing_maze(graph: Dict[Node, Dict[Node, int]], source_node: Node) -> Dict[Node, Node]:
    """ Function BFS that return a list of routes from source_node to all other nodes """
    graph_queue: List[Tuple[Node, List[Node]]] = [(source_node, [source_node])]  # add source_node to queue
    visited_vertices: List[Node] = [source_node]  # add source_node as visited
    routes: Dict[Node, Node] = {}  # crée un dictionnaire

    while graph_queue:  # while there is a neighbour to visit in the queue
        current_node: Node
        path: List[Node]
        (current_node, path) = graph_queue.pop(0)  # get the current_node and his path
        # print(current_node, "path = ", repr(path))

        for neighbour in graph.get(current_node):
            if neighbour not in visited_vertices:  # for each neighbour not visited
                graph_queue.append(
                    (neighbour, path + [neighbour]))  # ajoute le voisin avec son chemin (parcouru + lui-même)
                visited_vertices.append(neighbour)  # add the current_node as visited
                routes[neighbour] = current_node  # ajoute le noeud courant comme chemin pour aller au voisin

    return routes


'''
Test breadth_first_search
'''
# graph = [[1, 2, 5], [0, 2, 5], [0, 1], [4, 5], [3, 5], [0, 1, 3, 4]]
# print(repr(breadth_first_search(graph, 0)))
# 0 path =  [0]
# 1 path =  [0, 1]
# 2 path =  [0, 2]
# 5 path =  [0, 5]
# 3 path =  [0, 5, 3]
# 4 path =  [0, 5, 4]
# None

'''
Test breadth_first_search_routing
'''
# graph = [[1, 2, 5], [0, 2, 5], [0, 1], [4, 5], [3, 5], [0, 1, 3, 4]]
# print("Routes:", repr(breadth_first_search_routing(graph, 0)))
#
# Routes:  [None, 0, 0, 5, 5, 0] : pour aller à 4 il faut passer par 5 pour aller à 5 il faut passer par 0 donc 0, 5, 4

'''
Test breadth_first_search_routing_maze
'''
# maze = {(0, 0): {(1, 0): 1}, (0, 1): {(0, 2): 1, (1, 1): 1}, (0, 2): {(0, 1): 1}, (0, 3): {(1, 3): 1, (0, 4): 1},
#         (0, 4): {(0, 3): 1, (0, 5): 1}, (0, 5): {(0, 4): 1, (0, 6): 1}, (0, 6): {(1, 6): 1, (0, 5): 1},
#         (1, 0): {(2, 0): 1, (1, 1): 1, (0, 0): 1}, (1, 1): {(1, 0): 1, (0, 1): 1, (1, 2): 1},
#         (1, 2): {(2, 2): 1, (1, 3): 7, (1, 1): 1}, (1, 3): {(0, 3): 1, (1, 2): 7}, (1, 4): {(1, 5): 1},
#         (1, 5): {(1, 6): 1, (2, 5): 1, (1, 4): 1}, (1, 6): {(1, 5): 1, (0, 6): 1},
#         (2, 0): {(1, 0): 1, (3, 0): 1, (2, 1): 1}, (2, 1): {(2, 0): 1}, (2, 2): {(1, 2): 1, (2, 3): 1},
#         (2, 3): {(2, 2): 1}, (2, 4): {(3, 4): 2, (2, 5): 6}, (2, 5): {(3, 5): 1, (1, 5): 1, (2, 4): 6},
#         (2, 6): {(3, 6): 1}, (3, 0): {(2, 0): 1, (4, 0): 1, (3, 1): 1}, (3, 1): {(4, 1): 1, (3, 0): 1},
#         (3, 2): {(4, 2): 2, (3, 3): 1}, (3, 3): {(3, 4): 1, (3, 2): 1}, (3, 4): {(2, 4): 2, (3, 3): 1},
#         (3, 5): {(2, 5): 1, (3, 6): 1}, (3, 6): {(4, 6): 1, (2, 6): 1, (3, 5): 1}, (4, 0): {(3, 0): 1},
#         (4, 1): {(3, 1): 1, (5, 1): 1, (4, 2): 6}, (4, 2): {(3, 2): 2, (4, 1): 6}, (4, 3): {(4, 4): 1},
#         (4, 4): {(5, 4): 1, (4, 3): 1}, (4, 5): {(4, 6): 1}, (4, 6): {(5, 6): 1, (3, 6): 1, (4, 5): 1},
#         (5, 0): {(5, 1): 1, (6, 0): 1}, (5, 1): {(5, 0): 1, (4, 1): 1, (5, 2): 1}, (5, 2): {(5, 1): 1},
#         (5, 3): {(6, 3): 1, (5, 4): 7}, (5, 4): {(4, 4): 1, (5, 3): 7, (5, 5): 1},
#         (5, 5): {(5, 6): 1, (6, 5): 1, (5, 4): 1}, (5, 6): {(4, 6): 1, (5, 5): 1, (6, 6): 1},
#         (6, 0): {(5, 0): 1, (6, 1): 1}, (6, 1): {(6, 2): 1, (6, 0): 1}, (6, 2): {(6, 3): 1, (6, 1): 1},
#         (6, 3): {(5, 3): 1, (6, 2): 1}, (6, 4): {(6, 5): 1}, (6, 5): {(6, 4): 1, (5, 5): 1}, (6, 6): {(5, 6): 1}}
# location = (0, 0)
# print("Routes:", repr(breadth_first_search_routing_maze(maze, location)))
#
# routes : {(1, 0): (0, 0),  # 1
#           (2, 0): (1, 0),  # 2
#           (1, 1): (1, 0),
#           (3, 0): (2, 0),  # 3
#           (2, 1): (2, 0),
#           (0, 1): (1, 1),
#           (1, 2): (1, 1),
#           (4, 0): (3, 0),
#           (3, 1): (3, 0),  # 4
#           (0, 2): (0, 1),
#           (2, 2): (1, 2),
#           (1, 3): (1, 2),
#           (4, 1): (3, 1),  # 5
#           (2, 3): (2, 2),
#           (0, 3): (1, 3),
#           (5, 1): (4, 1),
#           (4, 2): (4, 1),  # 6
#           (0, 4): (0, 3),
#           (5, 0): (5, 1),
#           (5, 2): (5, 1),
#           (3, 2): (4, 2),  # 7
#           (0, 5): (0, 4),
#           (6, 0): (5, 0),
#           (3, 3): (3, 2),  # 8
#           (0, 6): (0, 5),
#           (6, 1): (6, 0),
#           (3, 4): (3, 3),
#           (1, 6): (0, 6),
#           (6, 2): (6, 1),
#           (2, 4): (3, 4),
#           (1, 5): (1, 6),
#           (6, 3): (6, 2),
#           (2, 5): (2, 4),
#           (1, 4): (1, 5),
#           (5, 3): (6, 3),
#           (3, 5): (2, 5),
#           (5, 4): (5, 3),
#           (3, 6): (3, 5),
#           (4, 4): (5, 4),
#           (5, 5): (5, 4),
#           (4, 6): (3, 6),
#           (2, 6): (3, 6),
#           (4, 3): (4, 4),
#           (5, 6): (5, 5),
#           (6, 5): (5, 5),
#           (4, 5): (4, 6),
#           (6, 6): (5, 6),
#           (6, 4): (6, 5)}
