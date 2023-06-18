from collections import defaultdict


def dfs(graph, node, visited, stack):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)

    stack.append(node)


def get_transposed_graph(graph):
    transposed_graph = defaultdict(list)

    for node in graph:
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)

    return dict(transposed_graph)


def find_strongly_connected_components(graph):
    visited = set()
    stack = []
    components = []

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)

    transposed_graph = get_transposed_graph(graph)
    visited.clear()

    while stack:
        node = stack.pop()

        if node not in visited:
            component = []
            dfs(transposed_graph, node, visited, component)
            components.append(component)

    return components


graph = {
    'A': ['B'],
    'B': ['C', 'E', 'F'],
    'C': ['D', 'G'],
    'D': ['C', 'H'],
    'E': ['A', 'F'],
    'F': ['G'],
    'G': ['F'],
    'H': ['D', 'G']
}

strongly_connected_components = find_strongly_connected_components(graph)

for component in strongly_connected_components:
    print(component)