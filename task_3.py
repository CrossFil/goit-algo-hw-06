import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ("Heroiv Pratsi", "Studentska", 3),
    ("Studentska", "Akademika Barabashova", 2),
    ("Akademika Barabashova", "Akademika Pavlova", 4),
    ("Akademika Pavlova", "Kholodna Hora", 3),
    ("Kholodna Hora", "Pivdennyi Vokzal", 1),
    ("Pivdennyi Vokzal", "Tsentralnyi Rynok", 2),
    ("Tsentralnyi Rynok", "Maіdan Konstytutsii", 3),
    ("Maіdan Konstytutsii", "Istorychnyi Muzei", 1),
    ("Istorychnyi Muzei", "Universytet", 2),
    ("Universytet", "Naukova", 2),
    ("Naukova", "Botanіchnyi Sad", 2),
    ("Botanіchnyi Sad", "23 Serpnia", 3),
    ("23 Serpnia", "Heroiv Pratsi", 3),
    ("Maіdan Konstytutsii", "Zakhysnykiv Ukrainy", 2),
    ("Zakhysnykiv Ukrainy", "Metrobudivnykiv", 1),
    ("Metrobudivnykiv", "Palats Sportu", 3),
    ("Palats Sportu", "Armiiska", 2),
    ("Armiiska", "Akademika Pavlova", 3)
]

G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

def dijkstra_all_pairs(graph):
    shortest_paths = dict(nx.all_pairs_dijkstra_path(graph))
    shortest_lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    return shortest_paths, shortest_lengths

shortest_paths, shortest_lengths = dijkstra_all_pairs(G)

source = "Naukova"
print(f"Shortest paths from {source}:")
for target in G.nodes():
    if target != source:
        print(f"To {target}: Path: {shortest_paths[source][target]}, Length: {shortest_lengths[source][target]}")
