import heapq


# Utility function that inserts an element to the min-heap, or replaces it otherwise
def insert_or_replace(min_heap, element, weight):
    # Insert if does not exist
    if element not in [x[1] for x in min_heap]:
        heapq.heappush(min_heap, (weight, element))

    # Replace otherwise
    else:
        index_to_update = [x[1] for x in min_heap].index(element)
        min_heap[index_to_update] = (weight, element)
        heapq.heapify(min_heap)


def dijkstra(graph, source_node):
    # Partie initialisation
    distances = [float("inf") for i in range(len(graph))]
    min_heap = [(0, source_node)]
    distances[source_node] = 0

    while len(min_heap) != 0:  # tant qu'il y qqch dans le tas (i.e. un voisin à traiter)

        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # prend le noeud le plus proche (priorité)

        for (neighbor, weight) in graph[closest_node]:  # pour chaque voisin
            neighbor_distance = closest_node_distance + weight  # distance = distance du noeud courant + du voisin
            if neighbor_distance < distances[neighbor]:  # si le chemin est plus court que celui connu (ou infini)
                insert_or_replace(min_heap, neighbor, neighbor_distance)  # mettre dans la file de priorité
                distances[neighbor] = neighbor_distance  # màj de la distance dans le tableau des distances

    return distances  # retourne le tableau des distances


def dijkstra_route(graph, source_node):
    # Partie initialisation
    distances = [float("inf") for i in range(len(graph))]  # tableau pour les distances de chaque noeud à l'infini
    min_heap = [(0, source_node)]  # sert à connaître les voisins à traiter et la distance min pour y arriver1110111111
    distances[source_node] = 0

    predecessors = [None for i in range(len(graph))]  # tableau de routage pour le plus court chemin vers le noeud

    while len(min_heap) != 0:  # tant qu'il y qqch dans le tas (i.e. un voisin à traiter)

        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # prend le noeud le plus proche (priorité)

        for (neighbor, weight) in graph[closest_node]:  # pour chaque voisin
            neighbor_distance = closest_node_distance + weight  # distance = distance du noeud courant + du voisin
            if neighbor_distance < distances[neighbor]:  # si le chemin est plus court que celui connu (ou infini)
                insert_or_replace(min_heap, neighbor, neighbor_distance)  # mettre dans la file de priorité
                distances[neighbor] = neighbor_distance  # màj de la distance dans le tableau des distances
                predecessors[neighbor] = closest_node  # màj du chemin dans la table de routage

    return distances, predecessors  # retourne un couple (tableau distances, tableau routes)


def dijkstra_route_maze(graph, source_node):
    # Partie initialisation
    distances = dict.fromkeys(graph, float("inf"))  # tableau pour les distances de chaque noeud à l'infini
    min_heap = [(0, source_node)]  # sert à connaître les voisins à traiter et la distance min pour y arriver1110111111
    distances[source_node] = 0

    predecessors = dict.fromkeys(graph, None)  # tableau de routage pour le plus court chemin vers le noeud

    while len(min_heap) != 0:  # tant qu'il y qqch dans le tas (i.e. un voisin à traiter)

        (closest_node_distance, closest_node) = heapq.heappop(min_heap)  # prend le noeud le plus proche (priorité)

        neighbors = graph.get(closest_node).items()  #

        for neighbor, weight in neighbors:  # pour chaque voisin
            neighbor_distance = closest_node_distance + weight  # distance = distance du noeud courant + du voisin
            if neighbor_distance < distances[neighbor]:  # si le chemin est plus court que celui connu (ou infini)
                insert_or_replace(min_heap, neighbor, neighbor_distance)  # mettre dans la file de priorité
                distances.update({neighbor: neighbor_distance})  # màj de la distance dans le tableau des distances
                predecessors[neighbor] = closest_node  # màj du chemin dans la table de routage

    return distances, predecessors  # retourne un couple (tableau distances, tableau routes)


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
Test dijkstra_route_maze
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
# result_route_maze = dijkstra_route_maze(maze, location)
#
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
