graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D', 'C']
}

def has_cycle_undirected(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            stack = [(start, None)]
            visited.add(start)

            while stack:
                node, parent = stack.pop()

                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, node))
                    elif neighbor != parent:
                        return True
    return False

print(has_cycle_undirected(graph))
