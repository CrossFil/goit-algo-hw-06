import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

line1 = ["Saltivska", "Heroiv Pratsi", "Studentska", "Akademika Barabashova", 
         "Kyivska", "Pivdennyi Vokzal", "Maidan Konstytutsii", "Istorychny Myzei"]
line2 = ["Kholodna Hora", "Pivdennyi Vokzal", "Tsentr Rynok", "Maidan Konstytutsii",
         "Pivdenna", "Armiiska", "Traktornyi Zavod", "Proletarska"]
line3 = ["Oleksiivska", "Peremoha", "Maidan Nauk", "Botanichnyi Sad", 
         "Naukova", "23 Serpnia", "Metrobudivnykiv"]

def add_line(line, color):
    edges = [(line[i], line[i+1]) for i in range(len(line)-1)]
    G.add_edges_from(edges, color=color)

add_line(line1, 'blue')
add_line(line2, 'red')
add_line(line3, 'green')

pos = nx.spring_layout(G)
edges = G.edges(data=True)
colors = [e[2]['color'] for e in edges]

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=colors)

plt.title("Kharkiv Metro Network")
plt.show()

# DFS implementation
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# BFS implementation
def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Test DFS and BFS
start_station = "Saltivska"
goal_station = "Maidan Konstytutsii"

print(f"DFS paths from {start_station} to {goal_station}:")
dfs_paths = list(dfs(G, start_station, goal_station))
for path in dfs_paths:
    print(path)

print(f"\nBFS paths from {start_station} to {goal_station}:")
bfs_paths = list(bfs(G, start_station, goal_station))
for path in bfs_paths:
    print(path)
