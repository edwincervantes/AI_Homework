import matplotlib.pyplot as plt
import networkx as nx

# Create the weigh Graph representing the map
G = nx.Graph()

G.add_edge("Oradea", "Zerind", weight=71)
G.add_edge("Oradea", "Sibiu", weight=151)
G.add_edge("Zerind", "Arad", weight=75)
G.add_edge("Arad", "Sibiu", weight=140)
G.add_edge("Arad", "Timisoara", weight=118)
G.add_edge("Timisoara", "Lugoj", weight=111)
G.add_edge("Lugoj", "Mehadia", weight=70)
G.add_edge("Mehadia", "Drobeta", weight=75)
G.add_edge("Drobeta", "Craiova", weight=120)
G.add_edge("Craiova", "Rimnicu Vilcea", weight=146)
G.add_edge("Craiova", "Pitesti", weight=138)
G.add_edge("Rimnicu Vilcea", "Sibiu", weight=80)
G.add_edge("Pitesti", "Rimnicu Vilcea", weight=97)
G.add_edge("Sibiu", "Fagaras", weight=99)
G.add_edge("Fagaras", "Bucharest", weight=211)
G.add_edge("Bucharest", "Pitesti", weight=101)
G.add_edge("Bucharest", "Giurgiu", weight=90)
G.add_edge("Bucharest", "Urziceni", weight=85)
G.add_edge("Urziceni", "Hirsova", weight=98)
G.add_edge("Urziceni", "Vaslui", weight=142)
G.add_edge("Hirsova", "Eforie", weight=86)
G.add_edge("Vaslui", "Iasi", weight=92)
G.add_edge("Iasi", "Neamt", weight=87)


def find_path_bfs(graph, starting_node, ending_node):
    '''

    :param graph: A Networkx graph
    :param starting_node: Node you wish to begin at
    :param ending_node: Node you wish to end at
    :return: A path from starting node to end node and the weight of the path
    '''
    visited = []
    queue = [[starting_node]]

    try:
        # Always start with the last element of queue as this is our last visited node
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbors = []
                # Find what edges connects these two nodes and make them neighbors
                for edge in graph.edges:
                    if edge[0] == node:
                        neighbors.append(edge[1])
                    elif edge[1] == node:
                        neighbors.append(edge[0])

                # Add the neighbor to the path and add the path to the queue
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    # Found our destination, return weight and both
                    if neighbor == ending_node:
                        weight = nx.path_weight(graph, new_path, 'weight')
                        return new_path, weight
                # Add the node to visited so we don't repeat nodes
                visited.append(node)
    finally:
        RuntimeError('Path does not exist')


bfs_path_1, bfs_weight_1 = find_path_bfs(G, "Oradea", "Bucharest")
bfs_path_2, bfs_weight_2 = find_path_bfs(G, "Timisoara", "Bucharest")
bfs_path_3, bfs_weight_3 = find_path_bfs(G, "Neamt", "Bucharest")
print("Path from Oradea to Bucharest via BFS: {}, weight: {}".format(bfs_path_1, bfs_weight_1))
print("Path from Timisoara to Bucharest via BFS: {}, weight: {}".format(bfs_path_2, bfs_weight_2))
print("Path from Neamt to Bucharest via BFS: {}, weight: {}".format(bfs_path_3, bfs_weight_3))

