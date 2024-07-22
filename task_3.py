import heapq

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

graph = {}
for u, v, w in edges:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        

        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
           
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


start_node = "Naukova"
shortest_paths = dijkstra(graph, start_node)


print(f"Shortest paths from {start_node}:")
for destination in shortest_paths:
    print(f"To {destination}: {shortest_paths[destination]}")
