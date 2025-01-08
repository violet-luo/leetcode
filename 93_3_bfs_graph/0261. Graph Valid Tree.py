def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1: # 有环
        return False
    
    neighbors = collections.defaultdict(list)
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    
    q = collections.deque([0]) # start from 0
    visited = {0}

    while q:
        node = q.popleft()
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                q.append(neighbor) # ([1,2,3])
                visited.add(neighbor)
    
    # 如果能遍历完所有的点，且没有环存在，那么说明这个无向图是树
    # if len(visited) < n: 有没有遍历的点
    return len(visited) == n
