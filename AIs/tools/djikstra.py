# Djikstra algorithm
import heapq
from typing import Tuple, List, Dict, Union, ItemsView

Node = Tuple[int, int]
Range = Tuple[int, int]


def insert_or_replace(min_heapq: heapq, node: Node, distance: int) -> None:
    """ Function that insert or replaces an element to the heapq """
    if node not in [x[1] for x in min_heapq]:  # insert if not existing
        heapq.heappush(min_heapq, (distance, node))

    else:  # replace if existing
        index_to_update = [x[1] for x in min_heapq].index(node)
        min_heapq[index_to_update] = (distance, node)
        heapq.heapify(min_heapq)


def get_min_max_values(maze_width: int, maze_height: int, location: Node, max_depth: int) -> Tuple[Range, Range]:
    """ Function that returns min/max values for x and y from a point and within a max_depth of nodes """

    def min_max(location_point: int, max_depth: int, max_axis_value: int) -> Range:
        """ Function that returns min/max values for an axis within a max_depth """
        low: int = (location_point - max_depth)
        high: int = (location_point + max_depth)

        # corrects the values if out of the maze
        if low < 0:  # below 0
            low = 0
        if high > max_axis_value:  # above maze_height/width
            high = max_axis_value

        return low, high

    (min_x, max_x) = min_max(location[0], max_depth, maze_width)
    (min_y, max_y) = min_max(location[1], max_depth, maze_height)

    return (min_x, max_x), (min_y, max_y)


def dijkstra(graph: List[List[Node]], source_node: int) -> List[int]:
    """ Djikstra algorithm that returns distances between nodes in graph """
    distances: List[Union[int, float]] = [float("inf") for i in
                                          range(len(graph))]  # init distances for each node to inf
    min_heap: heapq = [(0, source_node)]  # init priority queue with neighbours of current node
    distances[source_node] = 0  # init distance from current node to current node which is obviously 0

    while len(min_heap) != 0:  # while there is a neighbour to process

        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # takes closest node from heap queue

        for (neighbor, weight) in graph[closest_node]:  # for each neighbour
            neighbor_distance = closest_node_distance + weight  # distance = distance of current node + to neighbor
            if neighbor_distance < distances[neighbor]:  # if distance is closest than known (of inf)
                insert_or_replace(min_heap, neighbor, neighbor_distance)  # insert in heap queue
                distances[neighbor] = neighbor_distance  # update distance in distances list

    return distances  # return distances list


def dijkstra_route(graph: List[List[Node]], source_node: int) -> Tuple[List[int], List[int]]:
    """ Djikstra algorithm that returns distances between nodes in graph and a routing table """
    distances: List[Union[int, float]] = [float("inf") for i in range(len(graph))]  # init distance for each node to inf
    min_heap: heapq = [(0, source_node)]  # init priority queue with neighbours of current node
    distances[source_node]: List[int] = 0  # init distance from current node to current node which is obviously 0

    predecessors: List[Union[int, None]] = [None for i in range(len(graph))]  # routing table with shortest path to node

    while len(min_heap) != 0:  # while there is a neighbour to process

        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # takes closest node from heap queue

        for (neighbor, weight) in graph[closest_node]:  # for each neighbour
            neighbor_distance = closest_node_distance + weight  # distance = distance of current node + to neighbor
            if neighbor_distance < distances[neighbor]:  # if distance is closest than known (of inf)
                insert_or_replace(min_heap, neighbor, neighbor_distance)  # insert in heap queue
                distances[neighbor] = neighbor_distance  # update distance in distances list
                predecessors[neighbor] = closest_node  # update routing table with closest node of neighbour

    return distances, predecessors  # return distances list, routes list tuple


def dijkstra_route_maze(graph: Dict[Node, Dict[Node, int]], source_node: Node) \
        -> Tuple[Dict[Node, int], Dict[Node, Node]]:
    """ Djikstra algorithm that returns distances between nodes in maze and a routing table """
    # initialisation
    distances: Dict[Node, Union[int, float]] = dict.fromkeys(graph, float("inf"))  # init distances for each node to inf
    min_heap: heapq = [(0, source_node)]  # init priority queue with neighbours of current node
    distances[source_node] = 0  # init distance from current node to current node which is obviously 0

    predecessors: Dict[Node, Union[Node, None]] = dict.fromkeys(graph, None)  # routing table with shortest path to node

    while len(min_heap) != 0:  # while there is a neighbour to process

        closest_node_distance: int
        closest_node: Node
        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # takes closest node from heap queue

        neighbors: ItemsView[Node] = graph.get(closest_node).items()  #

        for neighbor, weight in neighbors:  # for each neighbour
            neighbor_distance = closest_node_distance + weight  # distance = distance of current node + to neighbor
            if neighbor_distance < distances[neighbor]:  # if distance is closest than known (of inf)
                insert_or_replace(min_heap, neighbor, neighbor_distance)  # insert in heap queue
                distances.update({neighbor: neighbor_distance})  # update distance in distances list
                predecessors[neighbor] = closest_node  # update routing table with closest node of neighbour

    return distances, predecessors  # return (distances dict, routes dict) tuple


def dijkstra_route_maze_range(graph: Dict[Node, Dict[Node, int]], maze_width: int, maze_height: int, source_node: Node,
                              max_depth: int) -> Tuple[Dict[Node, int], Dict[Node, Node]]:
    """ Djikstra algorithm that returns distances between nodes in maze and a routing table within a max_depth """
    distances: Dict[Node, Union[int, float]] = dict.fromkeys(graph, float("inf"))  # init distances for each node to inf
    min_heap: heapq = [(0, source_node)]  # init priority queue with neighbours of current node
    distances[source_node] = 0  # init distance from current node to current node which is obviously 0

    range_x: Range  # min/max values for x
    range_y: Range  # min/max values for y
    (range_x, range_y) = get_min_max_values(maze_width, maze_height, source_node, max_depth)

    predecessors: Dict[Node, Union[Node, None]] = dict.fromkeys(graph, None)  # routing table with shortest path to node

    while len(min_heap) != 0:  # while there is a neighbour to process

        closest_node_distance: int
        closest_node: Node
        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # takes closest node from heap queue

        # print("closest node:", closest_node, "items:", repr(graph.get(closest_node)))
        neighbors: ItemsView[Node] = graph.get(closest_node).items()  #

        neighbor: Node
        weight: int
        for neighbor, weight in neighbors:  # for each neighbour
            # if the neihbour is not within the range, do not explore it
            if not (range_x[0] <= neighbor[0] <= range_x[1] and range_y[0] <= neighbor[1] <= range_y[1]):
                pass
            else:
                neighbor_distance: int = closest_node_distance + weight  # distance = distance of current node + to neighbor
                if neighbor_distance < distances[neighbor]:  # if distance is closest than known (of inf)
                    insert_or_replace(min_heap, neighbor, neighbor_distance)  # insert in heap queue
                    distances.update({neighbor: neighbor_distance})  # update distance in distances list
                    predecessors[neighbor] = closest_node  # update routing table with closest node of neighbour

    return distances, predecessors  # return (distances dict, routes dict) tuple


'''
Test dijkstra
'''
# graph = [[(1, 1), (2, 7), (5, 3)], [(0, 1), (2, 1), (5, 1)], [(0, 7), (1, 1)], [(4, 2), (5, 2)], [(3, 2), (5, 5)],
#          [(0, 3), (1, 1), (3, 2), (4, 5)]]
# print(repr(dijkstra(graph, 0)))  # [0, 1, 2, 4, 6, 2]

'''
Test dijkstra_route
'''
# graph = [[(1, 1), (2, 7), (5, 3)], [(0, 1), (2, 1), (5, 1)], [(0, 7), (1, 1)], [(4, 2), (5, 2)], [(3, 2), (5, 5)],
#          [(0, 3), (1, 1), (3, 2), (4, 5)]]
# result_route = dijkstra_route(graph, 0)
#
# print(repr(result_route))  # ([0, 1, 2, 4, 6, 2], [None, 0, 1, 5, 3, 1])

'''
Maze for test dijkstra_route_*
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

'''
Test dijkstra_route_maze
'''
# location = (0, 0)
# result_route_maze = dijkstra_route_maze(maze, location)
# print(repr(result_route_maze))
#
# ({(0, 0): 0, (0, 1): 3, (0, 2): 4, (0, 3): 11, (0, 4): 12, (0, 5): 13, (0, 6): 14,
#   (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 10, (1, 4): 17, (1, 5): 16, (1, 6): 15,
#   (2, 0): 2, (2, 1): 3, (2, 2): 4, (2, 3): 5, (2, 4): 17, (2, 5): 17, (2, 6): 20,
#   (3, 0): 3, (3, 1): 4, (3, 2): 13, (3, 3): 14, (3, 4): 15, (3, 5): 18, (3, 6): 19,
#   (4, 0): 4, (4, 1): 5, (4, 2): 11, (4, 3): 21, (4, 4): 20, (4, 5): 21, (4, 6): 20,
#   (5, 0): 7, (5, 1): 6, (5, 2): 7, (5, 3): 12, (5, 4): 19, (5, 5): 20, (5, 6): 21,
#   (6, 0): 8, (6, 1): 9, (6, 2): 10, (6, 3): 11, (6, 4): 22, (6, 5): 21, (6, 6): 22},
#
# {(0, 0): None,
#  (0, 1): (1, 1),
#  (0, 2): (0, 1),
#  (0, 3): (1, 3),
#  (0, 4): (0, 3),
#  (0, 5): (0, 4),
#  (0, 6): (0, 5),
#  (1, 0): (0, 0), (1, 1): (1, 0), (1, 2): (1, 1), (1, 3): (1, 2), (1, 4): (1, 5), (1, 5): (1, 6), (1, 6): (0, 6),
#  (2, 0): (1, 0), (2, 1): (2, 0), (2, 2): (1, 2), (2, 3): (2, 2), (2, 4): (3, 4), (2, 5): (1, 5), (2, 6): (3, 6),
#  (3, 0): (2, 0), (3, 1): (3, 0), (3, 2): (4, 2), (3, 3): (3, 2), (3, 4): (3, 3), (3, 5): (2, 5), (3, 6): (3, 5),
#  (4, 0): (3, 0), (4, 1): (3, 1), (4, 2): (4, 1), (4, 3): (4, 4), (4, 4): (5, 4), (4, 5): (4, 6), (4, 6): (3, 6),
#  (5, 0): (5, 1), (5, 1): (4, 1), (5, 2): (5, 1), (5, 3): (6, 3), (5, 4): (5, 3), (5, 5): (5, 4), (5, 6): (4, 6),
#  (6, 0): (5, 0), (6, 1): (6, 0), (6, 2): (6, 1), (6, 3): (6, 2), (6, 4): (6, 5), (6, 5): (5, 5), (6, 6): (5, 6)})

'''
Test dijkstra_route_maze_range
'''
# location = (0, 0)
# result_route_maze_range = dijkstra_route_maze_range(maze, 25, 15, location, 4)
# print(repr(result_route_maze_range))
#
# ({(0, 0): 0, (0, 1): 3, (0, 2): 4, (0, 3): 11, (0, 4): 12, (0, 5): inf, (0, 6): inf, (1, 0): 1, (1, 1): 2, (1, 2): 3,
#   (1, 3): 10, (1, 4): inf, (1, 5): inf, (1, 6): inf, (2, 0): 2, (2, 1): 3, (2, 2): 4, (2, 3): 5, (2, 4): 17,
#   (2, 5): inf, (2, 6): inf, (3, 0): 3, (3, 1): 4, (3, 2): 13, (3, 3): 14, (3, 4): 15, (3, 5): inf, (3, 6): inf,
#   (4, 0): 4, (4, 1): 5, (4, 2): 11, (4, 3): inf, (4, 4): inf, (4, 5): inf, (4, 6): inf, (5, 0): inf, (5, 1): inf,
#   (5, 2): inf, (5, 3): inf, (5, 4): inf, (5, 5): inf, (5, 6): inf, (6, 0): inf, (6, 1): inf, (6, 2): inf, (6, 3): inf,
#   (6, 4): inf, (6, 5): inf, (6, 6): inf},
#
#  {(0, 0): None, (0, 1): (1, 1), (0, 2): (0, 1), (0, 3): (1, 3), (0, 4): (0, 3), (0, 5): None, (0, 6): None,
#   (1, 0): (0, 0), (1, 1): (1, 0), (1, 2): (1, 1), (1, 3): (1, 2), (1, 4): None, (1, 5): None, (1, 6): None,
#   (2, 0): (1, 0), (2, 1): (2, 0), (2, 2): (1, 2), (2, 3): (2, 2), (2, 4): (3, 4), (2, 5): None, (2, 6): None,
#   (3, 0): (2, 0), (3, 1): (3, 0), (3, 2): (4, 2), (3, 3): (3, 2), (3, 4): (3, 3), (3, 5): None, (3, 6): None,
#   (4, 0): (3, 0), (4, 1): (3, 1), (4, 2): (4, 1), (4, 3): None, (4, 4): None, (4, 5): None, (4, 6): None, (5, 0): None,
#   (5, 1): None, (5, 2): None, (5, 3): None, (5, 4): None, (5, 5): None, (5, 6): None, (6, 0): None, (6, 1): None,
#   (6, 2): None, (6, 3): None, (6, 4): None, (6, 5): None, (6, 6): None})
