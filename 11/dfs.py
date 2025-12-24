def dfs(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return order

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(dfs(graph, 'A'))


