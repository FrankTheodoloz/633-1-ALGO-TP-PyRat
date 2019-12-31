"""
Depth First Search (parcours en profondeur)
"""


def depth_first_search(graph, source_node):
    visited = []  # stocke les noeuds visités

    def depth_first_search_recursive(graph, current_node):
        visited.append(current_node)  # on ajoute le noeud comme visité
        print(current_node)

        for neighbor in graph[current_node]:  # pour chaque noeud voisin
            if neighbor not in visited:  # s'il n'a pas déjà été visité
                depth_first_search_recursive(graph, neighbor)  # lance la récursion
        print("return")

    depth_first_search_recursive(graph, source_node)  # lance la fonction récursive


def depth_first_search_routing(graph, source_node):
    visited = []  # stocke les noeuds visités
    routes = {}  # stocke les routes

    def depth_first_search_recursive(graph, current_node, path):

        visited.append(current_node)  # on ajoute le noeud comme visité
        routes[current_node] = path
        # print(current_node, "path :", repr(path))

        for neighbor in graph[current_node]:  # pour chaque noeud voisin
            if neighbor not in visited:  # s'il n'a pas déjà été visité
                depth_first_search_recursive(graph, neighbor, path + [neighbor])  # lance la récursion
        # print("return")

    depth_first_search_recursive(graph, source_node, [source_node])  # lance la fonction récursive + tableau du chemmin

    return routes


'''
Test dept_first_search
'''
# graph = [[1, 2, 5], [0, 2, 5], [0, 1], [4, 5], [3, 5], [0, 1, 3, 4]]
# depth_first_search(graph, 0)

'''
Test dept_first_search_routing
'''
# graph1 = [[1, 2, 5], [0, 2, 5], [0, 1], [4, 5], [3, 5], [0, 1, 3, 4]]
# depth_first_search_routing(graph, 0)

'''
Test dept_first_search_routing
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
# routes = depth_first_search_routing(maze, location)
# print(repr(routes))
