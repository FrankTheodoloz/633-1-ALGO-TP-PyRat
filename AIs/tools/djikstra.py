import heapq


def insert_or_replace(min_heapq, node, distance) -> None:
    """ Function that insert or replaces an element to the heapq """
    if node not in [x[1] for x in min_heapq]:  # insert if not existing
        heapq.heappush(min_heapq, (distance, node))

    else:  # replace if existing
        index_to_update = [x[1] for x in min_heapq].index(node)
        min_heapq[index_to_update] = (distance, node)
        heapq.heapify(min_heapq)


def dijkstra(graph: dict, source_node: int) -> list:
    """ Djikstra algorithm that returns distances between nodes in graph """
    distances: list = [float("inf") for i in range(len(graph))]  # init distances list for each node to inf
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


def dijkstra_route(graph: dict, source_node: int) -> (dict, dict):
    """ Djikstra algorithm that returns distances between nodes in graph and a routing table """
    distances: list = [float("inf") for i in range(len(graph))]  # init distances list for each node to inf
    min_heap: heapq = [(0, source_node)]  # init priority queue with neighbours of current node
    distances[source_node] = 0  # init distance from current node to current node which is obviously 0

    predecessors: list = [None for i in range(len(graph))]  # routing table with shortest path to node

    while len(min_heap) != 0:  # while there is a neighbour to process

        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # takes closest node from heap queue

        for (neighbor, weight) in graph[closest_node]:  # for each neighbour
            neighbor_distance = closest_node_distance + weight  # distance = distance of current node + to neighbor
            if neighbor_distance < distances[neighbor]:  # if distance is closest than known (of inf)
                insert_or_replace(min_heap, neighbor, neighbor_distance)  # insert in heap queue
                distances[neighbor] = neighbor_distance  # update distance in distances list
                predecessors[neighbor] = closest_node  # update routing table with closest node of neighbour

    return distances, predecessors  # return (distances list, routes list) tuple


def dijkstra_route_maze(graph: dict, source_node: tuple) -> (dict, dict):
    """ Djikstra algorithm that returns distances between nodes in maze and a routing table """
    # initialisation
    distances: dict = dict.fromkeys(graph, float("inf"))  # init distances list for each node to inf
    min_heap: heapq = [(0, source_node)]  # init priority queue with neighbours of current node
    distances[source_node] = 0  # init distance from current node to current node which is obviously 0

    predecessors: dict = dict.fromkeys(graph, None)  # routing table with shortest path to node

    while len(min_heap) != 0:  # while there is a neighbour to process

        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # takes closest node from heap queue

        neighbors = graph.get(closest_node).items()  #

        for neighbor, weight in neighbors:  # for each neighbour
            neighbor_distance = closest_node_distance + weight  # distance = distance of current node + to neighbor
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
# result = dijkstra(graph, 0)
#
# print(repr(result)) # [0, 1, 2, 4, 6, 2]

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
