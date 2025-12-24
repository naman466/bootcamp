class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def topological_sort(nodes):
    visited = set()
    order = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for child in node.children:
                dfs(child)
            order.append(node)  

    for node in nodes:
        if node not in visited:
            dfs(node)

    order  
    return order

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.children = [b, c]
b.children = [d]
c.children = [d]

sorted_nodes = topological_sort([a, b, c, d])
print([node.value for node in sorted_nodes])

