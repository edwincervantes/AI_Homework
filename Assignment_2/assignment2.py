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


def bfs(graph, starting_node):
    visited = []
    queue = [starting_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for edge in graph.edges:
                if edge[0] == node:
                    queue.append(edge[1])
                elif edge[1] == node:
                    queue.append(edge[0])
    return visited


print(bfs(G, "Bucharest"))
