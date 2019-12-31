"""
Breadth First Search (parcours en largeur)
"""


def breadth_first_search(graph, source_node):
    graph_queue = [(source_node, [source_node])]  # ajoute le noeud source dans la queue
    visited_vertices = [source_node]  # ajoute le noeud comme visité

    while graph_queue:  # si il reste quelque chose dans la queue
        (currentNode, path) = graph_queue[0]  # alloue à currentNode et path le valeurs de la queue
        graph_queue = graph_queue[1:]  # enlève l'entrée de la queue
        print(currentNode, "path = ", repr(path))  # écrit les valeurs

        for neighbor in graph[currentNode]:  # parcours les voisins du currentNode
            if neighbor not in visited_vertices:  # vérifie que le voisin n'a pas déjà été parcouru
                graph_queue.append(
                    (neighbor, path + [neighbor]))  # ajoute le voisin avec son chemin (parcouru + lui-même)
                visited_vertices.append(neighbor)  # ajoute le voisin comme visité


def breadth_first_search_routing(graph, source_node):
    graph_queue = [(source_node, [source_node])]  # ajoute le noeud source dans la queue
    visited_vertices = [source_node]  # ajoute le noeud comme visité
    routes = [None for i in range(len(graph))]  # crée une table de routage de la taille du graph (NEW)

    while graph_queue:  # si il reste quelque chose dans la queue
        (current_node, path) = graph_queue.pop(0)  # alloue à current_node et path le valeurs de la queue
        print(current_node, "path = ", repr(path))  # écrit les valeurs

        for neighbor in graph[current_node]:  # parcours les voisins du current_node
            if neighbor not in visited_vertices:  # vérifie que le voisin n'a pas déjà été parcouru
                graph_queue.append(
                    (neighbor, path + [neighbor]))  # ajoute le voisin avec son chemin (parcouru + lui-même)
                visited_vertices.append(neighbor)  # ajoute le voisin comme visité
                routes[neighbor] = current_node  # ajoute le noeud courant comme chemin pour aller au voisin

    print("routes :", repr(routes))  # affiche les routes


def breadth_first_search_routing_maze(graph, source_node):
    graph_queue = [(source_node, [source_node])]  # ajoute le noeud source dans la queue
    visited_vertices = [source_node]  # ajoute le noeud comme visité
    routes = {}  # crée un dictionnaire

    while graph_queue:  # si il reste quelque chose dans la queue
        (current_node, path) = graph_queue.pop(0)  # alloue à current_node et path le valeurs de la queue
        # print(current_node, "path = ", repr(path))  # écrit les valeurs

        for neighbor in graph.get(current_node):  # parcours les voisins du current_node
            if neighbor not in visited_vertices:  # vérifie que le voisin n'a pas déjà été parcouru
                graph_queue.append(
                    (neighbor, path + [neighbor]))  # ajoute le voisin avec son chemin (parcouru + lui-même)
                visited_vertices.append(neighbor)  # ajoute le voisin comme visité
                routes[neighbor] = current_node  # ajoute le noeud courant comme chemin pour aller au voisin

    print("routes :", repr(routes))  # affiche les routes
    return routes


'''
Test breadth_first_search
'''
# graph = [[1, 2, 5], [0, 2, 5], [0, 1], [4, 5], [3, 5], [0, 1, 3, 4]]
# breadth_first_search(graph, 0)

'''
Test breadth_first_search_routing
'''
# graph = [[1, 2, 5], [0, 2, 5], [0, 1], [4, 5], [3, 5], [0, 1, 3, 4]]
# breadth_first_search_routing(graph, 0)

# routes :  [None, 0, 0, 5, 5, 0] : pour aller à 4 il faut passer par 5 pour aller à 5 il faut passer par 0 donc 0, 5, 4

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
# breadth_first_search_routing_maze(maze, location)

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
