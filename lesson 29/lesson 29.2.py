from collections import deque

def bfs(graph, start):
    queue = deque([(start, 0)])
    visited = set([start])
    shortest_paths = {start: 0}

    while queue:
        node, distance = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)
                shortest_paths[neighbor] = distance + 1

    return shortest_paths


def all_pairs_shortest_paths(graph):
    all_shortest_paths = {}
    vertices = graph.keys()

    for vertex in vertices:
        shortest_paths = bfs(graph, vertex)
        all_shortest_paths[vertex] = shortest_paths

    return all_shortest_paths


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

shortest_paths = all_pairs_shortest_paths(graph)


for start_vertex, paths in shortest_paths.items():
    print(f"Найкоротші шляхи для вершини {start_vertex}:")
    for end_vertex, distance in paths.items():
        print(f"Шлях до вершини {end_vertex}: {distance}")
    print()