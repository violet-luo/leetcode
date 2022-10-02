def countComponents(self, n: int, edges: List[List[int]]) -> int:
    neighbors = collections.defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    
    res = 0
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        else:
            res += 1
            visited.add(i)
            self.bfs(i, neighbors, visited)
    return res
        
def bfs(self, root, neighbors, visited):
    queue = collections.dequeueue([root])
    while queue:
        node = queue.popleft()
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
