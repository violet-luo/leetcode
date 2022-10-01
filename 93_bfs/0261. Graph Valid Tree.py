def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    # 每个点和它的邻居
    neighbors = collections.defaultdict(list)
    # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)

    visited = set()
    queue = collections.deque([0])

    while queue:
        node = queue.popleft() #0
        visited.add(node) # {0: True}
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                visited.add(neighbor) # (0, 1, 2, 3, 4)
                queue.append(neighbor) # ([1,2,3])

    return len(visited) == n
