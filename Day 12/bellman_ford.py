def bellman_ford(n, edges, src):
    INF = float('inf')
    dist = [INF]*n
    dist[src] = 0
    
    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None
    
    return dist
    
n = 3
edges = [
    [0, 1, 1],
    [1, 2, -1],
    [2, 1, -1],
]

src = 0
print(bellman_ford(n, edges, src))
